#!/bin/bash

FILE=$1
BUCKET=$2
UPLOADID=$3

aws s3api list-parts --bucket ${BUCKET} --key ${FILE} --upload-id ${UPLOADID} > parts.json

python3 gen_parts_file.py > parts_processed.json

aws s3api complete-multipart-upload --multipart-upload file://parts_processed.json --bucket ${BUCKET} --key ${FILE} --upload-id ${UPLOADID}
