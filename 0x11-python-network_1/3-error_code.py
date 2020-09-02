#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""
from urllib import request, error
import sys

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as ex:
        print('Error code: {}'.format(ex.code))
