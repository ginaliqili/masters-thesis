# masters-thesis
Data processing scripts for master's thesis. Execute in the following order:

## 1) Weather Processing
First, process the weather data from gridMET. See README.md under the weather_scripts directory
## 2) Health Processing
Second, process the mortality data from NCHS and VDH. See README.md under the health_scripts directory
## 3) Weather and Health Merging
Third, merge the weather and health datasets together by date and climate division. See README.md under the weather_health_scripts directory.
## 4) Append demographic data, day of week, and lag variables
Fourth, append other useful daily covariates to the final data setsuch as total population, day of week, julian day, time, heat lags, etc. See README.md under the demographic_scripts directory.