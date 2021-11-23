import googletrans
dict1 = googletrans.LANGUAGES
dict2 = {value: key for key, value in dict1.items()}
j = 0
for i in dict1.items():
    if i[0] == "hi":
        print(j)
    j += 1

