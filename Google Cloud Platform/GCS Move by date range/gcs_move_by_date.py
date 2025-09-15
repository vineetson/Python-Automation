import argparse
import os
import sys
from datetime import datetime
from google.cloud import storage

# --- Configuration ---
SOURCE_BUCKET = "demo-bucket-src"
DESTINATION_BUCKET = "demo-bucket-mv"


def get_bucket_and_client(bucket_name):
    """
    Initializes a GCS client and gets a bucket object.
    """
    try:
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        if not bucket.exists():
            print(
                f"Error: Bucket '{bucket_name}' does not exist or you don't have permissions.")
            return None, None
        return bucket, client
    except Exception as e:
        print(f"Error initializing client for bucket '{bucket_name}': {e}")
        return None, None


def move_gcs_objects_by_date(source_bucket_name, dest_bucket_name, start_date_str, end_date_str):
    """
    Moves GCS objects from a source bucket to a destination bucket based on creation date.
    """
    try:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        # Set end date to the end of the day
        end_date = datetime.strptime(
            end_date_str, "%Y-%m-%d").replace(hour=23, minute=59, second=59)
    except ValueError:
        print("Error: Invalid date format. Please use YYYY-MM-DD.")
        sys.exit(1)

    source_bucket, _ = get_bucket_and_client(source_bucket_name)
    dest_bucket, _ = get_bucket_and_client(dest_bucket_name)

    if not source_bucket or not dest_bucket:
        sys.exit(1)

    print(
        f"Starting data move for objects created between {start_date_str} and {end_date_str}...")

    # Log file for moved items
    log_filename = f"gcs_move_by_date_{datetime.now().strftime('%Y%m%d%H%M%S')}.log"
    print(f"Log file for this operation: {log_filename}")

    files_to_move = []

    # List and filter objects
    print("Listing objects and filtering by creation date...")
    with open(log_filename, "w") as log_file:
        for blob in source_bucket.list_blobs():
            if start_date <= blob.time_created.replace(tzinfo=None) <= end_date:
                files_to_move.append(blob)

        if not files_to_move:
            print("No files found within the specified date range. No action taken.")
            log_file.write("No files found within the specified date range.\n")
            sys.exit(0)

        print(f"Found {len(files_to_move)} files to move.")
        log_file.write(f"Found {len(files_to_move)} files to move.\n")

        # Perform the move operation
        success_count = 0
        failure_count = 0
        print("Performing move operation...")
        for blob in files_to_move:
            source_path = blob.name
            dest_path = blob.name  # Maintains folder structure

            print(
                f"Moving: {source_path} to gs://{dest_bucket_name}/{dest_path}")
            log_file.write(
                f"Moving: {source_path} to gs://{dest_bucket_name}/{dest_path}\n")

            try:
                # Get the source blob and copy to destination
                source_blob = source_bucket.blob(source_path)

                # Check if the blob actually exists before attempting to move
                if not source_blob.exists():
                    print(
                        f"Warning: Source blob '{source_path}' no longer exists. Skipping.")
                    log_file.write(
                        f"Warning: Source blob '{source_path}' no longer exists. Skipping.\n")
                    failure_count += 1
                    continue

                source_bucket.copy_blob(source_blob, dest_bucket, dest_path)
                source_blob.delete()
                success_count += 1
                print(f"Successfully moved: {source_path}")
                log_file.write(f"Successfully moved: {source_path}\n")

            except Exception as e:
                failure_count += 1
                print(f"Failed to move {source_path}: {e}")
                log_file.write(f"Failed to move {source_path}: {e}\n")

        print("\nMove operation summary:")
        print(f"Total files identified for move: {len(files_to_move)}")
        print(f"Successfully moved: {success_count}")
        print(f"Failed to move: {failure_count}")
        print(
            f"A detailed log of this operation can be found at: {log_filename}")

        log_file.write("\nMove operation summary:\n")
        log_file.write(
            f"Total files identified for move: {len(files_to_move)}\n")
        log_file.write(f"Successfully moved: {success_count}\n")
        log_file.write(f"Failed to move: {failure_count}\n")

    if failure_count == 0:
        print("All identified files moved successfully! 🎉")
    else:
        print("Warning: Some files failed to move. Please check the logs for details. ⚠️")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Move GCS objects by creation date.")
    parser.add_argument("--start-date", required=True,
                        help="Start date (YYYY-MM-DD).")
    parser.add_argument("--end-date", required=True,
                        help="End date (YYYY-MM-DD).")

    args = parser.parse_args()

    # Confirmation
    confirmation = input(
        f"Are you sure you want to MOVE data created between {args.start_date} and {args.end_date} from gs://{SOURCE_BUCKET} to gs://{DESTINATION_BUCKET}? (yes/no): ")
    if confirmation.lower() != 'yes':
        print("Operation cancelled by user.")
        sys.exit(0)

    move_gcs_objects_by_date(
        SOURCE_BUCKET, DESTINATION_BUCKET, args.start_date, args.end_date)
