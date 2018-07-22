import translate_api
import configparser
import requests

def mk_requests_session():
	requests_session = requests.session()
	return (requests_session)

def autodetect_translate(requests_session, text, default_langs, api_key):
	detect_result = translate_api.detect_lang(requests_session, text, api_key)

	if len(text)<1: text = 'test' 

	if detect_result['code'] != 200:
		return detect_result
		
	from_lang = detect_result['lang']

	if from_lang == default_langs['from_lang']:
		to_lang = default_langs['to_lang']
	elif from_lang == default_langs['to_lang']:
		to_lang = default_langs['from_lang']
	else:
		to_lang = default_langs['to_lang']

	translate_result = translate_api.translate(requests_session, text, from_lang, to_lang, api_key)
	return(translate_result)