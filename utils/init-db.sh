#! /bin/bash
alembic upgrade head
if [ ${ENVIRONMENT} = "dev" ]; then
  python3 ../helper/populate_db.py || exit 1
  echo "Successfully applied populate_db"
fi

# Keep container running
tail -f /dev/null
