# Streamlit Covid19 Dashboard
Streamlit Project docs: https://streamlit.io/docs/

<p align="center">
  <img src="img/dashboard.png" width="750" title="Example dashboard App">
</p>

Get the proyect 
## Clone
```sh
git clone https://github.com/bhlr/streamlit-covid.git
```
*Page: https://github.com/bhlr/streamlit-covid

## Running Streamlit Covid19 docker built-in examples
### Docker-compuse
```sh
cd streamlit-covid.git
docker-compuse up 
```
#### Go to 
` http://localhost:8501


## Running Streamlit docker built-in examples
You can learn how to use streamlit by exploring 3 scripts (packed inside the docker image):

`docker run -it -p 8501:8501 tomerlevi/streamlit-docker /examples/intro.py` <br/>
`docker run -it -p 8501:8501 tomerlevi/streamlit-docker /examples/plot_example.py` <br/>
`docker run -it -p 8501:8501 tomerlevi/streamlit-docker /examples/uber_nyc_data_explorer.py` <br/>


## Running your own streamlit script
`docker run -it -p 8501:8501 -v <local-scripts-folder>:/app tomerlevi/streamlit <relative-path-to-a-script>`

Example:
`docker run -it -p 8501:8501 -v ~/workspace/streamlit-scripts:/app tomerlevi/streamlit src/main.py`

Once streamlit is running, open your browser and navigate to: http://localhost:8501

*NOTE*: you can open the script you passed (`<relative-path-to-a-script>`) in your favorite text editor and edit it, streamlit will pickup all changes once you refresh your browser tab.


## Build 
Clone the repo:
`git clone git@github.com:MrTomerLevi/streamlit-docker.git`

Change dir into the project:
`cd streamlit-docker`

*Optional:*  You can add your required PyPi packages to the `requirements.txt`

Run docker build:
`docker build -t tomerlevi/streamlit-docker .`



