# Demo

This is a demo script that demonstrates how to interact with the **TaskOrchestrator API**. The script will upload an audio file for transcription, and then repeatedly check for the result until it is ready.

## Prerequisites

Before running the demo, ensure the following services are up and running:

- **TaskOrchestrator API**: The API that manages the processing of the audio files, coordinates ASR, and translation services.
- **RabbitMQ**: The message broker used for communication between services.
- **Translation**: The Translation microservice receives English text and translates it into Persian.
- **ASR**: The ASR microservice receives an English audio file (in .wav format) and transcribes it into English text.

#### Project Requirements
Install poetry with ths command
```
curl -sSL https://install.python-poetry.org | python3 -
```
and
```
export PATH="$HOME/.local/bin:$PATH"
```
install all requirements with this command:
```
 poetry install
```

 ### Run demo
Run the demo with this command:
```
poetry run python demo.py
```