#!/bin/bash

#set -x
if [ $# -ne 1 ]
then
  echo "usage: $(basename $0) <api key>"
  exit 1
fi
API_KEY="$1"

API_HOST=truesight.bmc.com
API_PATH=api/v1/meta/
#API_PATH=api/v1/entities
API_URL="https://$API_HOST/$API_PATH"

curl -s -X GET -H "X-API-KEY: $API_KEY" "$API_URL"
