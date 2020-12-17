import os, re, random
import requests, json, base64
from time import sleep
# Imports the Google Cloud client library
from google.cloud import firestore

# GCP Storage setup
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "earthxhack-2020-0c81af847185.json"
db = firestore.Client()

# Device identifier
plant_num = 1

# Raspi Stuff (Commented out to run on a non-pi)
from picamera import PiCamera

# Capture image from camera and save to img/temp.jpg
camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()  # used for when pi gui is open
sleep(2)  # Camera warm-up time
camera.capture('img/plant.jpg')

# Context Manager for img files
with open('img/plant.jpg', "rb") as img_file:
    base64string = base64.b64encode(img_file.read())  # encode image in base64
    file_url = 'img/plant.jpg'

# endpoint and static header information
url = "https://fu9gq38ul8.execute-api.us-east-2.amazonaws.com/Testing/getprobabilities"
headers = {
    'Content-Type': 'application/json'
}

# embed base64 encoded image in request body
payload = "{\n  \"image\": \"data:image/jpeg;base64," + str(base64string) + "\",\n  \"file_url\": \"plant.jpg\"\n}"

# Make POST request
r = requests.request("POST", url, headers=headers, data=payload)

# Handle response
statuses = ["Healthy leaf", "Healthy tomato", "Unhealthy leaf", "Unhealthy tomato"]
response = r.text  # extracting response text
response = re.sub('[^0-9]', '', response)  # remove all non-numeric
n = 7  # digits per confidence value
decoded_response = [response[i:i + n] for i in range(0, len(response), n)]
print(f'decoded_response: {decoded_response}')

# Gets max value
highest_val = max(decoded_response)
doc_ref = db.collection(u'plants').document(f'plant{plant_num}')
# Make sure we are confident in highest_val
if float(highest_val) > .5:
    highest_name = decoded_response.index(highest_val)
    print(statuses[highest_name])
    doc_ref.set({
        u'status': statuses[highest_name]
    })
# Default to undetermined status
else:
    doc_ref.set({
        u'status': 'Undetermined Status'
    })

# Send plant health data (generating random correlated data for demo purposes)
metrics_data = db.collection(f'metrics{plant_num}')
growth = .5
for i in range(10):
    growth -= random.uniform(-.1, .1)
    metrics_data.document(f'plant_health{i}').set({
        'label': i,
        'value': growth
    })
