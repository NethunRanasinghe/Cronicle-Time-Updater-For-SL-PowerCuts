from datetime import datetime

def WriteLog(Log_Text):
    with open('Log.txt','a') as file:
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        lmsg = str(dt) + " : "  + str(Log_Text)
        file.write(lmsg+"\n")
        file.close