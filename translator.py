from tkinter import *
from tkinter.ttk import Combobox

root = Tk()
root.geometry("500x400")
root.title("Translator")
root.iconbitmap("Translator.ico")
root.resizable(False, False)
root.configure(bg = "#d62828")
lang_dict = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}

######################################################## ComboBox Languages
languages = StringVar()
font_box = Combobox(root, width = 30, textvariable = languages, state = "readonly")
font_box["values"] = [e for e in lang_dict.keys()]
font_box.current(38)

######################################################## Entry Box
varname1 = StringVar()
entry1 = Entry(root, width = 30, textvariable = varname1, font = ("times", 15, "italic bold"), relief = RAISED)
entry1.place(x = 150, y = 40)

varname2 = StringVar()
entry2 = Entry(root, width = 30, textvariable = varname2, font = ("times", 15, "italic bold"), relief = RAISED)
entry2.place(x = 150, y = 100)

######################################################## Labels
label1 = Label(root, text = "Enter Words : ", font = ("times", 15, "italic bold"), bg = "#d62828")
label1.place(x = 5, y = 40)

label2 = Label(root, text = "Translated : ", font = ("times", 15, "italic bold"), bg = "#d62828")
label2.place(x = 5, y = 100)

label3 = Label(root, text = " ", font = ("times", 15, "italic bold"), bg = "#d62828")
label3.place(x = 10, y = 250)

######################################################## Buttons
imgbt1 = PhotoImage(file = "click.png")
imgbt2 = PhotoImage(file = "log-out.png")

imgbt1 = imgbt1.subsample(15, 15)
imgbt2 = imgbt2.subsample(15, 15)


btn1 = Button(root, text = "Click", bd = 10, bg = "yellow", activebackground = "red", width = 100, font = ("times", 15, "italic bold"), image = imgbt1, compound = RIGHT)
btn1.place(x = 70, y = 170)

btn2 = Button(root, text = "Exit", bd = 10, bg = "yellow", activebackground = "red", width = 100, font = ("times", 15, "italic bold"), image = imgbt2, compound = RIGHT)
btn2.place(x = 280, y = 170)



root.mainloop()
