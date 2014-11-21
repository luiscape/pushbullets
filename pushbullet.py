## Script to push notifications using
## Pushbullet.

# For more information about Pushbullet and its
# API, please visit the service's web-page:
# https://docs.pushbullet.com/v2/pushes/

import sys
import os
import json
import requests as r

# for now you have to use Luis Capelo's API key. Ask him.
key = 'API_KEY'

# function to build the alert message that will
# be sent to the team.
def buildMessage(rev_id):

	# collect the data message that needs to
	# be sent

	# id
	# rev_id = sw.sqlite.get_var('latest_id')
	rev_id = '6d57ddaa-b447-4659-a987-e08011a30895'

	# getting information about the revision
	# in question
	url = 'https://data.hdx.rwlabs.org/api/action/revision_show?id=' + rev_id
	doc = r.get(url)
	data = doc.json()

	# parsing the body of message
	action = data["result"]["message"]
	user = data["result"]["author"]
	dataset_name = data["result"]["packages"][0]

	# building the title
	title = dataset_name + " changed."

	# getting everything together
	body = dataset_name + " changed. " + user + ": " + action

	# building the url
	update_url = 'https://data.hdx.rwlabs.org/dataset/' + dataset_name

	# building payload
	payload = {"type": "link", "title": title, "body": body, "url": update_url, "channel_tag": "dataset_alerts"}

	# returning results
	return payload


def sendAlert(rev_id):

	# defining authorization
	key_string = "Bearer " + key
	headers = {'content-type': 'application/json', "Authorization": key_string }

	payload = buildMessage(rev_id)

	# sending notification
	r.post('https://api.pushbullet.com/v2/pushes',
			data=json.dumps(payload),
			headers=headers)


# collecting parameters from the command line
if __name__ == '__main__':
    if len(sys.argv) <= 1:
        usage = '''python scripts/script.py {api-key}

				e.g.

				python scripts/script.py API-KEY
				'''
        print(usage)
        sys.exit(1)

    # collectig the API key from
    # command line and passing it to the
    # sendAlert function
    rev_id = sys.argv[1]
    sendAlert(rev_id)
