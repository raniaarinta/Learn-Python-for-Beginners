#read file
def readallfile():
    file=open("sample.txt","r")
    if file.readable():
        print(file.read())
    file.close()
#read line
def readline():
    file=open("sample.txt","r")
    if file.readable():
        print(file.readline())
    file.close()
#read line array
def readLineArray():
    file=open("sample.txt","r")
    if file.readable():
        print(file.readlines()[0])
    file.close()
#read line array loop
def readLineArrayLoop():
    file=open("sample.txt","r")
    if file.readable():
        for sample in file.readlines():
            print(sample)
    file.close()

    
readLineArrayLoop()