# Pushbullet Alerts
Helper functions to send alerts through the HDX channels hosted at [Pushbullet](https://www.pushbullet.com/). It combines the CKAN API interface with Pushbullet's API, making it easy to send notifications to a number of mobile devices with HDX content.

This version makes the scripts more high level. You have to pass to the function a payload and a channel. Please refer to HDX's notification channels documentation (under construction) for more information about what channel to use.

This is **work-in-progress**. Use at your own risk.

## Usage

The main fuction, `sendAlert()` takes three arguments `title`, `body`, and `channel`. The title and body arguments will be used to build the message sent to final users. The channel, specifies the HDX channel used.

Those three parameters should be passed to the `sendAlert()` function as follows:

```python
import pushbullet

# Buidling the parameters
title = "Dataset Edited"
body = "The dataset Ebola Cases in West Africa was just edited by Luis Capelo (luiscape)."
channel = "hdx-dev"  # Specify what channel

# Passing them to the sednAlert() function
pushbullet.sendAlert(title, body, channel)
```

## API Key
Right now the script is configured to use my API key. Soon enough it should be using HDX's API key. My API key is not included in the script. Send me an [email](capelo@un.org) about that if you are interested.

Please use with caution. The HDX team may get annoyed very quickly. :-}