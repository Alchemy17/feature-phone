import math

print("input a word")

input = input().lower()

characters = {"1":[" ", "a","d","g","j","m","p","t","w"],
"2":['b','e','h','k','n','q','u','x'],
"3":['c','f','i','l','o','r','v','y'],
"4":['s','z']}

counter = 0
for character in input:
    for letters in characters.keys():
        if character in characters[letters]:
            counter = counter + int(letters)

    # characters.setdefault(character,0)
    # characters[character] = characters[character] + 1


print(counter)
