import os
import whisper
import torch
from pathlib import Path
import logging
import time
import argparse

def check_gpu_status():
    """Funzione diagnostica per verificare lo stato della GPU"""
    logger = logging.getLogger(__name__)
    logger.info("=== GPU Diagnostic Info ===")
    logger.info(f"CUDA available: {torch.cuda.is_available()}")
    logger.info(f"CUDA version: {torch.version.cuda}")
    if torch.cuda.is_available():
        logger.info(f"CUDA device count: {torch.cuda.device_count()}")
        logger.info(f"Current CUDA device: {torch.cuda.current_device()}")
        logger.info(f"Device name: {torch.cuda.get_device_name(0)}")
    logger.info("========================")

def get_transcription_path(audio_file):
    """Get the path where the transcription should be saved"""
    audio_dir_name = audio_file.parent.name
    texts_dir = Path('./audio_texts') / audio_dir_name
    texts_dir.mkdir(parents=True, exist_ok=True)
    return texts_dir / audio_file.name.replace(audio_file.suffix, '.txt')

def transcribe_file(audio_path, model, language=None):
    """Transcribe a single audio file using Whisper"""
    try:
        options = dict(language=language, without_timestamps=False)
        result = model.transcribe(str(audio_path), **options)
        return result["text"]
    except Exception as e:
        print(f"Error transcribing {audio_path}: {e}")
        return None

def main():
    # Configurazione logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Aggiungiamo diagnostica GPU
    check_gpu_status()

    parser = argparse.ArgumentParser(description="Transcribe audio files using Whisper.")
    parser.add_argument('--language', type=str, default='en', help='Language for transcription. Default: en')
    parser.add_argument('--model', type=str, default='turbo', help='Whisper model to use (e.g., base, small, medium, large, turbo). Default: turbo')
    args = parser.parse_args()

    start_time_total = time.time()
    files_processed = 0

    # Modifichiamo la gestione del device
    if not torch.cuda.is_available():
        logger.warning("CUDA non disponibile. Usando CPU.")
        device = "cpu"
    else:
        device = "cuda"
        torch.cuda.empty_cache()  # Puliamo la memoria GPU prima di iniziare
        
    logger.info(f"Using device: {device}")

    try:
        # Modifichiamo il caricamento del modello
        logger.info(f"Loading Whisper model on {device}...")
        model = whisper.load_model(args.model)
        model = model.to(device)  # Spostiamo esplicitamente il modello sul device
        logger.info("Model loaded successfully")
        
        # Get current directory
        current_dir = Path('./audio_files')
        if not current_dir.exists():
            logger.error(f"Directory {current_dir} does not exist!")
            return
        
        # Process each subdirectory
        for dir_path in current_dir.iterdir():
            if not dir_path.is_dir():
                continue
                
            logger.info(f"Processing directory: {dir_path}")
            
            # Process each audio file in directory
            for audio_file in dir_path.glob('*.*'):
                if audio_file.suffix.lower() not in ['.mp3', '.wav', '.m4a', '.mp4', '.flac', '.aac', '.ogg', '.wma', '.webm']:
                    continue
                # Get transcription file path
                output_file = get_transcription_path(audio_file)
                
                # Skip if transcription already exists
                if output_file.exists():
                    logger.info(f"Skipping {audio_file.name} - transcription already exists")
                    continue
                    
                logger.info(f"Transcribing: {audio_file.name}")
                start_time = time.time()
                
                # Transcribe audio
                transcription = transcribe_file(audio_file, model, language=args.language)
                
                if transcription:
                    # Save transcription
                    with open(output_file, 'w', encoding='utf-8') as f:
                        f.write(transcription)
                    
                    elapsed_time = time.time() - start_time
                    files_processed += 1
                    logger.info(f"Saved transcription to: {output_file}")
                    logger.info(f"Transcription time: {elapsed_time:.2f} seconds")

        total_time = time.time() - start_time_total
        logger.info(f"Total files processed: {files_processed}")
        logger.info(f"Total processing time: {total_time:.2f} seconds")

    except Exception as e:
        logger.error(f"An error occurred during execution: {str(e)}")
    finally:
        if device == "cuda":
            # Log final GPU memory state
            logger.info(f"Final GPU memory allocated: {torch.cuda.memory_allocated(0) / 1024**3:.2f} GB")
            torch.cuda.empty_cache()

if __name__ == "__main__":
    main()