#! /bin/bash
alembic upgrade head
if [ ${ENVIRONMENT} -eq "dev" ]; then
  python3 ../helper/populate_db.py || exit 1
fi

# Keep container running
tail -f /dev/null
