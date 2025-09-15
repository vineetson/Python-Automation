## Requirement:

pip install google-cloud-storage

## How the Script Works:

#### 1. Imports and Client Initialization

The script starts by importing the necessary libraries: **`storage`** from the `google.cloud` package to interact with GCS, and **`logging`** for error handling. It then creates a `storage.Client()` object, which automatically handles authentication using your credentials.

#### 2. Main Logic with Error Handling

The core logic is wrapped in a `try...except` block. This is a **critical improvement** for production code.

- **`try` Block** : It attempts to execute the main code. The `storage_client.list_blobs(bucket_name)` method is called directly, which returns an iterator of `Blob` objects. It then uses a **list comprehension** to efficiently gather all object names into a list called `object_names`. Finally, it checks if the list is empty and prints a corresponding message.
- **`except` Block** : If any error occurs during the execution (e.g., the bucket doesn't exist, or there's a permission issue), the script catches the exception. Instead of just printing the error, it uses **`logging.error()`** to log the failure. This is a best practice for automation scripts as it allows for centralized error tracking.

#### 3. Execution Entry Point

The `if __name__ == '__main__':` block ensures that the `list_gcs_objects` function is called only when the script is executed directly, not when it's imported as a module into another script. You simply need to set the `bucket_name` variable and run the script.

## To list objects in a GCS bucket, the user or service account needs the **`storage.objects.list`** IAM permission.

Here are the recommended ways to grant this permission:

#### Predefined Roles

For the simplest approach, you can assign a **predefined IAM role** to the user or service account. The principle of least privilege dictates you should choose the role with the fewest permissions needed.

- **`roles/storage.objectViewer` (Storage Object Viewer)** : This is the most appropriate role for this task. It grants permissions to view object data and metadata, as well as to list objects. This role is ideal for read-only access to a bucket's contents.
- **`roles/storage.objectAdmin` (Storage Object Admin)** : This role has more permissions, including the ability to list, read, create, and delete objects. Only use this if the user needs to perform a wider range of actions.
- **`roles/storage.admin` (Storage Admin)** : This role grants full control over both buckets and objects. This is typically a powerful role that should be granted sparingly.

#### Custom Roles

If you want to follow the principle of least privilege strictly, you can create a **custom IAM role** that includes only the `storage.objects.list` permission. This is useful if the user should be able to see the files but not view their content or perform any other actions.

#### Where to Apply the Role

You should apply the chosen IAM role at the **bucket level** for the specific bucket you want the user to access. This ensures they can only list objects in that bucket, not in every bucket in the project.
