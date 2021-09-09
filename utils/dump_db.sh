#!/bin/bash
# Dumps the running perfectfit db to a file with name perfectfitdb + current timestamp

timestamp=$(date +%Y%m%d-%H%M%S)
dump_fname=perfectfitdb-${timestamp}.dump

# First check if the db is actually running by asking to dump the schema only
docker compose exec -u root db pg_dump -s perfectfit > /dev/null || { echo "dump_db.sh: Could not find running database." ; exit 1 ; }

echo "Dumping running db to: ${dump_fname} ..."
docker compose exec -u root db pg_dump -Fc perfectfit > ${dump_fname} || { echo "Error occured when dumping db. Dump file is probably bad or empty." ; exit 1 ; }
echo "...done"
