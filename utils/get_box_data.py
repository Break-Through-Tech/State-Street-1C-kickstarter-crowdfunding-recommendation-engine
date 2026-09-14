import os
from dotenv import load_dotenv
from box_sdk_gen import BoxClient
import pandas as pd

load_dotenv()

def get_datafile(client: BoxClient): # expects BoxClient
    folder_id = os.environ["BOX_DATA_FOLDER_ID"]
    file_name = os.environ["BOX_DATA_FILE_NAME"]
    items = client.folders.get_folder_items(folder_id).items
    matching_files = [
            item for item in items
            if item.name == file_name
    ]
    if not matching_files:
        raise FileNotFoundError(file_name)
    return matching_files[0]

def download_csv_data(client: BoxClient, local_path: str):
    data_file = get_datafile(client)
    file_stream = client.downloads.download_file(data_file.id) # https://github.com/box/box-python-sdk/blob/main/docs/downloads.md#download-file
    with open(local_path, "wb") as file:
        file.write(file_stream.read())

def load_csv_data(local_path: str) -> pd.DataFrame:
    return pd.read_csv(local_path)
