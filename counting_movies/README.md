# Counting Movies

> Based on an interview test of https://www.hackerrank.com

In this challenge, you will write an HTTP GET method to retrieve information
from a movie database. You will be given a search term, and your function
must return the value of the total field in the returned JSON object.

## Function description

Complete the function _getNumberOfMovies_. The function must return the value
of the total field in the returned JSON object.

_getNumberOfMovies_ has the following parameters:
 * _substr_: the string to search for in the movie database

It must query
https://jsonmock.hackerrank.com/api/movies/search/?Title=[substr]
and return the total number of movie titles having the substring _substr_ in
their title. The query response is a JSON object with the following five fields:
 * _page_: The current page.
 * _per_page_: The maximum number results per page.
 * _total_: The total number of movies having the substring _substr_ in their
title.
 * _total_pages_: The total number of pages which must be queried to get all
the results.
 * _data_: An array of JSON objects containing movie information where the
Title field denotes the title of the movie.

## Constrains

 * 0 < [substr] < 20

## How to execute

The input file format should contain only one line with the substring to be
queried. To execute the solution using the requests module, use:

```
$ python3 count_movies.py < input00.txt
```

to execute using the urllib module, use:

```
$ python3 count_movies2.py < input00.txt
```
