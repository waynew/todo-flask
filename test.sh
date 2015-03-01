#!/bin/sh
coverage run --source todo setup.py test
coverage report -m
