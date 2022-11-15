"""Written by trls250s for IBM Courser"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'apikey'), 'r', encoding="utf8") as file:
    apikey = file.read()

with open(os.path.join(__location__, 'url'), "r", encoding="utf8") as f:
    url = f.read()

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

"""English to French translator"""
def english_to_french(english_text):
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    output = translation['translations']
    french_text = output[0]
    return french_text['translation']

"""English to French translator"""
def french_to_english(french_text):
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    output = translation['translations']
    english_text = output[0]
    return english_text['translation']
