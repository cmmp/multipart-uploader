#!/bin/bash

FILE=$1
BUCKET=$2

aws s3api create-multipart-upload --bucket ${BUCKET} --key ${FILE} --metadata md5=`cat file.md5` > initiate.json
