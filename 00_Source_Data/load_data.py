# pylint: disable-msg=E0611 
# from kaggle.api.kaggle_api_extended import KaggleApi
# from zipfile import ZipFile
# import pandas
# import random
# import subprocess

# api = KaggleApi()
# api.authenticate()

# api.dataset_download_files('dilwong/flightprices')
# api.dataset_download_files('berkeleyearth/climate-change-earth-surface-temperature-data')

# with ZipFile("climate-change-earth-surface-temperature-data.zip", 'r') as zipfile_object:
#     zipfile_object.extractall()

# exit_code = subprocess.call('./load_data_to_db.sh')


# url = "http://stats.oecd.org/SDMX-JSON/data/<dataset identifier>/<filter expression>/<agency name>[ ?<additional parameters>]"

# response = requests.get(url)