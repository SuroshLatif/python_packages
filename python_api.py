# Python requests package
# Let's connect to live web using Python requests api
# We will connect to www.bbc.com and check if the web is live

# import requests
#
# responses = requests.get("http://wwww.bbc.co.uk/")
#
# def status_code_check(website):
#
#      if responses.status_code == 200:
#         print("Website up and running" + str(responses.status_code))
#     else:
#         print("OOPs something went wrong " +str(responses.status_code))
#
#
# status_code_check()




# status 200 means success and website is live and running
# status 400 or 484 means not working

# create a function called status code check
# function should return status code with appropriate message
# DRY

import requests

response = requests.get("http://wwww.bbc.co.uk/")
def check_status():
    if response: # the condition was true
    return ("Success and the status code" + str(response.status_code))
    elif response:
                print("Failure")
    elif response:
                print("OOPs something went wrong")

# requests goes one step further in simpliying this process for us
# If you use response instance in a condition expression
# It will evaluate to true if the status code was between 200-400, false otherwise
# therefore you can simplify the last example by rewriting the if statement as above


print(response.status_code)
