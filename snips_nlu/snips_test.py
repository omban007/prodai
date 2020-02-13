from snips_nlu import SnipsNLUEngine

engine = SnipsNLUEngine.from_path("snips_trained_model")

result = engine.parse("what about star")

if result['intent']['intentName']:
    print(result['slots'][0].get('rawValue'))
print(result)
