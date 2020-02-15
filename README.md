# jarvis-core

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
