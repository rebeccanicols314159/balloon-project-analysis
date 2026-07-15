# balloon-project-analysis
A github repo linked to the Balloon project

## Aim

My aims when creating the project are the following:
- Test the impact which certain meteorological factors have on the landing location of a weather balloon.
- For the factors which had a significant impact, investigate:
    - the optimal condition for the optimal flight path
    - the optimal condition which reduce the risk of the balloon landing in the ocean
- Present this data in an understandable format to be usable by others

## Inputs

**All inputs are stored in [/input-files](/input-files)****
- Landing location predictions provided by @jackt77
    - AllPredictions.json
    - LandPredictions.json
    - SeaPredictions.json
- Weather data collected by myself (@rebeccanicols314159), and other files related to previous analysis of this (found in repo [rebeccanicols314159/auto-weather-data-test](https://github.com/rebeccanicols314159/auto-weather-data-test))
    - data.json
    - nearesettimes.py (updated to suit current program)

## Overall data

**The data described below is stored in [/overall-data](/overall-data/)**

This is data required for all or multiple parts of the other project. It contains the following files:
- TimeComparisons.json (contains a json dict of times available for predictions and the time of the closest weather data collectd to each.)
- TimesData.json (contains a json dict of the prediction times and data with weather data of times above)

## Multiple use scripts

**The data described below is stored in [/multiple-use-scripts](/multiple-use-scripts/)**

This is programs which either could have many uses when adapted, or may need to be used for the same job many times. It also contains scripts which have an output which fits into either of the above categories. The outputs are stored in **Overall data** (see above). This folder contains the following files:
- timeswithdata.py (Combines TimeComparisons.json with data.json and AllPredictions.json and stores them in one json file named TimesData.json)

## Testing correlation

### Aim
To test the impact which certain meteorlogical factors have on the landing location of a weather balloon.
