import requests
import time

# Config
BASE_URL = "http://localhost:8000"

start_time = time.time()
file_path = "./test_audio_2.wav"

with open(file_path, "rb") as audio_file:
    response = requests.post(f"{BASE_URL}/process-audio/", files={"file": audio_file})

if response.status_code == 202:
    request_id = response.json()["request_id"]
    print(f"Request ID: {request_id}")
else:
    print("Failed to start processing")
    exit()

while True:
    result_response = requests.get(f"{BASE_URL}/result/", params={"request_id": request_id})
    result_data = result_response.json()

    if result_data["status"] == "completed":
        end_time = time.time()
        print(f"Transcription completed: {result_data['result']}")
        print(f"Time taken: {end_time - start_time:.2f} seconds")
        break
    elif result_data["status"] == "not_found":
        print("Request not found")
        break
    else:
        print("Still processing...")
        time.sleep(2)