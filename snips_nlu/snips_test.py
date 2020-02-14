from snips_nlu import SnipsNLUEngine

engine = SnipsNLUEngine.from_path("snips_trained_model")

result = engine.parse("what is the computer system")

print(result)
if result['intent']['intentName']:
    if result.get('slots'):
        print(result['slots'][0].get('rawValue'))

