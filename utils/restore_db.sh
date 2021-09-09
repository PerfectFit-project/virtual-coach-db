#!/bin/bash
# Restores the (presumably) running db from the specified dump file

if [ "$#" -ne 1 ]; then
    echo "Usage: ./restore_db.sh DUMPFILENAME"
    exit 1
fi
dump_fname=$1

echo "Restoring db state from: ${dump_fname} ..."
docker compose exec -T -u root db pg_restore -c -d perfectfit < ${dump_fname} || { echo "Error occured when trying to restore db from dump. Is db running?" ; exit 1 ; }
echo "...done"
