# Running Streamlit Covid19 docker built-in Stand-alone examples
**Streamlit Project docs:** https://streamlit.io/docs/

<p align="center">
  <img src="../img/dashboard.png" width="750" title="Example dashboard App">
</p>

## Running Covid19 ETL complete project
```sh
Docker-compuse
cd streamlit-covid
docker-compuse up 
```
Go to
` http://localhost:8501

## Editing the APP 

streamlite app uses a python code in folder `src/app.py`

## Stand-alon testing

For testing purpose the project can obtain its data from static files (Provided with the repository) one for each info : Confirmed, Dead, Recovered in a time series structure, this files are on `src/time_series_covid19_<type>.csv`

## Database Connection

For Database connection follow ths [Streamlit Documetation](https://docs.streamlit.io/knowledge-base/tutorials/databases/mysql)

This repository has included a demo connection on `.streamlit/secrets.toml`

## Dependencies 
`requirements.txt`
```
jsonschema==3.2
vega-datasets
mysql-connector-python
```

# Dashboard

#### Global Resume

<p align="center">
  <img src="../img/resume.png" width="750" title="Example dashboard App">
</p>

#### Wold Map

<p align="center">
  <img src="../img/worldmap.png" width="750" title="Example dashboard App">
</p>

#### Global Trend of cases

<p align="center">
  <img src="../img/globaltrend.png" width="750" title="Example dashboard App">
</p>

#### Top 5 Countries with comfirmed cases
<p align="center">
  <img src="../img/top5.png" width="750" title="Example dashboard App">
</p>

#### Raw Data

<p align="center">
  <img src="../img/rawdata.png" width="750" title="Example dashboard App">
</p>

#### Filter for country search in data an world map

<p align="center">
  <img src="../img/filter1.png" width="750" title="Example dashboard App">
</p>

<p align="center">
  <img src="../img/filter.png" width="750" title="Example dashboard App">
</p>

<p align="center">
  <img src="../img/zoommap.png" width="750" title="Example dashboard App">
</p>
