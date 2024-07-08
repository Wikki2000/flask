#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <jwt_token>"
    exit 1
fi

jwt_token=$1

curl -X GET http://127.0.0.1:5000/protected -H "Authorization: Bearer $jwt_token"
