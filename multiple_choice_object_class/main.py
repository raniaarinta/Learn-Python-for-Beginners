from question import question
sample =["what is the colour of an orange \n(A). orange \n(B). blue\n(C). Purple \n your answer: \n",
           "What is 2+2?  \n(A). 4 \n(B). 0\n(C). 1 \n your answer: \n",
           "How many months do we have in a year \n(A).12 \n(B). 1\n(C). 4\n your answer: \n "]

question1= [question(sample[0],"a"),question(sample[1],"a"),question(sample[2],"a") ]

def run_question(question):
    score=0
    for question in question:
       answer= input(question.promt)
       if answer == question.answer:
           score=score+1
    print("your score is "+str(score) )

run_question(question1)