# Pushbullet Alerts
Helper functions to send alerts through the HDX channels hosted at [Pushbullet](https://www.pushbullet.com/). It combines the CKAN API interface with Pushbullet's API, making it easy to send notifications to a number of mobile devices with HDX content.

This is **work-in-progress**. Use at your own risk.

## Usage

The functions of the scripts were tailored to use HDX content. Right now the main fuction, `sendAlert()` only takes one argument: CKAN's revision id or `rev_id` for short. Here is an example usage:

```python
import pushbullet

pushbullet.sendAlert('6d57ddaa-b447-4659-a987-e08011a30895')
```

## API Key
Right now the script is configured to use my API key. Soon enough it should be using HDX's API key. My API key is not included in the script. Send me an [email](capelo@un.org) about that if you are interested.

Please use with caution. The HDX team may get annoyed very quickly. :-}