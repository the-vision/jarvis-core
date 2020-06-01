# jarvis-core

The core of Just A Rather Very Intelligent System!

[![Build Status](https://travis-ci.org/the-vision/jarvis-core.svg?branch=master)](https://travis-ci.org/the-vision/jarvis-core)

![Python](https://img.shields.io/badge/python-3.7-blue.svg)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/the-vision/jarvis-core/master/LICENSE)
[![first-timers-only](https://img.shields.io/badge/first--timers--only-friendly-blue.svg?style=flat-square)](https://www.firsttimersonly.com/)

## Setup
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run
```
python -m rasa_nlu.train -c config.yml --data data/nlu.md --verbose
python -m rasa_nlu.server -c config.yml --path models/nlu --response_log models --verbose
curl 'http://localhost:5000/status'
curl 'http://localhost:5000/version'
curl 'http://localhost:5000/parse?q=roll+a+die'
curl 'http://localhost:5000/parse?q=songs+by+linkin+park'
```

## Development / Testing
1. Make changes in `data/nlu.md`.
1. Run `python -m rasa_nlu.train -c config.yml --data data/nlu.md` to train a new model, which will appear under the `models/nlu/default/` folder.
1. Change line 6 of `test.py` to the new folder created above, e.g. `interpreter = Interpreter.load('./models/nlu/default/model_20200526-231423')`
1. Run `python test.py`

You can also hit the blue Open in Gitpod button below to launch a ready-to-code environment (a VS Code-like interface in the browser with the dependencies pre-installed and the web server running).

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/the-vision/jarvis-core/)

Before contributing to this project do check [CONTRIBUTING.md](https://github.com/the-vision/jarvis-core/blob/master/CONTRIBUTING.md) file
