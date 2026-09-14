import os
from pathlib import Path
from dotenv import load_dotenv
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
import pandas as pd
from google_drive_client import get_drive_client

load_dotenv()

def get_datafile(service): 
    folder_id = os.environ["GOOGLE_DRIVE_DATA_FOLDER_ID"]
    file_name = os.environ["GOOGLE_DRIVE_DATA_FILE_NAME"]
    query = (
            f"name = '{file_name}' "
            f"and '{folder_id}' in parents "
            "and trashed = false"
    )

    results = (
            service.files()
            .list(
                q=query,
                pageSize=10,
                fields="files(id, name, capabilities(canDownload))",
                )
            .execute()
    )

    files = results.get("files", [])

    if not files:
        raise FileNotFoundError(file_name)

    return files[0]

def download_csv_data(service, local_path):
    data_file = get_datafile(service)

    if not data_file["capabilities"]["canDownload"]:
        raise PermissionError(
            f"File cannot be downloaded: {data_file['name']}"
        )

    request = service.files().get_media(
        fileId=data_file["id"]
    )

    with open(local_path, "wb") as file:
        downloader = MediaIoBaseDownload(file, request)

        done = False
        while not done:
            _, done = downloader.next_chunk()

def load_csv_data(local_path: str) -> pd.DataFrame:
    return pd.read_csv(local_path)

if __name__ == "__main__":
    try:
        service = get_drive_client()

        data_file = get_datafile(service)
        
        print(f"Found file: {data_file['name']}")
        #local_path = Path(__file__).resolve().parent.parent / "data" / "DSI_kickstarterscrape_dataset.csv"
        local_path = (
                Path(__file__).resolve().parent.parent 
                / "data"
                / "Raw-data"
                / "DSI_kickstarterscrape_dataset.csv"
                )

        local_path.parent.mkdir(parents=True, exist_ok=True)
        download_csv_data(service, local_path)
        print(f"Downloaded file to: {local_path}")


    except HttpError as error:
        print(f"An error occurred: {error}")
