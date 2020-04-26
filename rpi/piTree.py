import os
import random

import requests, json, base64
from time import sleep
# from picamera import PiCamera
# Imports the Google Cloud client library
from google.cloud import storage, firestore

# GCP Storage setup
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "earthxhack-2020-0c81af847185.json"
client = storage.Client()
# Add a new document
db = firestore.Client()

# Static data for GCP call
bucket_name = "earthxhack-2020.appspot.com"
source_file_name = "img/temp.jpg"
destination_blob_name = "temp.jpg"


# Uploads blob to GCP from file
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )


# # Capture image from camera and save to img/temp.jpg
# camera = PiCamera()
# camera.resolution = (1024, 768)
# # camera.start_preview() # used for when pi gui is open
# sleep(2) # Camera warm-up time
# camera.capture('img/temp.jpg')

# defining the api-endpoint
API_ENDPOINT = "https://runtime.sagemaker.us-east-2.amazonaws.com/endpoints/sample-endpoint-201CE626-5EC5-4030-9236-7D6A10F55C65-1/invocations"
# your API key here
API_KEY = "XXXXXXXXXXXXXXXXX"
# data to be sent to api
data = {'content_type': 'image/jpg',
        'Accept': 'Accept',

        }

with open("img/Healthy_leaf.jpg", "rb") as img_file:
    my_string = base64.b64encode(img_file.read())
print(my_string)

# sending post request and saving response as response object
r = requests.post(url=API_ENDPOINT, data=my_string)

# extracting response text
response = r.text
print(f'response:  {response}')
# response = '{"Healthy_Leaf": "0.000001", "Healthy_Tomato": "0.000000", "Unhealthy_Leaf": "0.999998","Unhealthy_Tomato": "0.000000"}'

# Decodes JSON into a python dictionary
decoded_response = json.loads(response)
# Gets max value
highest_val = max(decoded_response, key=decoded_response.get)
doc_ref = db.collection(u'plants').document(u'plant1')
# if float(decoded_response[highest_val]) > .5:
#     doc_ref.set({
#         u'status': highest_val
#     })

metrics_data = db.collection(u'metrics3')
growth = 0
for i in range(10):
    growth += random.uniform(0, .1)
    metrics_data.document(f'plant_health{i}').set({
        'label': i,
        'value': growth
    })

# Upload image to GCP
# upload_blob(bucket_name, source_file_name, destination_blob_name)
