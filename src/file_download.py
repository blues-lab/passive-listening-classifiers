from io import UnsupportedOperation
import json
import os
import gdown
import zipfile

def extract_id_from_google_drive_share_link(drive_link):
    return drive_link

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
        
        if provider == "google":
            print(url, output)
            gdown.download(url, output, quiet=False)
        else:
            raise UnsupportedOperation()

        if file_type == "zip":
            with zipfile.ZipFile(output,"r") as zip_ref:
                zip_ref.extractall(relative_folder_loc)
        else:
            raise UnsupportedOperation()
