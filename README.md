# Cronicle Time Updater For SL PowerCuts

This is a simple script written to create new shutdown events in cronicle task schedular according to the time of Sri Lankan daily powercuts.

i. It scraps the power disconnect time from "https://cebcare.ceb.lk/Incognito/DemandMgmtSchedule" website.

ii. By default it deletes any exsisting cronicle events (You can easily create a group for powercut events and add it as a filter to make sure other events won't get deleted).

iii. By default, it creates  shutdown shell scripts for the appropiate times. Change the POST request according to your need.

iv. After success, it will send an email to the specified email address.

**Don't Forget to Change the API keys for cronicle and webscrapping API**
