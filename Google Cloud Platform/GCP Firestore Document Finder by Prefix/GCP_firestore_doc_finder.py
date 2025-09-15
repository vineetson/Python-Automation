import os
import logging
from google.cloud import firestore
from google.cloud.exceptions import NotFound
from typing import Optional

# --- Configuration ---


class Config:
    """Centralized configuration loaded from environment variables."""
    PROJECT_ID: Optional[str] = os.environ.get("PROJECT_ID")
    DATABASE_ID: Optional[str] = os.environ.get("DATABASE_ID")
    COLLECTION: Optional[str] = os.environ.get("COLLECTION")
    DOCUMENT_ID_PREFIX: str = "pay"


# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# --- Singleton for Firestore Client ---
_firestore_client = None


def get_firestore_client() -> firestore.Client:
    """Initializes and returns a singleton Firestore client instance."""
    global _firestore_client
    if _firestore_client:
        return _firestore_client

    try:
        if not Config.PROJECT_ID or not Config.DATABASE_ID or not Config.COLLECTION:
            raise ValueError(
                "Required environment variables PROJECT_ID, DATABASE_ID, or COLLECTION are not set.")

        logging.info(
            f"Initializing Firestore client for project '{Config.PROJECT_ID}' and database '{Config.DATABASE_ID}'")
        _firestore_client = firestore.Client(
            project=Config.PROJECT_ID, database=Config.DATABASE_ID)
        logging.info("Firestore client initialized successfully.")
        return _firestore_client
    except exceptions.GoogleAPICallError as e:
        logging.error(f"API error during Firestore client initialization: {e}")
        raise
    except Exception as e:
        logging.error(
            f"An unexpected error occurred during Firestore client initialization: {e}")
        raise


def get_documents_by_id_prefix(firestore_client: firestore.Client, collection_name: str, id_prefix: str):
    """
    Finds and displays all documents where the document ID starts with a given prefix,
    using an efficient server-side query.
    """
    logging.info(
        f"\n--- Finding documents in '{collection_name}' with ID prefix: '{id_prefix}' ---")
    try:
        collection_ref = firestore_client.collection(collection_name)

        # Build the end prefix for the range query
        end_prefix = id_prefix + '\uf8ff'

        # Query Firestore for documents in the specified ID range
        query = collection_ref.order_by(firestore.DocumentReference.field_path).start_at({
            '__name__': id_prefix
        }).end_before({
            '__name__': end_prefix
        })

        docs = query.stream()

        found_docs = False
        for doc in docs:
            found_docs = True
            logging.info(f"\nDocument ID: {doc.id}")
            logging.info(f"Document data: {doc.to_dict()}")

        if not found_docs:
            logging.info(f"No documents found with ID prefix '{id_prefix}'.")

    except Exception as e:
        logging.error(f"An error occurred while querying for documents: {e}")


def main():
    """Main execution function."""
    try:
        client = get_firestore_client()
        if client and Config.COLLECTION:
            get_documents_by_id_prefix(
                client, Config.COLLECTION, Config.DOCUMENT_ID_PREFIX)
        else:
            raise ValueError("Configuration or client initialization failed.")
    except Exception as e:
        logging.critical(f"Script failed to run: {e}")
        exit(1)


if __name__ == "__main__":
    main()
