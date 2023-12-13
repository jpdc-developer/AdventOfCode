# with open("input.txt", "r") as f:
# use with to properly close file when no longer needed
with open("input.txt", "r") as f:
    lines = f.readlines()

    accumulator = 0
    number_characters = ""

    for line in lines:
        # use list comprehension to extract digits
        # instead of 2 nested for loops with if statements and breaks
        # digits = [char for char in line if char.isdecimal()]
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