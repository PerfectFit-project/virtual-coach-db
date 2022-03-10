#!/bin/sh
echo $PWD
alembic upgrade head
python3 ../helper/populate_db.py
