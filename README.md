

# english-audio-to-persian-text
This is the primary repository for deploying a project that consists of multiple microservices organized as submodules.
## Dependencies
install docker and docker compose

### Prerequisites
clone git submodules by this command:
```
git submodule update --init --recursive
```

##### Model Configuration

###### Configure ASR Model
It is recommended to use this lightweight model:
- **Download**: [Vosk English Model](https://alphacephei.com/vosk/models/vosk-model-en-us-0.22-lgraph.zip)
- **Setup**:
  1. Unzip the downloaded file.
  2. Place the unzipped folder in the directory specified by `ASR_MODELS` in your `.dockerenv` file.
  3. Configure the `MODEL_NAME` in the ASR microservice configuration.

###### Configure Translation Model
sample .dockerenv file:
```
ASR_MODELS=/Users/...a/asr_models/models
TRANSLATION_MODELS=/Users/...a/translation_models/models
```
It is recommended to use this lightweight model:
- **Download**: [Argos Translate English-Persian Model](https://argos-net.com/v1/translate-en_fa-1_5.argosmodel)
- **Setup**:
  1. Place the downloaded file in the directory specified by `TRANSLATION_MODELS` in your `.dockerenv` file.
  2. Configure the `MODEL_NAME` in the Translation microservice configuration.

sample .dockerenv file:
```
ASR_MODELS=/Users/...a/asr_models/models
TRANSLATION_MODELS=/Users/...a/translation_models/models
```

###### Run Project

```
docker-compose --env-file .dockerenv up -d
```
