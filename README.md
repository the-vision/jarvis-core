# jarvis-core

## Setup
```
python3 -m venv venv
source venv/bin/activate
pip install 'rasa_nlu[tensorflow]'
pip install -r requirements.txt
```

## Run
```
python -m rasa_nlu.train -c nlu_config.yml --data nlu.md --verbose
python jarvis.py
python -m rasa_nlu.server -c nlu_config.yml --path models/nlu --response_log models --verbose
curl 'http://localhost:5000/status'
curl 'http://localhost:5000/version'
curl 'http://localhost:5000/parse?q=hello'
curl 'http://localhost:5000/parse?q=songs+by+linkin+park'
```
