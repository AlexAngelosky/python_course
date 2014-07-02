import urllib

def read_file():
    text = open("D:\python\quotes.txt")#or other file
    data = text.read()
    print (data+"\n")     
    text.close()
    check_badwords(data)
    
def check_badwords(the_text):
    cheker = urllib.urlopen("http://www.wdyl.com/profanity?q="+the_text)
    message = cheker.read()
    #print(message)
    cheker.close()
    if "true" in message:       #this way is better
        print("ima psuvni tuk!!!")
    elif "false" in message:
        print("nqma psuvni!!!")
    else:
        print("error scanning")
    
        
read_file()    
