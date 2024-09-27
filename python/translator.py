import sys

english_to_braille = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
    ".": ".O.OOO",
    ",": ".O....",
    "?": ".OO.O.",
    "!": ".OO.OO",
    ":": ".O.O..",
    ";": ".OO...",
    "-": "..O..O",
    "/": "..OO..",
    "<": "..O.O.",
    ">": "..O.OO",
    "(": "..O..O",
    ")": "..OO.O",
    " ": "......",
    "capital_follow": ".....O",
    "decimal_follow": ".O...O",
    "number_follow": ".O.OOO",
}

number_to_braille = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
}

sym_to_braille = {
    ".": ".O.OOO",
    ",": ".O....",
    "?": ".OO.O.",
    "!": ".OO.OO",
    ":": ".O.O..",
    ";": ".OO...",
    "-": "..O..O",
    "/": "..OO..",
    "<": "..O.O.",
    ">": "..O.OO",
    "(": "..O..O",
    ")": "..OO.O"
}

braille_to_english = {
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",
    "......": " ",
}

braille_to_sym = {
    ".O.OOO": ".",
    ".O....": ",",
    ".OO.O.": "?",
    ".OO.OO": "!",
    ".O.O..": ":",
    ".OO...": ";",
    "..O..O": "-",
    "..OO..": "/",
    "..O.O.": "<",
    "..O.OO": ">",
    "..O..O": "(",
    "..OO.O": ")",
}

braille_to_num = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0"
}

def text_to_braille(text):
    results = []
    number_mode = False

    for char in text:
        if(char.isalpha()):
            number_mode = False
            if(char == char.lower()):
                results.append(english_to_braille[char.lower()])
            else:
                results.append(english_to_braille["capital_follow"])
                results.append(english_to_braille[char.lower()])
        elif(char.isnumeric() or number_mode):
            if(number_mode):
                results.append(english_to_braille[char])
            else:
                results.append(english_to_braille["number_follow"])
                results.append(english_to_braille[char])
            number_mode = True
        else:
            if(char == " "):
                results.append(english_to_braille[char])
            else:
                results.append(english_to_braille["decimal_follow"])
                results.append(english_to_braille[char])
            number_mode = False

    return "".join(results)

def braille_to_text(braille_input):
    results = []
    i = 0
    number_mode = False
    capital_mode = False
    sym_mode = False

    while (i < len(braille_input)):
        current_braille = braille_input[i:i+6]
        if(current_braille == ".....O"):
            capital_mode = True
            sym_mode = False
            number_mode = False
            i += 6
            continue
        elif(current_braille == ".O.OOO"):
            number_mode = True
            capital_mode = False
            sym_mode = False
            i += 6
            continue
        elif(current_braille == ".O...O"):
            sym_mode = True
            number_mode = False
            capital_mode = False
            i += 6
            continue
        elif(current_braille in braille_to_english):
            if(number_mode):
                results.append(braille_to_num[current_braille])
            else:
                char = braille_to_english[current_braille]
                if(char == "capital_follow" or char == "number_follow"):
                    pass
                else:
                    if(capital_mode):
                        results.append(char.upper())
                    else:
                        results.append(char)
            capital_mode = False
        elif(sym_mode):
            results.append(braille_to_sym[current_braille])
        
        i += 6

    return "".join(results)

if __name__ == "__main__":
    input_text = " ".join(sys.argv[1:])

    dic = {"b": 0, "n_b": 0}
    english = False
    output = ""

    for char in input_text:
        if(char == "O" or char == "."):
            dic["b"] += 1
        else:
            english = True
            break

    if(english):
        output = text_to_braille(input_text)
    else:
        output = braille_to_text(input_text)
    print(output)