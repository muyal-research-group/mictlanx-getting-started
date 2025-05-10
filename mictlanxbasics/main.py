"""
Basic async client example using MictlanX to upload a file.

This script:
- Loads configuration from environment variables (optionally from an .env file)
- Initializes an AsyncClient for MictlanX
- Uploads a file to a distributed bucket using chunked upload
"""

from mictlanx.v4.asyncx import AsyncClient
from mictlanx.utils.index import Utils as UtilsX
from dotenv import load_dotenv
import asyncio
import os

# Load environment variables from a .env file if provided
ENV_FILE_PATH = os.environ.get("ENV_FILE_PATH", ".env")
if ENV_FILE_PATH != -1:
    load_dotenv(ENV_FILE_PATH)

# Load configuration values from environment
MICTLANX_CLIENT_ID   = os.environ.get("MICTLANX_CLIENT_ID", "client-0")
MICTLANX_DEBUG       = bool(int(os.environ.get("MICTLANX_DEBUG", "1")))
MICTLANX_MAX_WORKERS = int(os.environ.get("MICTLANX_MAX_WORKERS", "2"))
MICTLANX_LOG_PATH    = os.environ.get("MICTLANX_LOG_PATH", "./log")
SOURCE_PATH          = os.environ.get("SOURCE_PATH", "/home/nacho/Programming/Python/examples/mictlanx-basics/source")
MICTLANX_PROTOCOL    = os.environ.get("MICTLANX_PROTOCOL", "https")
MICTLANX_ROUTERS_STR = os.environ.get("MICTLANX_ROUTERS", "mictlanx-router-0:localhost:60666")

# Parse the routers from the environment string
routers = list(UtilsX.routers_from_str(routers_str=MICTLANX_ROUTERS_STR, protocol=MICTLANX_PROTOCOL))

# Create an asynchronous MictlanX client
client = AsyncClient(
    client_id      = MICTLANX_CLIENT_ID,
    routers        = routers,
    debug          = MICTLANX_DEBUG,
    max_workers    = MICTLANX_MAX_WORKERS,
    log_output_path= MICTLANX_LOG_PATH
)

async def main():
    """
    Main async function to upload a file to a MictlanX bucket using chunked upload.

    The function uploads one image file and prints the response status.
    """
    path1     = "{}/01.jpg".format(SOURCE_PATH)
    path2     = "{}/02.jpg".format(SOURCE_PATH)  # Unused in this example, but shows how to prep multiple files
    bucket_id = "cubeton"
    key       = "millave04"

    # Upload a file with metadata tags and chunk size
    put_response = await client.put_file(
        bucket_id=bucket_id,
        key=key,
        path=path1,
        tags={
            "test": "01",
            "more_fields": "kjksjkhdfdjhk",
            "path": path1
        },
        chunk_size="10kb"
    )

    print(put_response)
    assert put_response.is_ok

    # Example of uploading raw bytes instead of a file
    """
    put_response = await client.put(
        bucket_id=bucket_id,
        key=key,
        value=b"HOLAAAAAAA IN BYTES"
    )
    """

# Entry point of the script
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
