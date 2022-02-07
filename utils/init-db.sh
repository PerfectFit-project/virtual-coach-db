#! /bin/bash
alembic upgrade head
python3 ../helper/populate_db.py