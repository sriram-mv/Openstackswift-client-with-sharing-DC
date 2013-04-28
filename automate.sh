#!/bin/bash
python listobjects.py test:tester testing
python listobjects.py test:tester3 testing3
while true
do
	python sync.py test:tester testing
	sleep 8 
	python sync.py test:tester3 testing3
	sleep 8
done	

