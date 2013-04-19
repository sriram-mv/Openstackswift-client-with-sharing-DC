#!/bin/bash
while true
do
	python sync.py test:tester testing 
	python sync.py test:tester3 testing3
	sleep 1
done	

