import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def french_to_english(frenchtext) :
    """
    Test
    """
    authenticator = IAMAuthenticator('-wPGTj5SIrBzZbvffqnEjGgtpNgdRfAHm5g2MioxyDbZ')
    language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)
    language_translator.set_service_url(
        'https://api.eu-gb.language-translator.watson.cloud.ibm.com')
    englishtranslation= language_translator.translate(
    text=frenchtext, model_id='fr-en').get_result()

    return englishtranslation.get("translations")[0].get("translation")

def english_to_french(englishtext) :
    authenticator = IAMAuthenticator('-wPGTj5SIrBzZbvffqnEjGgtpNgdRfAHm5g2MioxyDbZ')
    language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)
    language_translator.set_service_url(
        'https://api.eu-gb.language-translator.watson.cloud.ibm.com')

    frenchtranslation= language_translator.translate(
    text=englishtext, model_id='en-fr').get_result()

    return frenchtranslation.get("translations")[0].get("translation")