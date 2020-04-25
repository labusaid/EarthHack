import os
from time import sleep
# from picamera import PiCamera
# Imports the Google Cloud client library
from google.cloud import storage, firestore

# GCP Storage setup
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="earthxhack-2020-0dd11a74799e.json"
client = storage.Client()
# Static data for GCP call
bucket_name = "earthxhack-2020.appspot.com"
source_file_name = "temp.jpg"
destination_blob_name = "temp"

print('Credendtials from environ: {}'.format(
    os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')))

# Uploads blob to GCP from file
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # bucket_name = "your-bucket-name"
    # source_file_name = "local/path/to/file"
    # destination_blob_name = "storage-object-name"

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

# Add a new document
db = firestore.Client()
doc_ref = db.collection(u'users').document(u'alovelace')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
})

# Upload image to GCP
upload_blob(bucket_name, source_file_name, destination_blob_name)