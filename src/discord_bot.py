import requests
import io
import uuid

# discord webhook
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/847295744925761616/PRRoam6IMBRqMfxZC5Iz_CAqD17n5rycpHPByYPlHgyZGR1uwtgVoI_GhE_NMplq_V91"

def prefix(length=8):
    return str(uuid.uuid1()).replace("-", "")[:length]

def notify(message, webhook=DISCORD_WEBHOOK, **kwargs):
    if len(message) > 2000:
        fname = prefix()
        kwargs.update({"files": {fname: io.StringIO(message)}})
        # submit only a preview, attach the rest in file
        message = "{}{}{}".format(message[:500], "."*79, message[-500:]) 
    
    requests.post(webhook, data={"content": message}, **kwargs)