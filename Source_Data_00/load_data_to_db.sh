#!/bin/bash


sed 's/\r$//' GlobalLandTemperaturesByCity.csv > GlobalTemperaturesByCity.csv
sed 's/\r$//' GlobalLandTemperaturesByCountry.csv > GlobalTemperaturesByCountry.csv
sed 's/\r$//' GlobalLandTemperaturesByMajorCity.csv > GlobalTemperaturesByMajorCity.csv
sed 's/\r$//' GlobalLandTemperaturesByState.csv > GlobalTemperaturesByState.csv
sed 's/\r$//' GlobalTemperatures.csv > GlobalLandTemperatures.csv

./pgfutter --host $RDS_HOSTNAME --port "5432" --db "globaltemperatures" --user "postgres" --pw $RDS_PASSWORD csv GlobalTemperaturesByCity.csv
./pgfutter --host $RDS_HOSTNAME --port "5432" --db "globaltemperatures" --user "postgres" --pw $RDS_PASSWORD csv GlobalTemperaturesByCountry.csv
./pgfutter --host $RDS_HOSTNAME --port "5432" --db "globaltemperatures" --user "postgres" --pw $RDS_PASSWORD csv GlobalTemperaturesByMajorCity.csv
./pgfutter --host $RDS_HOSTNAME --port "5432" --db "globaltemperatures" --user "postgres" --pw $RDS_PASSWORD csv GlobalTemperaturesByState.csv
./pgfutter --host $RDS_HOSTNAME --port "5432" --db "globaltemperatures" --user "postgres" --pw $RDS_PASSWORD csv GlobalTemperatures.csv

rm *.csv
rm *.zip

exit 1