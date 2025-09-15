from google.cloud import storage
import logging

def list_gcs_objects(bucket_name):
    """Lists all the objects in the specified GCS bucket."""
    storage_client = storage.Client()
    try:
        blobs = storage_client.list_blobs(bucket_name)
        object_names = [blob.name for blob in blobs]
        if object_names:
            print(f"Objects in bucket '{bucket_name}':")
            for name in object_names:
                print(f"- {name}")
        else:
            print(f"No objects found in bucket '{bucket_name}'.")
    except Exception as e:
        logging.error(f"Failed to list objects in bucket '{bucket_name}': {e}")

if __name__ == '__main__':
    bucket_name = 'your-bucket-name'  # Replace with your actual bucket name
    list_gcs_objects(bucket_name)