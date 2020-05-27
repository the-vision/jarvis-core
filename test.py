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
            'input': 'What\'s the time?',
            'intent': 'time',
            'entities': []    	    
        },
        {
            'input': 'vietnam travel options',
            'intent': 'travel',
            'entities': [
                {
                    'name': 'destination',
                    'value': 'vietnam'
                }
            ]
        },
        {
            'input': 'show me a quote',
            'intent': 'quote',
            'entities': []
        },
        {
            'input': 'thank you',
            'intent': 'thanks',
            'entities': []
        },
        {
            'input': 'flip a coin',
            'intent': 'coin',
            'entities': []
        },
        {
            'input': 'translate hello',
            'intent': 'translate',
            'entities': [
                {
                    'name': 'text',
                    'value': 'hello'
                }
            ]
        },
        {
            'input': 'tell me a fact',
            'intent': 'fact',
            'entities': []
        },
        {
            'input': 'goodbye',
            'intent': 'bye',
            'entities': []
        },
        {
            'input': 'batman movie',
            'intent': 'movie',
            'entities': [
                {
                    'name': 'movie',
                    'value': 'batman'
                }
            ]
        },
        {
            'input': 'news',
            'intent': 'news',
            'entities': []
        },
        {
            'input': 'random joke',
            'intent': 'joke',
            'entities': []
        },
        {
            'input': '100 USD to INR',
            'intent': 'currency',
            'entities': [
                {
                    'name': 'amount',
                    'value': '100'
                },
                {
                    'name': 'from_currency',
                    'value': 'USD'
                },
                {
                    'name': 'to_currency',
                    'value': 'INR'
                }
            ]
        },
        {
           'input': 'define space',
           'intent': 'dictionary',
           'entities': [
                {
                    'name': 'word',
                    'value': 'space'
                }
            ]
        },
        {
            'input': 'define server',
            'intent': 'dictionary',
            'entities': [
                {
                    'name': 'word',
                    'value': 'server'
                }
            ]
        },
        {
            'input': 'find server in wikipedia',
            'intent': 'wiki',
            'entities': [
                {
                    'name': 'wiki',
                    'value': 'server'
                }
            ]
        },
        {
            'input': 'show memes',
            'intent': 'meme',
            'entities': []
        },
        {
            'input': 'help me',
            'intent': 'help',
            'entities': []
        },
        {
            'input': 'detective conan anime',
            'intent': 'anime',
            'entities': [
                {
                    'name': 'anime',
                    'value': 'detective conan'
                }
            ]
        },
    ]

    for query in queries:
        data = extract_structured_data(query['input'])
        print (data)
        assert (data == query)
