#!/bin/sh
echo 'some debugging statments'
echo $PWD
ls ../
ls ../helper
alembic upgrade head
python3 ../helper/populate_db.py
