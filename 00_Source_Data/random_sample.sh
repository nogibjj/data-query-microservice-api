#!/bin/bash
shuf -n 500000 itineraries.csv  > itineraries_small.csv
sed  -i '1i legId,searchDate,flightDate,startingAirport,destinationAirport,fareBasisCode,travelDuration,elapsedDays,isBasicEconomy,isRefundable,isNonStop,baseFare,totalFare,seatsRemaining,totalTravelDistance,segmentsDepartureTimeEpochSeconds,segmentsDepartureTimeRaw,segmentsArrivalTimeEpochSeconds,segmentsArrivalTimeRaw,segmentsArrivalAirportCode,segmentsDepartureAirportCode,segmentsAirlineName,segmentsAirlineCode,segmentsEquipmentDescription,segmentsDurationInSeconds,segmentsDistance,segmentsCabinCode' itineraries_small.csv

# ./pgfutter --host $RDS_HOSTNAME --port "5432" --db "flightprices" --user "postgres" --pw $RDS_PASSWORD csv 00_Source_Data/itineraries_small.csv

./pgfutter --host $RDS_GLOBAL_TEMP_HOSTNAME --port "5432" --db "globaltemperatures" --user "postgres" --pw $RDS_PASSWORD csv 00_Source_Data/GlobalLandTemperaturesByCity.csv

exit 1