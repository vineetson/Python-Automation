### 📂 GCP File Mover

This Python script is a modern and robust solution for automating file management in Google Cloud Storage (GCS). It's designed to find a specific file in a `raw/` folder and move it to a `processed/` folder within the same bucket. It uses best practices like proper logging and detailed error handling, making it perfect for production data pipelines.

---

### 🚀 Getting Started

#### **Prerequisites**

- **Python 3.x**
- **Google Cloud SDK** : Ensure you've authenticated with your GCP project using `gcloud auth login` and set your project with `gcloud config set project [YOUR_PROJECT_ID]`. The script uses **Application Default Credentials (ADC)** for seamless, secure authentication.

#### **Setup**

1. **Clone the repository** (if applicable) or save the script file.
2. **Create a virtual environment** to manage dependencies:

   ```
   python -m venv venv
   ```

3. **Activate the environment** :

```
   # On macOS/Linux
   source venv/bin/activate
   # On Windows
   venv\Scripts\activate
```

1. **Install the necessary library** :

```
   pip install google-cloud-storage
```

---

### 💻 How It Works

The script's core logic is within the `check_and_move_object_optimized` function.

1. **Client Initialization** : It creates a `storage.Client()` object, which automatically authenticates using your `gcloud` credentials.
2. **Path Construction** : It dynamically builds the full source and destination paths for the file.
3. **Atomic Move** : The script leverages the `bucket.rename_blob()` method. This is a highly efficient and **atomic** operation, meaning it renames the file in one step. This ensures data integrity—the file is either completely moved or remains in its original location, with no risk of duplication or corruption.
4. **Logging** : Instead of simple print statements, the script uses Python's built-in `logging` module. This provides structured, time-stamped logs that can be easily monitored and debugged in a production environment. It distinguishes between successful operations (`INFO`), files not found (`WARNING`), and critical failures (`ERROR`).

---

### 🔑 IAM Permissions

To run this script, the user or service account must have the following IAM permissions on the GCS bucket:

- `storage.objects.create`: Permission to create the new file at the destination path.
- `storage.objects.delete`: Permission to delete the original file from the source path.

For convenience, you can grant the **`roles/storage.objectAdmin`** role on the specific bucket. This pre-defined role provides all the necessary permissions for read, write, and deletion of objects, perfectly matching the script's requirements.

---

### ⚙️ Usage

1. Open the script and update the configuration variables (`YOUR_BUCKET_NAME`, `OBJECT_FILENAME_TO_MOVE`, etc.).
2. Save your changes.
3. Run the script from your terminal:

   ```
   python your_script_name.py
   ```

This script is a foundation for creating more complex data processing workflows. Consider integrating it into a **Cloud Function** to trigger it automatically when a new file is uploaded or using **Cloud Composer (Apache Airflow)** to orchestrate a series of data movement tasks.
