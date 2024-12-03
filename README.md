# Whisper Transcription

A Python script for transcribing audio files using the [Whisper](https://github.com/openai/whisper) model.

## Features

- **Language-Specific Transcription:** Specify the language for transcription through command-line arguments.
- **GPU Acceleration Support:** Utilizes CUDA for faster processing if a compatible GPU is available.
- **Detailed Logging:** Logs processing steps, performance metrics, and errors to assist in monitoring and debugging.
- **Automated Directory Handling:** Processes all audio files within specified directories and organizes transcriptions accordingly.
- **Error Handling:** Gracefully handles errors during transcription, ensuring uninterrupted processing of remaining files.

## Requirements

- **Python 3.7+**
- [Whisper](https://github.com/openai/whisper)

## Model

This script uses the "turbo" model of Whisper, which is the best in terms of transcription accuracy and computation performance.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/whisper-transcription.git
    cd whisper-transcription
    ```

2. **Install the dependencies:**

    - Follow [Whisper](https://github.com/openai/whisper) instructions

## Usage

Run the transcription script with the desired language and model:

```bash
python transcribe.py --language en --model turbo
```

Replace en with the appropriate language code (e.g., it for Italian) and turbo with the desired model (e.g., base, small, medium, large, turbo). By default english language and turbo model are selected.

Note: If no language is specified, the default language is set to English (en). Only medium, large and turbo models support multilingual transcription.

## Configuration

- **Audio Files Directory:** Place your audio files in the ./audio_files directory. The script will process each subdirectory within this directory.
- **Transcription Output:** Transcriptions are saved in the ./audio_texts directory, maintaining the same subdirectory structure as the audio files.

## Logging
Logs are output to the console with detailed information about the processing status and performance metrics, including:

- Device information (CPU or GPU details)
- Processing time per file
- Total files processed
- Total processing time

## Improvements needed
- Multiple voice recognizer
