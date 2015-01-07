# Import the pushbullet script.
import pushbullet

# Add the HDX pushbullet API key here.
hdx_key = 'XXXXX'

# And build the payload / message you want o build.
# The payload contains a few options, such as message type
# and URL. From more information about those options,
# please refer to the Pushbullet documentation here:
# https://docs.pushbullet.com/v2/pushes/
payload = {"type": "link", "title": "WHO updated EVD data", "body": "WHO just updated the Ebola data.", "url": "#", "channel_tag": "hdx-alerts"}

# Use the sendAlert function to send an alert
# to all subscribers. You'll need to pass a
# payload and the HDX API key.
pushbullet.sendAlert(pushbullet_key, payload)
