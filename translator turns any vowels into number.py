#convert any vowls into number
#if the vowls is an uppercase turn into 1
#if the vowls is lower case turn into 0
#example Ant= 1nt and ant=0nt

def translate(phrase):
    translation=""
    for letter in phrase:
        if letter in "AIUEOaiueo":
            if letter.isupper():
                translation= translation + "1"
            else:
                translation= translation + "0"
        else:
            translation=translation + letter
    return translation

print(translate(input("insert pharse: ")))