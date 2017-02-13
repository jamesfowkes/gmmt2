import requests
import os
import logging

TRANSPORT_API_URL = os.getenv("TRANSPORT_API_URL")

import cachecontrol
sess = cachecontrol.CacheControl(requests.Session())

def request(target, url_params):
	full_url = TRANSPORT_API_URL + target
	
	r = sess.get(full_url, params=url_params)

	logging.info("Requesting {}".format(r.url))

	return r.json()
