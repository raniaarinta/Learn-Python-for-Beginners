secret_word="giraffe"
guess=""
counter_guess=0
guess_count=3
check_guess=False

while secret_word!=guess and not(check_guess):
    if(counter_guess<guess_count):
        guess=input("guess the secret word: ")
        counter_guess+=1
    else:
        check_guess=True
if check_guess:
    print("out of guess")
else:
    print("you win")
   



    