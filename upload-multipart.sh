#!/bin/bash

FILE=$1
BUCKET=$2
UPLOADID=$3

for i in `seq 1 20`; # 20 parts file
do
    FI=$(printf "%02d" $i)
    MD5=`openssl md5 -binary parts/part-${FI} | base64`
    echo "Uploading part $FI with MD5 $MD5"
    aws s3api upload-part --bucket ${BUCKET} --key ${FILE} --part-number $FI --body parts/part-${FI} --upload-id ${UPLOADID} --content-md5 ${MD5}
done
