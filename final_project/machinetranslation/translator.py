import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(version='2022-09-09', 
authenticator=authenticator, service_name='Language Translator-5k')

language_translator.set_service_url(url)

def english_to_french(english_text): #write the code here
    french_text = language_translator.translate(
    text = english_text,
    model_id = 'en-fr').get_result()
    res_one = french_text["translations"]
    res_two = res_one[0]
    res_fin = res_two["translation"]
    return res_fin

def french_to_english(french_text): #write the code here
    english_text = language_translator.translate(
    text = french_text,
    model_id = 'fr-en').get_result()
    res_one = english_text["translations"]
    res_two = res_one[0]
    res_fin = res_two["translation"]
    return res_fin
