#!/bin/python3

import json
import requests


# Complete the function below.
def getNumberOfMovies(substr):

    #
    # This implementation uses the requests module to submit the HTTP GET
    #

    url = 'https://jsonmock.hackerrank.com/api/movies/search/'

    # set headers to handle JSON
    headers = {}
    headers['Accept'] = 'application/json'

    # Set the query parameters
    queryparam = {}
    queryparam['Title'] = substr

    # EXECUTE the HTTP requests
    response = requests.request('GET', url, headers=headers, params=queryparam)

    if response.status_code != 200:
        response.raise_for_status()

    return(json.loads(response.text)['total'])

if __name__ == '__main__':
    #f = open(os.environ['OUTPUT_PATH'], 'w')

    try:
        _substr = str(input())
    except:
        _substr = None

    res = getNumberOfMovies(_substr)
    # f.write(str(res) + "\n")
    # f.close()
    print(res)
