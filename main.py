import ScrapData as SD
import CronicleUpdateRecord as CUR
import Logging as LG

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

    CUR.Create_Events(h,m,t)

LG.WriteLog("Creating new events Finished !")
LG.WriteLog("###################################################################################################")