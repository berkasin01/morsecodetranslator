from morseCode import MorseCode

morse = MorseCode()
translate_on = True
while translate_on:
    morse.translate()
    get_final = input("Would you like to translate something else?Y or N")
    if get_final == "N":
        translate_on = False
