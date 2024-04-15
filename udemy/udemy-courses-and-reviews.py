import requests
import json
from requests.auth import HTTPBasicAuth

# This is the maximum results of courses that the Udemy API can return in a single GET request, that is 85
payload = {
	'page': '1',
	'page_size': '10'
}


# We are going to use HTTP Basic Authentication in order to use Udemy APIs.
basic = HTTPBasicAuth('uclPrCbXWfaAxPneidKaZNalPBLm7pA1up0JrVWX', 
	'vl1GW8gX0QOW5KtLMQsRigwInD39khdh3zIxKDR3NAMBwmTCX5EBpmLDtADtc1tyn29vMWgcPAlxmnJIxub0DCxsN9B3UrfTR8UyKUhAYfacwF6MWpXObbIXTEN8SNuc')

all_courses = []

while payload['page'] != '2':
	courses_response = requests.get(
		"https://www.udemy.com/api-2.0/courses/", 
		auth = basic, 
		timeout = 20,
		params = payload
	)

	course_response_dict = courses_response.json()
	course_results = course_response_dict['results']
	print("Course Iteration" + payload['page'])
	for course in course_results:
		
		# Course ID
		print("Course ID : " + str(course['id']))
		course_id = course['id']

		# These reviews will be maintained on a per course basis.
		all_reviews_per_course = []
		review_payload = {
			'page': '1',
			'page_size': '100'
		}

		while review_payload['page'] != '85':
			review_response = requests.get(
					"https://www.udemy.com/api-2.0/courses/" + str(course_id) + "/reviews/",
					auth = basic, 
					timeout = 20,
					params = review_payload
				)
			review_response_dict = review_response.json()
			review_results = review_response_dict['results']

			for review in review_results:
				if review['content']:
					all_reviews_per_course.append(review)

			print("Review Iteration" + review_payload['page'])

			review_payload['page'] = str(int(review_payload['page']) + 1)

			if review_response_dict['next'] is None:
				break

		# Now add a property called reviews with all the reviews for the course
		course['reviews'] = all_reviews_per_course

		# Append the course to the final result : all_courses
		all_courses.append(course)
	payload['page'] = str(int(payload['page']) + 1)

with open('udemy-courses-and-reviews.json', 'w', encoding='utf-8') as f:
    json.dump(all_courses, f, ensure_ascii=False, indent=4)

print(len(all_courses))


