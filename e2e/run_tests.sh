#!/bin/bash
docker-compose down --volumes
docker-compose up -d

mkdir -p tests_results

docker-compose exec -e BROWSER=$BROWSER test_runner ./run.sh
