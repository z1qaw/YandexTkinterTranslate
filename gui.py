import translate
import translate_api

import pyperclip
import configparser
import tkinter
import os

from tkinter import *
from tkinter import messagebox


class Window(Frame):

	def __init__(self, master=None):
		Frame.__init__(self, master)                 
		self.master = master
		self.init_window()
		

	def init_window(self):

		config = configparser.ConfigParser()
		config.read('cfg.ini')

		TRANSLATE_API_KEY = config['DEFAULT']['yandexapikey']
		DEFAULT_LANGS = {'from_lang': config['DEFAULT']['fromlang'],
						'to_lang': config['DEFAULT']['tolang']}

		self.master.title("Translate")
		self.pack(fill=BOTH, expand=1)
		from_lang_text_entry = Entry(self)
		from_lang_text_entry.place(x=0, y=0)

		to_lang_text_entry = Entry(self)
		to_lang_text_entry.place(x=0, y=25)

		from_lang_var = StringVar()
		to_lang_var = StringVar()

		from_lang_var.set(DEFAULT_LANGS['from_lang'])
		to_lang_var.set(DEFAULT_LANGS['to_lang'])


		from_lang_label = Label(self, textvariable=from_lang_var, relief=RAISED)
		from_lang_label.place(x=170, y=0)

		to_lang_label = Label(self, textvariable=to_lang_var, relief=RAISED)
		to_lang_label.place(x=170, y=25)

		Window.translate_clipboard(to_lang_text_entry, from_lang_text_entry,
							from_lang_var, to_lang_var,
							from_lang_label, to_lang_label,
							TRANSLATE_API_KEY, DEFAULT_LANGS)

	def translate_clipboard(to_lang_text_entry, from_lang_text_entry,
							from_lang_var, to_lang_var,
							from_lang_label, to_lang_label,
							TRANSLATE_API_KEY, DEFAULT_LANGS):
		clipboard_text = pyperclip.paste()
		autodetect_translate_result = translate.autodetect_translate(
												translate.mk_requests_session(),
												clipboard_text,
												DEFAULT_LANGS,
												TRANSLATE_API_KEY
												)

		if autodetect_translate_result['code'] != 200:
			messagebox.showinfo("Error", autodetect_translate_result['message'])

		translated_text = autodetect_translate_result['text'][0]

		from_lang_text_entry.insert(0, clipboard_text)
		to_lang_text_entry.insert(0, translated_text)

		detect_langs = translated_text = autodetect_translate_result['lang'].split('-')
		from_lang_var.set(detect_langs[0])
		to_lang_var.set(detect_langs[1])


def main():
	root = Tk()

	x_screen_pos = (root.winfo_screenwidth())
	y_screen_pos = 0
	root.wm_geometry("+%d+%d" % (x_screen_pos, y_screen_pos))

	root.geometry("200x50")
	root.resizable(width=False, height=False)

	app = Window(root)
	root.mainloop()

if __name__ == '__main__':
	main()