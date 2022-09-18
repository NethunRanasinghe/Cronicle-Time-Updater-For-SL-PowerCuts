from bs4 import BeautifulSoup
from time import sleep
import Logging as LG
from scrapingant_client import ScrapingAntClient

Code_List = []
Disconnect_Time = []

url = 'https://cebcare.ceb.lk/Incognito/DemandMgmtSchedule'

client = ScrapingAntClient(token='--Enter Your API--')
page_content = client.general_request(url).content


def GetPage():
    soup = BeautifulSoup(page_content, 'lxml')
    Cells = soup.find_all('div', {'class':'fc-content'})

    if(len(soup.find_all('div', {'class':'fc-content'})) > 0):
        LG.WriteLog("Done !")
        Code_List.append(Cells)
        GetValues(Cells)
    else:
        LG.WriteLog("Trying Again ...")
        sleep(3)
        GetPage()

def GetValues(Cell_List):
    My_Group = []
    Disconnect_Time_Temp = []
    

    #Add content of my group to a list
    for items in Cell_List:
        Group = items.find('div', class_="fc-title").text
        
        if Group == 'T':
            My_Group.append(items)
        else:
            pass
    
    #Get Disconnect times
    for content in My_Group:
        DTime = content.find('div', class_="fc-time").text
        Disconnect_Time_Temp.append(DTime)

    for times in Disconnect_Time_Temp:
        if("PM" in times):
            CTimeP = times.split("PM")[0]
            CTimeP = str(int(CTimeP.split(":")[0]) + 12) + ":" + CTimeP.split(":")[1]
            Disconnect_Time.append(CTimeP)

        elif("AM" in times):
            CTimeA = times.split("AM")[0]
            Disconnect_Time.append(CTimeA)

def RunScrapper():
    LG.WriteLog("Starting Scrapping !")
    GetPage()

    LG.WriteLog("Scrapping Finished !")
    LG.WriteLog("###################################################################################################")

    return Disconnect_Time