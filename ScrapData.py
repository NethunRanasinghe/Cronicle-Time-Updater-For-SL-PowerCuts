import Logging as LG
import requests
from datetime import datetime, timedelta
requests.packages.urllib3.disable_warnings()

S_Cookie = "Your_Cookie"

S_Auth = "Auth_Token"

Date1 = datetime.now().strftime('%Y-%m-%d')
Date2 = datetime.now() + timedelta(days=1)

Disconnect_Time = []

def GetValues(cookie, verify_token):
    S_Headers = {
            "Content-Type":"json",
            "Cookie":cookie,
            "RequestVerificationToken" : verify_token
            }

    S_URL = f"https://cebcare.ceb.lk/Incognito/GetCalendarData?from={Date1}&to={Date2.strftime('%Y-%m-%d')}&acctNo=Your_ACC_NU"

    response = requests.get(url=S_URL,headers=S_Headers,verify=False)

    GetTime(response.json())


def GetTime(J_Content):

    Interupts = J_Content['interruptions']
    
    for v in Interupts:
        if 'startTime' in v :
            T_Time = v['startTime'].split('T')[1].split(":")
            S_Time = T_Time[0] + ":" + T_Time[1]

            Disconnect_Time.append(S_Time) 

def RunScrapper():
    LG.WriteLog("Starting Scrapping !")
    GetValues(S_Cookie,S_Auth)

    LG.WriteLog("Scrapping Finished !")
    LG.WriteLog("###################################################################################################")

    return Disconnect_Time