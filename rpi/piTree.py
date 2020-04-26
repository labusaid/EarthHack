import os
import random

import requests, json, base64
from time import sleep
# from picamera import PiCamera
# import cv2
# Imports the Google Cloud client library
from google.cloud import storage, firestore

# GCP Storage setup
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "earthxhack-2020-0c81af847185.json"
db = firestore.Client()

# Firebase Storage (did not end up needing)
# Static data for GCP call
# client = storage.Client()
# bucket_name = "earthxhack-2020.appspot.com"
# source_file_name = "img/temp.jpg"
# destination_blob_name = "temp.jpg"
# Uploads blob to GCP from file
# def upload_blob(bucket_name, source_file_name, destination_blob_name):
#     storage_client = storage.Client()
#     bucket = storage_client.bucket(bucket_name)
#     blob = bucket.blob(destination_blob_name)
#
#     blob.upload_from_filename(source_file_name)
#
#     print(
#         "File {} uploaded to {}.".format(
#             source_file_name, destination_blob_name
#         )
#     )
# Upload image to GCP
# upload_blob(bucket_name, source_file_name, destination_blob_name)


# Raspi Stuff (Commented out to run on a non-pi)
# # Capture image from camera and save to img/temp.jpg
# camera = PiCamera()
# camera.resolution = (1024, 768)
# # camera.start_preview() # used for when pi gui is open
# sleep(2) # Camera warm-up time
# camera.capture('img/temp.jpg')

# defining the api-endpoint
API_ENDPOINT = "https://fu9gq38ul8.execute-api.us-east-2.amazonaws.com/Testing/getprobabilities"

plant_img = ["Healthy_tomato.jpg", "Healthy_leaf.jpg", "Unhealthy_Tomato.jpg"]

for plant_num in range(1, 4):
    print(f'plant_num: {plant_num}')

    # Context Manager for img files
    with open('img/'+ plant_img[plant_num - 1], "rb") as img_file:
        # temp = cv2.imread(plant_img[plant_num - 1])
        # test_img = cv2.cvtColor(temp, cv2.COLOR_BGR2RGB)
        # _, img_encoded = cv2.imencode('.jpg', test_img)
        # my_string = img_encoded.tostring()

        my_string = base64.b64encode(img_file.read())  # encode image in base64
        # print(my_string)

    # data to be sent to api
    data = {
        "data": my_string,
        "file_name": plant_img[plant_num - 1]
    }

    print(f'posting: {data}')

    r = requests.post(url=API_ENDPOINT,
                      data=data)  # sending post request and saving response as response object
    response = r.text  # extracting response text
    # response = '{"Healthy_Leaf": "0.000001", "Healthy_Tomato": "0.000000", "Unhealthy_Leaf": "0.999998","Unhealthy_Tomato": "0.000000"}'
    print(f'response: {response}')
    decoded_response = json.loads(response)  # Decodes JSON into a python dictionary

    # Gets max value
    highest_val = max(decoded_response, key=decoded_response.get)
    doc_ref = db.collection(u'plants').document(f'plant{plant_num}')
    if float(decoded_response[highest_val]) > .5:
        doc_ref.set({
            u'status': highest_val
        })

    metrics_data = db.collection(f'metrics{plant_num}')
    growth = .5
    for i in range(10):
        growth -= random.uniform(-.1, .1)
        metrics_data.document(f'plant_health{i}').set({
            'label': i,
            'value': growth
        })
