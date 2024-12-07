#!/bin/bash

# Check if the environment argument is passed
# $0 represents the script name
# $1 refers to the first argument
# -z if the argument ($1) has zero length

if [ -z "$1" ]; then
  echo "Usage: $0 <etl-name>"
  echo "Example: $0 etl-1 or etl-2"
  exit 1
fi

ETL=$1

# Run the main.py script with the etl
python3 src/main.py $ETL
