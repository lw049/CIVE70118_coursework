# Dataset 1 (D1)

This dataset has 10,000 observations of work trips made by different individuals. This is effectively like a daily trip file from a travel demand survey. Columns include:

| VARIABLE NAME | NOTES | EXAMPLE |
| :--- | :--- | :--- |
| `HHID` | Unique household ID (sample only 1 person per household) | 1 |
| `ORIGIN_OF_TRIP` | Origin of trip (1 to 10 zones) | 5 |
| `DESTINATION_OF_TRIP` | Destination of trip (1 to 10 zones) | 4 |
| `TT_WALK` | Travel time for walk in min. (10-60 min.) | 53 |
| `WALKABILITY_INDEX` | Walkability index, the higher the value the more attractive the environment for walking (1-100) | 5 |
| `TT_CYCLE` | Travel time for cycle in min. (10-60 min.) | 25 |
| `BIKEABILITY_INDEX` | Bikeability index, the higher the value the more attractive the environment for cycling (1-100) | 94 |
| `TT_PT` | Travel time for public transport in min. (10-60 min.) | 24 |
| `FARE_PT` | Fare for public transport in GBP (1-7 GBP) | 5 |
| `WT_PT` | Waiting time for public transport in min. (2-20 min.) | 15 |
| `AT_PT` | Access time for public transport in min. (5-30 min.) | 9 |
| `AC_PT` | Access Cost for public transport in GBP (0-5 GBP) | 1 |
| `TT_CAR` | Travel time for car in min (10-60 min.) | 56 |
| `FC_CAR` | Fuel cost for car in GBP (1-3 GBP) | 3 |
| `PC_CAR` | Parking cost for car in GBP (1-8 GBP) | 6 |
| `CC_CAR` | Congestion charge for car in GBP (2-10 GBP) | 6 |
| `INCOME` | Income in 10k GBP (10-100k GBP) | 88 |
| `GENDER` | Gender (Male=1, Female=2) | 2 |
| `AGE` | Age (18-70) | 42 |
| `CAR_OWNERSHIP` | Household owning a car (Yes=1, No=0) | 0 |
| `CHOSEN_MODE` | Mode choice of the trip (Walk=1, Bike=2, PT=3, Car=4) | 2 |
| `AV_WALK` | Availability of walk | 1 |
| `AV_CYCLE` | Availability of cycle | 1 |
| `AV_PT` | Availability of public transport | 1 |
| `AV_CAR` | Availability of car | 1 |