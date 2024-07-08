#!/bin/bash

if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage: $0 <username> <password>"
    exit 1
fi

username=$1
password=$2

curl -X POST http://127.0.0.1:5000/login -H "Content-Type: application/json" -d "{\"username\":\"$username\",\"password\":\"$password\"}"
