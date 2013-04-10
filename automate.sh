#!/bin/bash
while true
do
	sleep 10
	python sync.py test:tester testing http://127.0.0.1:8080/v1/AUTH_test
done	

