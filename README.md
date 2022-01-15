# randomnum
Simple API to generate random UUID and timestamp
[![DUB](https://img.shields.io/dub/l/vibe-d.svg)]()
[![PyPI](https://img.shields.io/pypi/v/nine.svg)]()

# Running the API
#### A step-by-step guide

- This is a guide to how to use the code provided on this [repository](https://github.com/MikeSoft007/randomnum) to genarate random charactes in UUID and time stamp:

## INSTALLATION AND GUIDE

1. clone/download the project into the directory of your choice


#### Using a virtual environment

2. Create a virtual environment

          $ python3 -m venv venv
          $ . venv/bin/activate

1. Install the project's dependancies

        $ pip install requirements.txt           


1. Configure your flask path

        $ export FLASK_APP=run.py


1. Launch application

        $ flask run            

1. Head to https://localhost:5000

- Assuming that you are doing your development on a localhost, you have to expose your application living in the webroot of your localhost to the internet via a application like [heroku](https://dashboard.heroku.com/).

- This application has been developed on an Ubuntu 21.04LTS. Courtesy of Heroku, the publicly accessible url is: https://mikeapi.herokuapp.com/ (instead of http://localhost) which is referenced in the code as well. 

- The webhook or callback to this application therefore becomes: 
https://mikeapi.herokuapp.com/. 

- Finally, this application works with a connection to a mongodb database to display all generated UUID sorted from the latest to oldest.
```


- Written with <3 by mekpenyong2@gmail.com
