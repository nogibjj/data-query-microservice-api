#!/bin/bash


./pgfutter --host $RDS_HOSTNAME --port "5432" --db "globaltemperatures" --user "postgres" --pw $RDS_PASSWORD csv GlobalLandTemperaturesByCity.csv
./pgfutter --host $RDS_HOSTNAME --port "5432" --db "globaltemperatures" --user "postgres" --pw $RDS_PASSWORD csv GlobalLandTemperaturesByCountry.csv
./pgfutter --host $RDS_HOSTNAME --port "5432" --db "globaltemperatures" --user "postgres" --pw $RDS_PASSWORD csv GlobalLandTemperaturesByMajorCity.csv
./pgfutter --host $RDS_HOSTNAME --port "5432" --db "globaltemperatures" --user "postgres" --pw $RDS_PASSWORD csv GlobalLandTemperaturesByState.csv
./pgfutter --host $RDS_HOSTNAME --port "5432" --db "globaltemperatures" --user "postgres" --pw $RDS_PASSWORD csv GlobalTemperatures.csv

exit 1