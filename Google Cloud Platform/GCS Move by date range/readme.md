## 🐍 GCS Python Scripts

This repository contains Python scripts for automating routine tasks on Google Cloud Platform (GCP).

### ☁️ `gcs_move_by_date.py`

This script provides a robust and efficient way to move objects between Google Cloud Storage (GCS) buckets based on their creation date. It's an excellent tool for data lifecycle management, archival, and cleanup.

### ⚙️ How it Works

1. **Client Initialization** : The script first uses the `google-cloud-storage` library to authenticate and connect to your GCP project.
2. **Bucket Validation** : It checks if both the source and destination buckets exist and are accessible to the user or service account.
3. **Date Filtering** : It lists all objects in the source bucket and filters them based on the **`time_created`** metadata, moving only those objects that fall within the specified date range.
4. **Copy and Delete** : For each identified object, the script performs a **copy** operation to the destination bucket and then **deletes** the original object from the source bucket. This atomic process ensures data integrity during the move.
5. **Logging** : All operations, including successes and failures, are logged to a timestamped file for easy auditing and troubleshooting.

---

### 🛠️ Installation & Usage

#### 1. **Prerequisites**

- Python 3.6+
- Google Cloud SDK installed and authenticated on your machine.
- Your GCP project ID is set in your environment or the script.

#### 2. **Install Requirements**

First, you need to install the necessary Python library using **`pip`** . It's highly recommended to use a virtual environment.

```
pip install google-cloud-storage
```

#### 3. **Run the Script**

Execute the script from your terminal, providing the start and end dates as arguments.

```
python gcs_move_by_date.py --start-date YYYY-MM-DD --end-date YYYY-MM-DD
```

**Example:**

To move all files created in October 2023:

```
python gcs_move_by_date.py --start-date 2023-10-01 --end-date 2023-10-31
```

---

### 🔒 IAM Permissions for Production

For a service account to run this script in a production environment, it needs the following IAM roles on the respective buckets:

- **Source Bucket (`your-source-bucket`)** :
- **Storage Object Viewer** : Required to list and read object metadata.
- **Storage Object Deleter** : Required to delete the original files.
- **Destination Bucket (`your-destination-bucket`)** :
- **Storage Object Creator** : Required to write new objects to the bucket.

> **Note** : For simplicity, the **Storage Object Admin** role can be granted on both buckets, as it includes all the necessary permissions. However, for a principle of least privilege, it's best practice to grant the specific roles listed above.
