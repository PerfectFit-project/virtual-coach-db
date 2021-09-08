#!/bin/bash
# Dumps the running perfectfit db to a file with name perfectfitdb + current timestamp

timestamp=$(date +%Y%m%d-%H%M%S)
dump_fname=perfectfitdb-${timestamp}.dump
echo "Dumping running db to: ${dump_fname} ..."
docker compose exec -u root db pg_dump -Fc perfectfit > ${dump_fname}
echo "...done"
