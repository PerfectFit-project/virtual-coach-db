#!/bin/bash
docker compose exec -u root db psql -d perfectfit -c 'SELECT * FROM USERS'
