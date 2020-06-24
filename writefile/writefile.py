#read file
def readallfile():
    file=open("sample.txt","r")
    if file.readable():
        print(file.read())
#write with new file
def writeNewFile():
    file=open("sample1.txt","w")
    file.write("\nT - quality control")
    file.close()
#create HTML  new file
def write_HTML_New_File():
    file=open("index.html","w")
    file.write("<h1>hello world</h1>")
    file.close()
#read file
def read_HTML_file():
    file=open("index.html","r")
    if file.readable():
        print(file.read())
#write file replacing the exsisting file
def writefile():
    file=open("sample.txt","w")
    file.write("\nT - quality control")
    file.close()
#append file
def appendfile():
    file=open("sample.txt","a")
    file.write("\nT - quality control")
    file.close()
#read and write file
def readwritefile():
    file=open("sample.txt","r+")
    file.close()

write_HTML_New_File()
read_HTML_file()