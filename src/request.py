#Function: this is a python script that checks to see if coverage reported from the Codecov API is accurate

import requests
import time
import os

payload = {'token': os.environ['API_KEY']}

link = 'https://codecov.io/api/gh/codecov/Python-Standard'

print("Waiting 60 seconds for report to upload before pinging API...")

#night night
time.sleep(60)

print("Pinging Codecov's API..")
#get latest coverage data
all_data = requests.get(link, params=payload).json()
commit_data = all_data['commits'][0]
coverage_percentage = commit_data['totals']['c']

print("Ensuring coverage percentage is accurate...")
#result should return 85.71429 as its coverage metric
if(coverage_percentage == os.environ['CORRECT_COVERAGE']): 
    print("Success! Codecov's API returned the correct coverage percentage, "+ os.environ['CORRECT_COVERAGE'])
    exit(0)
else:
    print("Whoops, something is wrong D: Codecov did not return the correct coverage percentage. Coverage percentage should be "+os.environ['CORRECT_COVERAGE']+" but Codecov returned "+coverage_percentage)
    exit(1)
