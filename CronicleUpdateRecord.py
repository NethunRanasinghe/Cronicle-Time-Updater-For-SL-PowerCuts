import requests
import Logging as LG

IDs = []

def Get_Events():
    url = "http://192.168.1.4:3012/api/app/get_schedule/v1?api_key=ADD YOUR API KEY"
    resp = requests.get(url)
    
    ContentJ = resp.json()
    Rows = ContentJ['rows']

    if len(Rows) != 0:
        #Get the ids of the exsisting events
        for i in range(len(Rows)):
            Row_Data = dict(Rows[i])
            IDs.append(Row_Data['id'])

        Delete_Events()
    else:
        pass

def Delete_Events():
    url = "http://192.168.1.4:3012/api/app/delete_event/v1?api_key=ADD YOUR API KEY"

    for Nu_Id in IDs:
        body = {"id" : f"{Nu_Id}"}
        resp = requests.delete(url=url,json=body)
        LG.WriteLog(str(resp))

def Create_Events(h,m,title):
    url = "http://192.168.1.4:3012/api/app/create_event/v1?api_key=ADD YOUR API KEY"
    body = {'enabled': 1, 
    'params': {'script': '#!/bin/sh\n\n/usr/sbin/shutdown -h now', 
    'annotate': 1, 'json': 0}, 
    'timing': {'hours': [h], 'minutes': [m]}, 
    'max_children': 1, 
    'timeout': 3600, 
    'catch_up': 0, 
    'queue_max': 1000, 
    'timezone': 'Asia/Colombo', 
    'plugin': 'shellplug', 
    'title': f'{title}', 
    'category': 'cl4xy9xzi01', 
    'target': 'proxmox', 
    'algo': 'random', 
    'multiplex': 0, 
    'stagger': 0, 
    'retries': 0, 
    'retry_delay': 0, 
    'detached': 0, 
    'queue': 0, 
    'chain': '', 
    'chain_error': '', 
    'notify_success': '', 
    'notify_fail': '', 
    'web_hook': '', 
    'cpu_limit': 0, 
    'cpu_sustain': 0, 
    'memory_limit': 0, 
    'memory_sustain': 0, 
    'log_max_size': 0, 
    'notes': 'Shutdown the server', 
    'modified': 1661712784
    }

    resp = requests.post(url=url,json=body)
    LG.WriteLog(str(resp.json()))
