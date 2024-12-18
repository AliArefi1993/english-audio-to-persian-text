#!/bin/bash

docker-compose down
docker compose --env-file ../.dockerenv up -d

echo "Waiting 10 sec for all services to be up and ready..."
sleep 10

# Run tests
artillery run test.yml --output results.json

# Run cleanup
docker-compose down
