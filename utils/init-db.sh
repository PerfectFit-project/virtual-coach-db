#!/bin/sh
echo 'some debugging statments'
echo $PWD
echo 'new line endings'
ls /
ls /app
ls /app/helper
echo 'old line endings'
ls /
ls /app
ls /app/helper
alembic upgrade head
python3 /app/helper/populate_db.py
