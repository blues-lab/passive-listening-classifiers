from io import UnsupportedOperation
import json
import os
import gdown
import zipfile
import click
import requests

def extract_id_from_google_drive_share_link(drive_link):
    return drive_link


def download_file(url, local_filename):
#     local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename

"""
Example model json format
"models": [
{
    "name": "general",
    "relative_folder_location": "",
    "download_url": "<download_url/id>",
    "provider": "google", 
    "file_type": "zip"
}]

"""
with open("src/models.json") as model_file:
    models_dict = json.load(model_file)["models"]
    for model_download in models_dict:
        relative_folder_loc = model_download["relative_folder_location"]
        name = model_download["name"]
        file_type = model_download["file_type"]
        provider = model_download["provider"]
        print(f"Download model for {name} at {relative_folder_loc} with {provider}")

        if not os.path.exists(relative_folder_loc):
            os.mkdir(relative_folder_loc)
        
        url = model_download["download_url"]
        output = os.path.join(relative_folder_loc, f'{name}_model_files.{file_type}')

        print(url, output)
        if provider == "google":
            print(url, output)
            gdown.download(url, output, quiet=False)
        if provider == "http" or provider == "https":
            download_file(url, output)
        else:
            raise UnsupportedOperation()

        if file_type == "zip":
            with zipfile.ZipFile(output,"r") as zip_ref:
                zip_ref.extractall(relative_folder_loc)
        else:
            raise UnsupportedOperation()
