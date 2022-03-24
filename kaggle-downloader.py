from kaggle.api.kaggle_api_extended import KaggleApi
import json
import zipfile
import os
api = KaggleApi()
api.authenticate()

f = open("file_names.json")
file_names = json.load(f)

counter = 1
for file_name in file_names:
    print(f"{counter}/{len(file_names)}")
    if(file_name.startswith("test/")):
        api.competition_download_file('siim-covid19-detection', file_name, path='./dataset/test/')
    elif(file_name.startswith("train/")):
        api.competition_download_file('siim-covid19-detection', file_name, path='./dataset/train/')
    else:
        api.competition_download_file('siim-covid19-detection', file_name, path='./dataset/')
    counter += 1

for root, dirs, files in os.walk("./dataset", topdown=False):
   for name in files:
        file_name = os.path.join(root, name)
        if(file_name.endswith(".zip")):
            print(file_name)
            with zipfile.ZipFile(file_name,"r") as zip_ref:
                zip_ref.extractall(os.path.dirname(file_name))
            os.remove(file_name)
        