import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def convert():
    word = input("Enter a word: ").upper()
    try:
        outputlist = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alaphbet")
        convert()
    else:
        print(outputlist)


convert()
