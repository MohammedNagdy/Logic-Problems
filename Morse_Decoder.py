# Dictionary representing the morse code chart 
MORSE_CODE = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 


def decodeMorse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    morse_code = morse_code + " "
    space = 0
    letter = ""
    message = ""
    for l in morse_code:
        if l != " ":
            #counter for space
            space = 0
            #get the letter
            letter += l
        #there's one space then there's a new letter after the space        
        #otherwise use space for a new word
        else:
            space += 1
            #checking for a new letter or space
            if space == 1:
                #get the key from the value in the dict
                #getting the letter from the dict
                char = [let for let , code in MORSE_CODE.items() if code == letter] 
                message += "".join(char)
                letter = ""
            
            elif space == 3:
                message += " "
            else:
                pass
                #raise "Error in spacing"
    return message
