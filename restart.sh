#! /bin/bash
docker exec -u postgres sqlapp dropdb sqlapp
sleep 2
docker exec -u postgres sqlapp createdb sqlapp
echo DB Flashed !
bash launch.sh
