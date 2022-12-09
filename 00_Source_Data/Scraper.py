from kaggle.api.kaggle_api_extended import KaggleApi
from zipfile import ZipFile
import pandas
import random
import subprocess

api = KaggleApi()
api.authenticate()

# api.dataset_download_files('dilwong/flightprices')
# api.dataset_download_files('berkeleyearth/climate-change-earth-surface-temperature-data')

with ZipFile("climate-change-earth-surface-temperature-data.zip", 'r') as zipfile_object:
    zipfile_object.extractall()

# exit_code = subprocess.call('./random_sample.sh')


# ./pgfutter --host $RDS_HOSTNAME --port "5432" --db "flightprices" --user "postgres" --pw $RDS_PASSWORD csv 00_Source_Data/itineraries_small.csv




# url = "http://stats.oecd.org/SDMX-JSON/data/<dataset identifier>/<filter expression>/<agency name>[ ?<additional parameters>]"

# response = requests.get(url)