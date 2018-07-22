import requests
import urllib

# Language detect docpage is https://tech.yandex.com/translate/doc/dg/reference/detect-docpage/
def detect_lang(requests_session, text, api_key): # To example: detect_lang(requests_session, 'Hello World!', TRANSLATE_API_KEY)
	post_url = 'https://translate.yandex.net/api/v1.5/tr.json/detect'
	post_params = {'key': api_key}
	post_data = {'text': text}
	detect_result = requests_session.post( post_url, data=post_data, params=post_params )
	return (detect_result.json()) # Return dict in formate {'code': 200, 'lang': 'en'}

# Text translate docpage https://tech.yandex.com/translate/doc/dg/reference/translate-docpage/
def translate(requests_session, text, from_lang, to_lang, api_key): # To example: translate(requests_session, 'Hello', 'en', 'ru', TRANSLATE_API_KEY)
	post_url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
	post_params = {'lang': from_lang + '-' + to_lang,
					'key': api_key}
	post_data = {'text': text}
	translate_result = requests_session.post( post_url, data=post_data, params=post_params )
	return(translate_result.json()) # Return dict in formate {'text': ['Привет'], 'lang': 'en-ru', 'code': 200}