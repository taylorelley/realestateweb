#!/bin/bash
docker build -t realestate .
docker run -p 5000:5000 realestate
