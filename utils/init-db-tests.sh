#! /bin/bash
alembic upgrade head
python3 ../helper/populate_db.py
python3 ../helper/create_new_user.py
