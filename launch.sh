#! /bin/bash
source venv/bin/activate
source .env
export PYTHONPATH="${PYTHONPATH}:${WORK_ENV}:${PWD}/src/"
cd src/notebooks
python -m jupyter notebook
