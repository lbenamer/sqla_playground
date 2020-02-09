#! /bin/bash
virtualenv --python=python2.7 venv
sleep 2
docker run --name sqlapp -p 5532:5432 -d postgres:9.6
source venv/bin/activate
python -m pip install  -r requirements.txt
sleep 2
docker exec -u postgres sqlapp createdb sqlapp
deactivate
echo SQL Alchemy Postgres Playground succesfully installed !
bash launch.sh
