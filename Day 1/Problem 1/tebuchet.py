f = open("input.txt", "r")
lines = f.readlines()

accumulator = 0
number_characters = ""

for line in lines:
    for character in line:
        if character.isdecimal():
            number_characters += character
            for character in reversed(line):
                if character.isdecimal():
                    number_characters += character
                    accumulator += int(number_characters)
                    break
            number_characters = ""
            break
            

print(accumulator)