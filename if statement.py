is_female = False
is_tall= True
if is_female and is_tall:
    print("i am a female and tall")
elif is_female and not(is_tall):
    print("i am a female")
elif is_tall and not(is_female):
    print("i am a tall")
else:
    print("i am not a female and short")
