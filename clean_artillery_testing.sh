#!/bin/bash

docker compose up -d

# sleep to be sure all services are up and ready
sleep 10

# Run tests
artillery run test.yml

# Run cleanup
docker-compose down
