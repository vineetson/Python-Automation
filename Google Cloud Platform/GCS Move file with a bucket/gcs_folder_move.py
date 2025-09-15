from google.cloud import storage
from google.cloud.exceptions import NotFound
import logging
import os

# Configure logging at the beginning of your script
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def check_and_move_object_optimized(
    bucket_name: str,
    source_folder: str,
    destination_folder: str,
    object_name: str,
):
    """
    Checks if an object exists in the source folder of a GCS bucket and moves it to the destination folder.

    Args:
        bucket_name (str): The name of your GCS bucket.
        source_folder (str): The source folder name (e.g., 'raw/').
        destination_folder (str): The destination folder name (e.g., 'processed/').
        object_name (str): The name of the object to find and move.
    """
    source_path = os.path.join(source_folder, object_name).replace('\\', '/')
    destination_path = os.path.join(
        destination_folder, object_name).replace('\\', '/')

    try:
        client = storage.Client()
        bucket = client.bucket(bucket_name)

        source_blob = bucket.blob(source_path)

        logging.info(
            f"Attempting to move '{source_path}' to '{destination_path}' in bucket '{bucket_name}'...")

        # The rename_blob operation is atomic and handles existence checks implicitly.
        new_blob = bucket.rename_blob(source_blob, destination_path)

        logging.info(
            f"Successfully moved '{source_path}' to '{destination_path}'.")
        logging.info(f"New object size: {new_blob.size} bytes")
        logging.info(f"New object creation time: {new_blob.time_created}")

    except NotFound:
        logging.warning(
            f"Object '{object_name}' not found in folder '{source_folder}'. No action taken.")

    except Exception as e:
        logging.error(
            f"An error occurred while processing '{object_name}': {e}")


# --- Configuration ---
YOUR_BUCKET_NAME = "demo-poc"
OBJECT_FILENAME_TO_MOVE = "c-123457.txt"
SOURCE_FOLDER = "raw/"
DESTINATION_FOLDER = "processed/"

# --- Run the script ---
if __name__ == "__main__":
    logging.info("Starting object move process...")
    check_and_move_object_optimized(
        bucket_name=YOUR_BUCKET_NAME,
        source_folder=SOURCE_FOLDER,
        destination_folder=DESTINATION_FOLDER,
        object_name=OBJECT_FILENAME_TO_MOVE,
    )
    logging.info("Process completed.")
