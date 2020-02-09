#! /bin/bash
source venv/bin/activate
export PYTHONPATH="${PYTHONPATH}:${HOME}/partoo/:${PWD}/src/"
export PARTOO_CONFIG_FILE="${HOME}/partoo/development.ini"
cd src/notebooks
python -m jupyter notebook
