#!/bin/bash
# Request to a URL. Displays only the status code of the response.
curl -so /dev/null -w "%{http_code}" "$1"
