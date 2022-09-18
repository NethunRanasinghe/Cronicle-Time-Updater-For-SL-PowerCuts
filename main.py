import ScrapData as SD
import CronicleUpdateRecord as CUR
import Logging as LG
import Send_Email as SE

Times_Title = []

#Get Disconnecting Times
Times = SD.RunScrapper()

#Delete Exsisting Events
LG.WriteLog("Deleting exsisting events !")

CUR.Get_Events()

LG.WriteLog("Deleting exsisting events Finished !")
LG.WriteLog("###################################################################################################")

#Add new events
LG.WriteLog("Creating new events !")

for i in range(len(Times)):
    h = int(Times[i].split(":")[0])
    m = int(Times[i].split(":")[1])
    t = Times[i]
    Times_Title.append(Times[i])

    CUR.Create_Events(h,m,t)

#Send email
for count,item in enumerate (Times_Title):
    Times_Title[count] = f"Event {count+1} at -> " + item

l = str(Times_Title)
l = l.replace(',',"\n").replace("'","").replace('[',"").replace(']',"")
l = f"New Shutdown events have been created ::: \n\n {l}"
SE.SendMail(l)

LG.WriteLog("Creating new events Finished !")
LG.WriteLog("###################################################################################################")