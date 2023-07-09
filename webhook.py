import requests
import json

# Load config data from file
with open('config.json') as f:
    config = json.load(f)

# replace this with your Discord webhook URL
webhook_url = config["hook"]  

# replace this with your server IP/domain
minecraft_server_ip = 'vanyarozovych.aternos.me:56613'  

response = requests.get(f'https://api.mcsrvstat.us/2/{minecraft_server_ip}')
data = response.json()

if data['online']:
    status = 'Online'
    players = f"{data['players']['online']}/{data['players']['max']}"
    version = data['version']
    software = data.get('software', 'Unknown')  # some servers may not return this information
    hostname = data['hostname']
else:
    status = 'Offline'
    players = 'N/A'
    version = 'N/A'
    software = 'N/A'
    hostname = 'N/A'

message = {
    "content": f"**Minecraft Server Status**\n\n"
               f"**Status:** {status}\n"
               f"**Players:** {players}\n"
               f"**Version:** {version}\n"
               f"**Software:** {software}\n"
               f"**Hostname:** {hostname}\n"
}

requests.post(webhook_url, json=message)