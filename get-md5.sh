#!/bin/bash
FILE=$1

openssl md5 -binary ${FILE} | base64 > file.md5
