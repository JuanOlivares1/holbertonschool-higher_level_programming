#!/bin/bash
# Request to an URL. Displays body size
curl -so /dev/null -w '%{size_download}\n' "$1"
