#!/bin/bash

# Build the Docker image
docker build -t realestate-api .

# Run the Docker container
docker run -p 8000:8000 realestate-api
