# Set up the postgres database and management container.
Run the following in the directory that contains the `docker-compose.yml` file:
```
docker-compose up
```

# Applying migrations
You must deliberately apply existing migrations:
```
docker-compose exec manage alembic upgrade head
```

# If you want to change the database schema

## 1. Edit `models.py`
The schema is defined using `SQLAlchemy` in the `dbschema/models.py` file. You can edit this file to
describe the new database structure you want.

## 2. Generate the revision to the new schema

First make sure that all current migrations have been applied:
```
docker-compose exec manage alembic upgrade head
```
(You can alternatively just run the `./utils/apply_migrations.sh` script which does the same thing)

Then generate the revision to upgrade to the new schema defined in `models.py`:
```
docker-compose exec manage alembic revision --autogenerate
```

## 3. Apply the new revision

Finally, apply migrations again to upgrade to the latest revision:
```
docker-compose exec manage alembic upgrade head
```

If you want this revision to be permanent and available to others, please
remember to `git add` it to the repo. It will be found in the `dbschema/migrations/versions/`
directory. Use `git status` to see which files in there are new.


# Checking the schema of the currently running database
You can use the running `manage` container to execute other checks on the
postgres db. For example, you can print out the database metadata:
```
docker-compose exec manage python3 print_schema.py
```

# Adding new users to the db
Currently this is handled by running a script in the [onboarding/ dir of the virtual-coach-server repo](https://github.com/PerfectFit-project/virtual-coach-server/tree/main/onboarding). See the README there for instructions on using it.

# Backup and restore the db
Important: The database docker-compose must be up and running with all migrations applied, as described above, BEFORE running any of the following steps.

## Backup
In this repo you will find the `dump_db.sh` and `restore_db.sh` utility scripts. To create a backup of the currently running db,
run:
`./utils/dump_db.sh`
This will produce a dump of the full database contents to a file with a name of the form 'perfectfitdb-[TS]' where [TS] is the current timestamp.

## Restore
To reset the db contents to that in one of these dumps, run e.g.
`./utils/restore_db.sh my_previous_backup.dump`

## See contents of USERS table
`./utils/print_all_users.sh` will print out all the info currently stored in the (running) db's USERS table.

## Load test data
Once the db is up and running, you can use:
`./utils/restore_db.sh test.dump`
to populate the database with sample user data.

# Using the python package, `virtual_coach_db`
For development purposes, you can install this python package using pip, from the repo root directory:
```
pip install .
```
Note: Do not use development mode (i.e. `pip install -e .`) as it does not resolve the namespace correctly and you will get errors like `ModuleNotFoundError: No module named 'virtual_coach_db'`.

Alternatively, if you just want to use it (e.g. in a Dockerfile) then add it to your requirements.txt:
```
git+https://github.com/PerfectFit-project/virtual-coach-db
```

Note that when installing it in a Dockerfile on Windows, you may need to install further requirements to be able to install the required psycopg2 package in the Dockerfile (e.g. libpq-dev). Also note that if your database runs on localhost, the database cannot be reached via localhost from inside a Docker container on Windows. Use host.docker.internal from inside a Docker container to connect to the database on localhost instead.
