# Multipart uploader for Amazon S3

This is a simple CLI tool written in a mix of python and bash.

You need to have [aws-cli]() installed and configured (credentials available) on your system.

Tested with Python 3 on a Linux machine.

Usage:

```bash
➜  sap-downloads git:(master) ✗ ./multipart-uploader.py -h
usage: multipart-uploader.py [-h] -f FILENAME -b BUCKET

Multipart uploader for S3.

optional arguments:
  -h, --help            show this help message and exit
  -f FILENAME, --file FILENAME
                        file to upload
  -b BUCKET, --bucket BUCKET
                        bucket on s3 to store the file
```