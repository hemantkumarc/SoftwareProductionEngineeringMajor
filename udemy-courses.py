import requests
import json

# This is the maximum results of courses that the Udemy API can return in a single GET request
payload = {
	'page_size': '100'
}

# We provide URL, HTTP Basic Authentication and Timeout options to the GET request.
r = requests.get(
	"https://www.udemy.com/api-2.0/courses/", 
	auth = ('uclPrCbXWfaAxPneidKaZNalPBLm7pA1up0JrVWX', 'vl1GW8gX0QOW5KtLMQsRigwInD39khdh3zIxKDR3NAMBwmTCX5EBpmLDtADtc1tyn29vMWgcPAlxmnJIxub0DCxsN9B3UrfTR8UyKUhAYfacwF6MWpXObbIXTEN8SNuc'), 
	timeout = 5,
	params = payload
)

# Below code works
# response_dict = r.json()  
# with open('udemy-data.json', 'w', encoding='utf-8') as f:
#     json.dump(response_dict, f, ensure_ascii=False, indent=4)