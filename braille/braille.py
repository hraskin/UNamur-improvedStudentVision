# Written by Aadit Trivedi
# June 6, 2018
# Braille Library

char_to_array = {
    " " : [[0,0],[0,0],[0,0]],
    "a" : [
            [1,0],
            [0,0],
            [0,0]
        ],
    "b" : [
            [1,0],
            [1,0],
            [0,0]
        ],
    "c" : [
            [1,1],
            [0,0],
            [0,0]
        ],
    "d" : [
            [1,1],
            [0,1],
            [0,0]
        ],
    "e" : [
            [1,0],
            [0,1],
            [0,0]
        ],
    "f" : [
            [1,1],
            [1,0],
            [0,0]
        ],
    "g" : [
            [1,1],
            [1,1],
            [0,0]
        ],
    "h" : [
            [1,0],
            [1,1],
            [0,0]
        ],
    "i" : [
            [0,1],
            [1,0],
            [0,0]
        ],
    "j" : [
            [0,1],
            [1,1],
            [0,0]
        ],
    "k" : [
            [1,0],
            [0,0],
            [1,0]
        ],
    "l" : [
            [1,0],
            [1,0],
            [1,0]
        ],
    "m" : [
            [1,1],
            [0,0],
            [1,0]
        ],
    "n" : [
            [1,1],
            [0,1],
            [1,0]
        ],
    "o" : [
            [1,0],
            [0,1],
            [1,0]
        ],
    "p" : [
            [1,1],
            [1,0],
            [1,0]
        ],
    "q" : [
            [1,1],
            [1,1],
            [1,0]
        ],
    "r" : [
            [1,0],
            [1,1],
            [1,0]
        ],
    "s" : [
            [0,1],
            [1,0],
            [1,0]
        ],
    "t" : [
            [0,1],
            [1,1],
            [1,0]
        ],
    "u" : [
            [1,0],
            [0,0],
            [1,1]
        ],
    "v" : [
            [1,0],
            [1,0],
            [1,1]
        ],
    "w" : [
            [0,1],
            [1,1],
            [0,1]
        ],
    "x" : [
            [1,1],
            [0,0],
            [1,1]
        ],
    "y" : [
            [1,1],
            [0,1],
            [1,1]
        ],
    "z" : [
            [1,0],
            [0,1],
            [1,1]
        ],
}


asciicodes = [' ','!','"','#','$','%','&','','(',')','*','+',',','-','.','/',
          '0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@',
          'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
          'r','s','t','u','v','w','x','y','z','[','\\',']','^','_']
brailles = ['⠀','⠮','⠐','⠼','⠫','⠩','⠯','⠄','⠷','⠾','⠡','⠬','⠠','⠤','⠨','⠌','⠴','⠂','⠆','⠒','⠲','⠢',
        '⠖','⠶','⠦','⠔','⠱','⠰','⠣','⠿','⠜','⠹','⠈','⠁','⠃','⠉','⠙','⠑','⠋','⠛','⠓','⠊','⠚','⠅',
        '⠇','⠍','⠝','⠕','⠏','⠟','⠗','⠎','⠞','⠥','⠧','⠺','⠭','⠽','⠵','⠪','⠳','⠻','⠘','⠸']


def text_to_braille(text):
    ascii_braille = {}

    arrayLength = len(asciicodes)
    counter = 0

    while counter < arrayLength:
        ascii_braille[asciicodes[counter]] = brailles[counter]
        counter = counter + 1

    final_string = ''
    for char in text:
        char = char.lower()
        if char == "a":
            final_string = final_string + ascii_braille[char]
        elif char == "b":
            final_string = final_string + ascii_braille[char]
        elif char == "c":
            final_string = final_string + ascii_braille[char]
        elif char == "d":
            final_string = final_string + ascii_braille[char]
        elif char == "e":
            final_string = final_string + ascii_braille[char]
        elif char == "f":
            final_string = final_string + ascii_braille[char]
        elif char == "g":
            final_string = final_string + ascii_braille[char] 
        elif char == "h":
            final_string = final_string + ascii_braille[char]
        elif char == "i":
            final_string = final_string + ascii_braille[char] 
        elif char == "j":
            final_string = final_string + ascii_braille[char]
        elif char == "k":
            final_string = final_string + ascii_braille[char]
        elif char == "l":
            final_string = final_string + ascii_braille[char]
        elif char == "m":
            final_string = final_string + ascii_braille[char]
        elif char == "n":
            final_string = final_string + ascii_braille[char]
        elif char == "o":
            final_string = final_string + ascii_braille[char]
        elif char == "p":
            final_string = final_string + ascii_braille[char]
        elif char == "q":
            final_string = final_string + ascii_braille[char]
        elif char == "r":
            final_string = final_string + ascii_braille[char]
        elif char == "s":
            final_string = final_string + ascii_braille[char]
        elif char == "t":
            final_string = final_string + ascii_braille[char]
        elif char == "u":
            final_string = final_string + ascii_braille[char]
        elif char == "v":
            final_string = final_string + ascii_braille[char]
        elif char == "w":
            final_string = final_string + ascii_braille[char] 
        elif char == "x":
            final_string = final_string + ascii_braille[char]
        elif char == "y":
            final_string = final_string + ascii_braille[char]
        elif char == "z":
            final_string = final_string + ascii_braille[char]
        elif char == " ":
            final_string = final_string + ascii_braille[char]
    print(final_string)
    return final_string