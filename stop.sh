#!/bin/bash

# Docker stop and delete image script
echo 'Docker stop script'
docker-compose down

echo '$\nDocker delete image script'
docker rmi mysql
