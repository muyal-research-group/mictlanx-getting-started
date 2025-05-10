# MictlanX Basics

A basic example of using the `mictlanx` library to interact with a distributed file storage system in asynchronous mode. This project demonstrates setting up a client, uploading files, and managing configurations via environment variables and Docker Compose.

---

## 📁 Project Structure

```
.
├── README.md
├── assets/                    # Optional static assets
├── log/                       # Log output directory
│   ├── client-0
│   └── client-0.error
├── mictlanx.yml              # MictlanX configuration file
├── mictlanxbasics/
│   ├── __init__.py
│   └── main.py               # Main async example script
├── poetry.lock
├── pyproject.toml
├── requirements.txt
├── run_mictlanx.sh          # Script to launch containers with Docker Compose
├── source/                  # Source media to upload
│   ├── 01.gif
│   ├── 02.jpg
│   └── 03.jpg
└── tests/
    └── __init__.py
```

---

## 🚀 Getting Started

### 🐳 Docker Compose Deployment

Use the provided `run_mictlanx.sh` script to launch the required MictlanX services using Docker Compose:

### Run

```bash
./run_mictlanx.sh
```

This script will initialize all necessary containers as defined in the `mictlanx.yml` configuration file.

Make sure you have Docker and Docker Compose installed and available in your shell.

---
## Install Dependencies

This project uses [Poetry](https://python-poetry.org/) for dependency and environment management. Follow these steps to install everything cleanly using the official `poetry-plugin-shell`.

#### ✅ Step-by-step Setup

1. **Install Poetry (using the official installer)**

   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

   Make sure Poetry is available in your shell:

   ```bash
   poetry --version
   ```

2. **Install the Poetry Shell Plugin**

   Poetry 2.0+ requires a plugin for `poetry shell` support:

   ```bash
   poetry self add poetry-plugin-shell
   ```


4. **Create and activate the virtual environment**

   From your project directory:

   ```bash
   poetry shell
   ```

   This activates the virtual environment (creating it if needed).

5. **Install project dependencies**

   Once inside the virtual environment:

   ```bash
   poetry lock && poetry install
   ```

---

### 🔍 Optional Checks

- Check which environment Poetry is using:

  ```bash
  poetry env info
  ```

- List all environments Poetry knows about:

  ```bash
  poetry env list
  ```




---

### Setup Environment

Create a `.env` file or set the environment variables externally. You can also use a custom `.env` file path via the `ENV_FILE_PATH` environment variable.

Example `.env`:

```env
MICTLANX_CLIENT_ID=client-0
MICTLANX_DEBUG=1
MICTLANX_MAX_WORKERS=2
MICTLANX_LOG_PATH=./log
SOURCE_PATH=./source
MICTLANX_PROTOCOL=https
MICTLANX_ROUTERS=mictlanx-router-0:localhost:60666
```

---

### Running the Example

Make sure your MictlanX environment is up and running (see Docker section below), then run the main script:

```bash
python3  mictlanxbasics.main
```


---

## 🔍 Viewing Uploaded Files and Metadata

Once you've uploaded files using the example script, you can **inspect and retrieve them** using the MictlanX HTTP API.

The following endpoints are available:

### ✅ Retrieve the Merged File

```http
GET /api/v4/buckets/<bucket_id>/<key>/merge
```

- This endpoint returns the full merged object (i.e., the complete file as it was originally uploaded).
- In your example code, these values are:

  - `bucket_id`: `"cubeton"`
  - `key`: `"millave03"`

👉 Example:

```bash
curl -O https://localhost:60666/api/v4/buckets/cubeton/millave03/merge
```

Make sure to replace `<router_host>` and `<port>` with the actual address of the router (e.g., `localhost:60666`).

---

### 🧾 Inspect Chunk Metadata

```http
GET /api/v4/buckets/<bucket_id>/metadata/<key>/chunks
```

- This endpoint returns the metadata of each chunk that was uploaded as part of the object.
- Useful for debugging or verifying chunked upload integrity.

👉 Example:

```bash
curl https://localhost:60666/api/v4/buckets/cubeton/metadata/millave03/chunks
```

You’ll get a JSON response containing information about each stored chunk (e.g., size, tag, storage node).

---

### 📌 Notes

- These values (`bucket_id` and `key`) are defined statically in the code:
  
  ```python
  bucket_id = "cubeton"
  key = "millave03"
  ```

- You can modify them in the script to upload and retrieve different objects.

---


## 📦 Features Demonstrated

- Asynchronous interaction with MictlanX via `AsyncClient`
- Dynamic environment configuration loading via `dotenv`
- Chunked file uploads to a bucket
- Tag metadata association per file
- Basic validation with assertion

---


## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## 👤 Author

Developed by Ignacio Castillo. Contributions and suggestions are welcome.