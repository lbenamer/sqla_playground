#! /bin/bash
source .env
virtualenv --python=${PYTHON_BIN} venv
sleep 2
docker run --name sqlapp -p ${DB_PORT}:5432 -d postgres:9.6
source venv/bin/activate
python -m pip install  -r requirements.txt
python -m pip install -r ${DEPENDENCIES}
sleep 2
docker exec -u postgres sqlapp createdb ${DB_NAME}
deactivate
echo SQL Alchemy Postgres Playground succesfully installed !
bash launch.sh
