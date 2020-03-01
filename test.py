import os
import requests

CONFIDENCE_THRESHOLD = 0.5
FALLBACK_INTENT = 'N/A'
PORT = os.environ.get('PORT', '5000')


def extract_structured_data(query, result):
    data = {
        'input': query,
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
        {
            'input': 'roll a die',
            'intent': 'dice',
            'entities': []
        },
        {
            'input': 'songs by linkin park',
            'intent': 'music',
            'entities': [
                {
                    'name': 'song',
                    'value': 'linkin park'
                }
            ]
        },
        {
            'input': 'show me a xkcd comic',
            'intent': 'xkcd',
            'entities': []
        },
        {
            'input': 'hey',
            'intent': 'hello',
            'entities': []
        },
    ]

    for query in queries:
        response = requests.get('http://0.0.0.0:' + PORT + '/parse?q=' + query['input'])
        data = extract_structured_data(query['input'], response.json())
        print (data)
        assert (data == query)
