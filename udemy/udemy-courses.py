import requests
import json
from requests.auth import HTTPBasicAuth

# This is the maximum results of courses that the Udemy API can return in a single GET request
payload = {
	'page': '1',
	'page_size': '100'
}

# We are going to use HTTP Basic Authentication in order to use Udemy APIs.
basic = HTTPBasicAuth('uclPrCbXWfaAxPneidKaZNalPBLm7pA1up0JrVWX', 
	'vl1GW8gX0QOW5KtLMQsRigwInD39khdh3zIxKDR3NAMBwmTCX5EBpmLDtADtc1tyn29vMWgcPAlxmnJIxub0DCxsN9B3UrfTR8UyKUhAYfacwF6MWpXObbIXTEN8SNuc')


all_courses = []

while payload['page'] != '85':
	r = requests.get(
		"https://www.udemy.com/api-2.0/courses/", 
		auth = basic, 
		timeout = 20,
		params = payload
	)

	response_dict = r.json()
	results = response_dict['results']
	# print("I am in iteration"+payload['page'])
	for result in results:
		all_courses.append(result)
	payload['page'] = str(int(payload['page']) + 1)

with open('udemy-data.json', 'w', encoding='utf-8') as f:
    json.dump(all_courses, f, ensure_ascii=False, indent=4)

# this must print 8380
print(len(all_courses))