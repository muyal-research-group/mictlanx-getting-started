#!/bin/bash

curl --request POST \
  --url http://localhost:60666/api/v4/elastic/async \
  --header 'Content-Type: application/json' \
  --data '{
  "rtype": "PEER",
  "rf": 2,
  "memory": 4000000000,
  "disk": 40000000000,
  "workers": 2,
  "protocol": "http",
  "strategy": "ACTIVE"
 
}'