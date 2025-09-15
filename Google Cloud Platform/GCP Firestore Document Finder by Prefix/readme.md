
### 📂 **GCP Firestore Document Finder**

A robust and efficient Python solution for querying documents in Google Cloud Firestore. This script is engineered to find and retrieve documents where the document ID starts with a specified prefix, leveraging an optimized server-side query for unparalleled performance and cost-effectiveness. 🚀

---

### 💻 **Why This Script is a Game-Changer**

In data-intensive applications, retrieving documents efficiently is a top priority. A common anti-pattern is to fetch an entire collection and filter locally, which is slow, expensive, and scales poorly. This script introduces a **best-in-class approach** by performing a  **server-side range query** . Instead of fetching unnecessary data, it asks Firestore to do the heavy lifting, retrieving  **only the documents that match your criteria** . This is not just a feature; it's a **fundamental optimization** that can save you a significant amount of money and compute time in production.

---

### **How It Works Under the Hood**

1. **Centralized Configuration** : All settings, from the project ID to the collection name, are managed via environment variables. This is the  **gold standard for production applications** , enabling seamless transitions between development, staging, and production environments without changing a single line of code.
2. **Singleton Client** : The script employs the singleton pattern to ensure only one instance of the Firestore client is created. This prevents redundant resource allocation and dramatically improves performance for repeated operations.
3. **The Querying Magic** : The core of the script lies in its server-side query. By ordering documents by their `__name__` (the document ID) and using `start_at` and `end_before`, the script creates a precise query range. For a prefix "123", the query retrieves all documents from ID "123" up to, but not including, "124". This technique makes the query  **fast, scalable, and cost-effective** .
4. **Structured Logging** : With Python's `logging` module, every step of the process is logged with timestamps and severity levels. This is vital for debugging, monitoring, and auditing in a production environment.

---

### **🚀 Getting Started**

#### **Prerequisites**

* **Python 3.x**
* **Google Cloud SDK** : Authenticate via `gcloud auth login` and set your project with `gcloud config set project [YOUR_PROJECT_ID]`.

#### **Setup**

1. **Create and activate a virtual environment** :

```
   python -m venv venv
   source venv/bin/activate
```

1. **Install the Firestore library** :

```
   pip install google-cloud-firestore
```

#### **Usage**

Set your environment variables and run the script from the terminal.

```
PROJECT_ID="your-project" \
DATABASE_ID="(default)" \
COLLECTION="your-collection" \
python GCP_firestore_doc_finder.py
```

---

### **🔑 IAM Permissions**

For the user or service account to run this script, it requires the following IAM permissions on the Firestore database:

* `datastore.documents.get`
* `datastore.documents.list`

These permissions are typically granted via the **`roles/datastore.viewer`** (read-only) or **`roles/datastore.user`** (read/write) predefined roles. For production, create a **custom IAM role** with the principle of least privilege in mind.
