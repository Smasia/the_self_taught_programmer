# challenge 1
for i in "Camus":
    print(i)

# challenge 2
string1 = input("type somethin: ")
string2 = input("type somethin: ")
print(f"Yesterday I wrote a {string1}. I sent it to {string2}!")

# challenge 3
def capitalize(sentence: str):
    return sentence[0].upper() + sentence[1:]
print(capitalize("aldous Huxley was born in 1984"))