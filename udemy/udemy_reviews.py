import requests
import json
from requests.auth import HTTPBasicAuth

# This is the maximum results of courses that the Udemy API can return in a single GET request
# payload = {
# 	'page': '1',
# 	'page_size': '100'
# }

review_payload = {
	'page': '1',
	'page_size': '100'
}

# We are going to use HTTP Basic Authentication in order to use Udemy APIs.
basic = HTTPBasicAuth('uclPrCbXWfaAxPneidKaZNalPBLm7pA1up0JrVWX', 
	'vl1GW8gX0QOW5KtLMQsRigwInD39khdh3zIxKDR3NAMBwmTCX5EBpmLDtADtc1tyn29vMWgcPAlxmnJIxub0DCxsN9B3UrfTR8UyKUhAYfacwF6MWpXObbIXTEN8SNuc')


# all_courses = []
all_reviews_per_course = []

while review_payload['page'] != '85':
	r = requests.get(
		"https://www.udemy.com/api-2.0/courses/4077322/reviews/", 
		auth = basic, 
		timeout = 20,
		params = review_payload
	)

	response_dict = r.json()
	results = response_dict['results']
	for result in results:
		if result['content']:
			all_reviews_per_course.append(result)
	review_payload['page'] = str(int(review_payload['page']) + 1)

	if response_dict['next'] is None:
		break


with open('udemy-review.json', 'w', encoding='utf-8') as f:
    json.dump(all_reviews_per_course, f, ensure_ascii=False, indent=4)

# This must print the number of reviews of a course.
print(len(all_reviews_per_course))




