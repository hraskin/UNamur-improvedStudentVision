# Written by Aadit Trivedi
# June 6, 2018
# Braille Library

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