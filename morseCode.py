class MorseCode:
    def __init__(self):
        self.morse_alphabet = ['.- ', '-... ', '-.-. ', '-.. ', '. ', '..-. ', '--. ', '.... ', '.. ', '.--- ', '-.- ',
                               '.-.. ', '-- ', '-. ', '--- ', '.--. ', '--.- ', '.-. ', '... ', '- ', '..- ', '...- ',
                               '.-- ', '-..- ', '-.-- ', '--.. ', ' / ', '.----. ', '-.-.-- ', '.--.-. ', ' / ',
                               '...-..- ', ' / ', '..-. ', ' / ', '.-... ', ' / ', '-.--. ', '-.--.- ', '..--.- ',
                               '-....- ', '-...- ', '.-.-. ', ' / ', '-.--. ', '-.-.-. ', '..--.. ', '.-.-.- ',
                               '----- ', '.---- ', '..--- ', '...-- ', '....- ', '..... ', '-.... ', '--... ',
                               '---.. ', '----. ']

        self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                         'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', "'", '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                         '_', '-', '=', '+', '{', '[', '}', ']', ':', ';', '?', '.', '0', '1', '2', '3', '4', '5', '6',
                         '7', '8', '9']

    def translate(self):
        start_translate = True
        while start_translate:

            user_text = input("What is the sentence to convert to Morse Code?").upper()
            morse_or_translate = input("Alphabet-Morse(A) or Morse-Alphabet(M)?A or M?")
            translation = []
            final = "Please Select a correct function!"

            if morse_or_translate == "A":
                split_text = list(user_text)
                for char in split_text:
                    get_index = self.alphabet.index(char)
                    translation.append(self.morse_alphabet[get_index])
                    final = "".join(translation)

            elif morse_or_translate == "M":
                split_text = user_text.split()
                for char in split_text:
                    if char == "/":
                        new_char = " " + char + " "
                        get_index = self.morse_alphabet.index(new_char)
                        translation.append(self.alphabet[get_index])
                    else:
                        new_char = char + " "
                        get_index = self.morse_alphabet.index(new_char)
                        translation.append(self.alphabet[get_index])
                final = "".join(translation)

            print(final)
            start_translate = False
