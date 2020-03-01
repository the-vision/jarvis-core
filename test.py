from rasa_nlu.model import Interpreter

CONFIDENCE_THRESHOLD = 0.5
FALLBACK_INTENT = 'N/A'

interpreter = Interpreter.load('./models/nlu/default/test')


def extract_structured_data(query):
    result = interpreter.parse(query)
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
        {
            'input': 'travel',
            'intent': 'travel',
            'entities': []
    ]

    for query in queries:
        data = extract_structured_data(query['input'])
        print (data)
        assert (data == query)
