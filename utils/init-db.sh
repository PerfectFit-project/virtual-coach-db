#! /bin/bash
alembic upgrade head

# Keep container running
tail -f /dev/null
