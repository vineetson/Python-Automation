# 🐍 Python Automation Hub

Welcome to the **Python Automation Hub** ! This repository is your go-to source for a growing collection of Python scripts designed to simplify, optimize, and automate tasks across various domains—from cloud infrastructure and DevOps to everyday workflows.

---

### ✨ Features

Our scripts are crafted to be simple, scalable, and efficient, helping you solve real-life problems one line of code at a time. Key features include:

- **🔹 Automate Repetitive Workflows** : Say goodbye to manual, tedious tasks.
- **☁️ Cloud Automation** : Simplify infrastructure management on platforms like **GCP** , **AWS** , and more.
- **🔧 DevOps Utilities** : Streamline your CI/CD pipelines, scripting, and infrastructure setup.
- **⚡ Real-World Problem-Solving** : Practical solutions for real-world challenges.

---

### 🚀 Getting Started

### 📂 Repository Structure

The repository is organized by GCP service, with each folder containing a specific automation script and its corresponding `readme.md` file.

```
.
├── README.md                  # The main README file you are currently reading.
│
└── Google Cloud Platform/
    ├── Cloud Storage/
    │   ├── list_objects.py    # Lists all objects in a GCS bucket.
    │   └── readme.md
    │
    ├── GCP Firestore Document Finder by Prefix/
    │   ├── GCP_firestore_doc_finder.py # Efficiently queries Firestore documents by ID prefix.
    │   └── readme.md
    │
    ├── GCS Move by date range/
    │   ├── gcs_move_by_date.py # Moves GCS objects based on a specific date range.
    │   └── readme.md
    │
    └── GCS Move file within a bucket/
        ├── gcs_folder_move.py # Moves a single GCS object from one folder to another.
        └── readme.md
```

---

### 📝 Scripts and Documentation

- **[Cloud Storage](https://github.com/vineetson/Python-Automation/tree/master/Google%20Cloud%20Platform/Cloud%20Storage)**
  - **list_objects.py** : A simple, yet robust script to list all files in a specified GCS bucket.
- **[GCP Firestore Document Finder by Prefix](https://github.com/vineetson/Python-Automation/tree/master/Google%20Cloud%20Platform/GCP%20Firestore%20Document%20Finder%20by%20Prefix)**
  - **GCP_firestore_doc_finder.py** : An optimized script that efficiently queries Firestore documents by ID prefix using a server-side range query, which is crucial for cost-effective operations on large datasets.
- **[GCS Move by date range](https://github.com/vineetson/Python-Automation/tree/master/Google%20Cloud%20Platform/GCS%20Move%20by%20date%20range)**
  - **gcs_move_by_date.py** : A script designed for data lifecycle management, allowing you to move objects to a different location based on their creation date.
- **[GCS Move file within a bucket](https://github.com/vineetson/Python-Automation/tree/master/Google%20Cloud%20Platform/GCS%20Move%20file%20within%20a%20bucket)**
  - **gcs_folder_move.py** : An atomic and reliable script to move a single file from a source folder to a destination folder within the same bucket.

Getting up and running with any script in this repository is a breeze.

1. **Clone the Repository** :

```
   git clone https://github.com/vineetson/Python-Automation.git
   cd Python-Automation
```

1. **Set Up Your Environment** : Create a virtual environment to manage dependencies for each script.

```
   python3 -m venv venv
   # Activate on Linux / macOS
   source venv/bin/activate
   # Activate on Windows
   venv\Scripts\activate
```

1. **Install Dependencies** : Navigate to the specific script's directory and install its dependencies from the `requirements.txt` file (if one exists).

```
   pip install -r requirements.txt
```

1. **Run an Automation Script** : Execute the script with Python. Each script's local `README.md` will provide specific usage details.

```
   python script_name.py
```

---

### 🤝 Contributing

We welcome contributions! Your ideas and code can help grow this hub and make life easier for others. Here's how you can contribute:

1. **Fork the repository** .
2. **Create a new branch** : `git checkout -b feature-name`.
3. **Commit your changes** : `git commit -m 'feat: Add new automation script for X'`.
4. **Push to your branch** : `git push origin feature-name`.
5. **Open a Pull Request** and describe your changes. We'll review it and merge it once it's ready. 🎉

---

### 📌 Planned Automations

We have an exciting roadmap of automations planned. Feel free to open an Issue and suggest new ideas!

- **☁️ Cloud Cleanup** : Scripts to automatically identify and remove unused cloud resources to cut costs.
- **📊 Cloud Cost Optimization** : Tools to track and provide insights into cloud spending.
- **🔄 Log Rotation & Archival** : Automate the handling and archival of system/application logs.
- **⚡ CI/CD Pipeline Triggers** : Scripts to automate deployments and pipeline triggers.
- **🔐 Security Checks** : Basic infrastructure security scans and compliance checks.
- **🧹 Resource Health Monitoring** : Simple monitoring and alerting scripts for cloud resources.

---

### 🌍 About

Built with ❤️ and **Python** to simplify complex tasks and make life easier—one automation at a time.
