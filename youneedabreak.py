import webbrowser
import time 

init=0
while (init<10):
    print ("started work " +time.ctime())
    time.sleep(60*60)#every hour a brake because 2 hours on the computer is bad
    print ("you need a brake :) " +time.ctime())
    webbrowser.open("https://www.youtube.com/watch?v=y6Sxv-sUYtM")
    init=init+1
 
