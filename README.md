# Whisper Transcription

A Python script for transcribing audio and video files using the [Whisper](https://github.com/openai/whisper) model.

## Requirements
- Python 3.7+
- ffmpeg (required by Whisper, see [installation instructions](https://github.com/openai/whisper))
- CUDA-compatible GPU (optional, for acceleration)

## Features

- **Language-Specific Transcription:** Specify the language for transcription through command-line arguments.
- **GPU Acceleration Support:** Utilizes CUDA for faster processing if a compatible GPU is available.
- **Detailed Logging:** Logs processing steps, performance metrics, and errors to assist in monitoring and debugging.
- **Automated Directory Handling:** Processes all audio files within specified directories and organizes transcriptions accordingly.
- **Error Handling:** Gracefully handles errors during transcription, ensuring uninterrupted processing of remaining files.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/simog-dev/Ready-Whisper.git
    cd Ready-Whisper
    ```

2. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    - **You must have 'ffmpeg' installed on your system**, for further instructions please see [Whisper](https://github.com/openai/whisper)

## Usage

Run the transcription script with the desired language and model:

```bash
python transcribe.py --language en --model turbo
```

- Replace **en** with the appropriate language code (e.g., it for Italian) and **turbo** with the desired model (e.g., base, small, medium, large, turbo). 
- By default english language and turbo model are selected.

- **Note**: Only medium, large and turbo models support multilingual transcription. For further details please see [Whisper](https://github.com/openai/whisper) repository.

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
