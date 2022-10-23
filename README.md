# Cronicle Time Updater For SL PowerCuts

This is a simple script written to create new shutdown events in cronicle task schedular according to the time of Sri Lankan daily powercuts.

i. It scraps the power disconnect time from "https://cebcare.ceb.lk/Incognito/OutageMap" website.

ii. By default it deletes any exsisting cronicle events (You can easily create a group for powercut events and add it as a filter to make sure other events won't get deleted).

iii. By default, it creates  shutdown shell scripts for the appropiate times. Change the POST request according to your need.

iv. After success, it will send an email to the specified email address.

<h2> Since this is not sesitive information I don't think it's illegal but plase use this responsibly. </h2>

* You can get the cookie and auth(Request verification code) using inspect elements (https://cebcare.ceb.lk/Incognito/OutageMap) and checking the network -> Fetch/XHR
* It is inside the request header.
* For some reason this cookie and auth doesn't expire so you only have to set it once. 
* Your electric bill account number will be on the CEB care app(You can also get your powerct group from the app) or inside any old electricity bills you recieved.


**Don't Forget to Change the API keys and set the correct api endpoint for cronicle**
