## Script to push notifications using
## Pushbullet.

# For more information about Pushbullet and its
# API, please visit the service's web-page:
# https://docs.pushbullet.com/v2/pushes/

import sys
import json
import requests as r

# for now you have to use Luis Capelo's API key. Ask him.
key = 'API_KEY'

# function to build the alert message that will
# be sent to the team.
def buildMessage(rev_id):

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
        usage = '''python scripts/script.py {revision_id}

				e.g.

				python scripts/script.py 6d57ddaa-b447-4659-a987-e08011a30895
				'''
        print(usage)
        sys.exit(1)

    # collecting the revision id from
    # the command line interface
    # and passing to the sendAlert function
    rev_id = sys.argv[1]
    sendAlert(rev_id)
