from rasa_nlu.model import Interpreter

import json

DEBUG = True
CONFIDENCE_THRESHOLD = 0.5
FALLBACK_INTENT = 'N/A'

interpreter = Interpreter.load('./models/nlu/default/model_20200227-224723')


def extract_structured_data(interpreter, query):
    result = interpreter.parse(query)
    if DEBUG:
        print(json.dumps(result, indent=2))
    data = {
        'text': query,
        'intent': FALLBACK_INTENT,
        'entities': []
    }
    if result['intent']['confidence'] > CONFIDENCE_THRESHOLD:
        data['intent'] = result['intent']['name']
    for entity in result['entities']:
        if entity['confidence'] > CONFIDENCE_THRESHOLD:
            data['entities'].append({
                'name': entity['entity'],
                'value': entity['value']
            })
    return data

if '__main__' == __name__:
    queries = [
        'roll a die',
        'songs by linkin park',
        'show me a xkcd comic',
        'hello'
    ]

    print('Extracting intents from queries...')
    for query in queries:
        data = extract_structured_data(interpreter, query)
        print(data)
