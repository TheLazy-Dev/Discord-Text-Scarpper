import requests
import json

messages=[]
def retrive_messages(channel_id):
    headers = {
                'authorization': '{Authorization(Check Readme)}'
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers)
    jsonn = json.loads(r.text)
    for value in jsonn:
        user    = value['author']['username']
        content = value['content']
        message = f'{user} :\n{content}'
        messages.append(message)

    messages.reverse()
    for message in messages:
            with open(f'Scraped Messages/message_{channel_id}.txt' ,"a", encoding='utf-8') as myfile:
                myfile.write(message)
                myfile.write("\n")
                myfile.write("\n")


retrive_messages('channel_ID')
