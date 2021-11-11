#!/bin/bash
docker compose exec -u root db psql -d perfectfit -c 'SELECT * FROM closed_user_answers'
