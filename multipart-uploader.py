#!/usr/bin/env python3

import argparse
import subprocess
import json

parser = argparse.ArgumentParser(description="Multipart uploader for S3.")
parser.add_argument(
    "-f",
    "--file",
    dest="filename",
    action="store",
    help="file to upload",
    required=True,
    type=str,
)
parser.add_argument(
    "-b",
    "--bucket",
    dest="bucket",
    action="store",
    help="bucket on s3 to store the file",
    required=True,
    type=str,
)

args = parser.parse_args()

print("Computing md5 sum of %s..." % args.filename)
subprocess.call(["./get-md5.sh", args.filename])
print("Splitting file %s..." % args.filename)
subprocess.call(["./file-split.sh", args.filename])
print("Initiating multipart upload...")
subprocess.call(["./initiate-multipart.sh", args.filename, args.bucket])
upload_id = json.loads(open("initiate.json", "r").read())["UploadId"]
print("Multipart upload created with id %s" % upload_id)
print("Uploading file parts...")
subprocess.call(["./upload-multipart.sh", args.filename, args.bucket, upload_id])
print("Completing multipart upload...")
subprocess.call(["./complete-multipart.sh", args.filename, args.bucket, upload_id])
