import requests
import os
import logging

TRANSPORT_API_URL = os.getenv("TRANSPORT_API_URL")

import cachecontrol
sess = cachecontrol.CacheControl(requests.Session())

def get_module_logger():
	return logging.getLogger()

def request(target, url_params):
	
	full_url = TRANSPORT_API_URL + target
	
	r = sess.get(full_url, params=url_params)

	get_module_logger().info("Using params {}".format(url_params))
	get_module_logger().info("Requesting {}".format(r.url))

	return r.json()
