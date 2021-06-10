import random

alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ь", "э", "ю", "я"]


string_in = input()
string_out = ""
while "это" not in string_out:
    for g in alphabet:
        alphabet.insert(0, alphabet[random.randint(0, len(alphabet)-1)])
        string_out = ""
        for i in string_in:
            if i == " ":
                continue
            index = alphabet.index(str(i), 0, len(alphabet))
            string_out = str(string_out) + str(alphabet[index-1])

        if string_out == "это":
            break
    if string_out == "это":
        break

print(string_out)
print(alphabet)