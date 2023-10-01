#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL and displays the body of the response.
If the HTTP status code is greater than or equal to 400,
print: Error code: followed by the value of the HTTP status code
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    response = get(argv[1])
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
