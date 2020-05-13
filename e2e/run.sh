#!/bin/bash
pip3 install -r requirements.txt

behave --verbose tests/features/ --junit --junit-directory tests_results
