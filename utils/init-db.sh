#!/bin/sh
echo 'some debugging statments'
echo $PWD
ls /
ls /app
ls /app/helper
alembic upgrade head
python3 /app/helper/populate_db.py
