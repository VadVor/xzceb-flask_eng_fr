import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url(url)

englishText_test = 'Hello, how are you today?'
frenchText_test = 'Bonjour, comment vous êtes aujourd\'hui?'



def englishToFrench(englishText_test):
    translation = language_translator.translate(
    text = englishText_test,
    model_id='en-fr').get_result()
    json_string=json.dumps(translation, ensure_ascii=False)
    parse_string = json.loads(json_string)
    frenchText = parse_string['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText_test):
    translation = language_translator.translate(
    text = frenchText_test,
    model_id='fr-en').get_result()
    json_string=json.dumps(translation, ensure_ascii=False)
    parse_string = json.loads(json_string)
    englishText = parse_string['translations'][0]['translation']
    return englishText

print(englishToFrench(englishText_test))
print(frenchToEnglish(frenchText_test))
