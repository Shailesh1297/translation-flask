from transformers import pipeline

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-hi")

def translate(data):
    return translator(data,src_lang="eng", tgt_lang="hin")

def translate_json(json_object, src='eng', dest='hin'):
    if isinstance(json_object, str):
        return translate(json_object)
    elif isinstance(json_object, list):
        return [translate_json(item, src=src, dest=dest) for item in json_object]
    elif isinstance(json_object, dict):
        new_json_object = {}
        for key, value in json_object.items():
            new_json_object[key] = translate_json(value, src=src, dest=dest)
        return new_json_object
    else:
        return json_object