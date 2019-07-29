#!/bin/python3

import sys
import os
from urllib.request import Request
from urllib.request import urlopen
from urllib.error import URLError
import json


# Complete the function below.
def getNumberOfMovies(substr):
    #
    # This implementation uses the urllin module to submit the HTTP GET

    url = 'https://jsonmock.hackerrank.com/api/movies/search/'

    # set headers to handle JSON
    headers = {}
    headers['Accept'] = 'application/json'

    # Set the query parameters
    url += '?Title=' + substr

    # EXECUTE the HTTP requests
    req = Request(url, headers=headers)
    response = urlopen(req)

    return(json.loads(response.read())['total'])

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
