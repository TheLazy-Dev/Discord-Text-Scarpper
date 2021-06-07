import requests
import json

def retrive_messages(channel_id):
    headers = {
        'authorization': '{Authorization(Check Readme)}'
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers)
    jsonn = json.loads(r.text)
    for value in jsonn:
        with open("{Path/to/PreExisting/fileName.txt}","a") as myfile:
            myfile.write(value['content'])
            myfile.write("\n")
    

retrive_messages('channel_ID')
