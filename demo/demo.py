import requests
import time
import logging
import os
import wave


logging.basicConfig(level=logging.INFO)  # Ensure INFO level logs are shown
logger = logging.getLogger(__name__)

# Config
BASE_URL = "http://localhost:8000"

start_time = time.time()
file_path = "./test_audio_2.wav"

file_size = os.path.getsize(file_path)  # in bytes

with wave.open(file_path, 'rb') as audio_file:
    frames = audio_file.getnframes()
    rate = audio_file.getframerate()
    duration = frames / float(rate)

logger.info(f"Audio duration: {duration:.2f} seconds")
logger.info(f"Audio size: {file_size/1000000:.2f} m")


with open(file_path, "rb") as audio_file:
    response = requests.post(f"{BASE_URL}/process-audio/", files={"file": audio_file})

if response.status_code == 202:
    request_id = response.json()["request_id"]
    logger.info(f"Request ID: {request_id}")
else:
    logger.error("Failed to start processing")
    exit()

# waite for creating request_id and saving to db
time.sleep(1)

while True:
    result_response = requests.get(f"{BASE_URL}/result/", params={"request_id": request_id})
    result_data = result_response.json()

    if result_data["status"] == "completed":
        end_time = time.time()
        logger.info(f"Transcription completed: {result_data['result']}")
        logger.info(f"Time taken: {end_time - start_time:.2f} seconds")
        break
    elif result_data["status"] == "not_found":
        logger.warning("Request not found")
        break
    else:
        logger.info("Still processing...")
        time.sleep(1)
