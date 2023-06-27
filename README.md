# Set up the postgres database and management container.
Run the following in the directory that contains the `docker-compose.yml` file:
```
docker-compose up
```

# Applying migrations
You must deliberately apply existing migrations:
```
docker-compose exec manage_db alembic upgrade head
```

# If you want to change the database schema

## 1. Edit `models.py`
The schema is defined using `SQLAlchemy` in the `dbschema/models.py` file. You can edit this file to
describe the new database structure you want.

## 2. Generate the revision to the new schema

First make sure that all current migrations have been applied:
```
docker-compose exec manage_db alembic upgrade head
```
(You can alternatively just run the `./utils/apply_migrations.sh` script which does the same thing)

Then generate the revision to upgrade to the new schema defined in `models.py`:
```
docker-compose exec manage_db alembic revision --autogenerate
```

## 3. Apply the new revision

Finally, apply migrations again to upgrade to the latest revision:
```
docker-compose exec manage_db alembic upgrade head
```

If you want this revision to be permanent and available to others, please
remember to `git add` it to the repo. It will be found in the `dbschema/migrations/versions/`
directory. Use `git status` to see which files in there are new.


# Checking the schema of the currently running database
You can use the running `manage_db` container to execute other checks on the
postgres db. For example, you can print out the database metadata:
```
docker-compose exec manage_db python3 print_schema.py
```

# Adding new users to the db
Currently this is handled by running a script in the [onboarding/ dir of the virtual-coach-server repo](https://github.com/PerfectFit-project/virtual-coach-server/tree/main/onboarding). See the README there for instructions on using it.

# Populate db with test data
Important: The database docker-compose must be up and running with all migrations applied, as described above, 
BEFORE running any of the following steps.

Once the db is up and running, you can use:
`python helper/populate_db.py`
to populate the database with sample user data.

NB: The database will use the environment variable specified in the docker-compose file:
- DATABASE_URL = the endpoint of the database (default: postgresql+psycopg2://root:root@db/perfectfit)
- TEST_USER_ID = the user id that will be used to populate the data (default: 41482)

## Updating the test data
**When you updated the db models, you must also update the `helper/populate_db.py` script 
to match the new schema.**

NB: Follow these steps to repopulate a fresh database:
1. Stop the running containers: `docker-compose down`
2. Run containers: `docker-compose up`
3. Apply migrations: `./utils/apply_migrations.sh`
4. Populate database: `python helper/populate_db.py`

## See contents of USERS table
`./utils/print_all_users.sh` will print out all the info currently stored in the (running) db's USERS table.

# Using the python package, `virtual_coach_db`
For development purposes, you can install this python package using pip, from the repo root directory:
```
pip install .
```
Note: Do not use development mode (i.e. `pip install -e .`) as it does not resolve the namespace correctly and you will get errors like `ModuleNotFoundError: No module named 'virtual_coach_db'`.

Alternatively, if you just want to use it (e.g. in a Dockerfile) then add it to your requirements.txt using the most updated version:
```
git+https://github.com/PerfectFit-project/virtual-coach-db#v0.1.0
```

Note that when installing it in a Dockerfile on Windows, you may need to install further requirements to be able to install the required psycopg2 package in the Dockerfile (e.g. libpq-dev). Also note that if your database runs on localhost, the database cannot be reached via localhost from inside a Docker container on Windows. Use host.docker.internal from inside a Docker container to connect to the database on localhost instead.

# New versions release
When a new version of the niceday_client package is ready and tested, a [new relase has to be created together with release notes](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository). The release name has to follow the semantic versioning convention.


# Sources

## Activities (activities.csv)

Albers, N., Neerincx, M. A., Penfornis, K. M., & Brinkman, W. P. (2022). Users’ needs for a digital smoking cessation application and how to address them: A mixed-methods study. PeerJ, 10, e13824.

De StopCoach (https://www.trimbos.nl/aanbod/interventies/de-stopcoach/).

Michie, S., Ashford, S., Sniehotta, FalkoF., Dombrowski, StephanU., Bishop, A., & French, DavidP. (2011). A refined taxonomy of behaviour change techniques to help people change their physical activity and healthy eating behaviours: The CALO-RE taxonomy. Psychology & Health, 26(11), 1479–1498. https://doi.org/10.1080/08870446.2010.540664

Michie, S., Brown, J., Geraghty, A. W., Miller, S., Yardley, L., Gardner, B., ... & West, R. (2012). Development of StopAdvisor: a theory-based interactive internet-based smoking cessation intervention. Translational behavioral medicine, 2(3), 263-275.


### Educational Activities

#### Websites, Videos, Other Online Material

https://www.cdc.gov/tobacco/campaign/tips/quit-smoking/7-common-withdrawal-symptoms/index.html

https://www.dailysabah.com/life/2020/02/05/what-happens-to-your-body-after-you-quit-smoking-a-timeline

https://exerciseright.com.au/body-reacts-to-exercise/

Ikstopnu.nl

https://www.ikstopnu.nl/bibliotheek/ontwenningsverschijnselen/#krijg-je-altijd-ontwenningsverschijnselen 

https://www.ikstopnu.nl/bibliotheek/roken-en-stress/#ik-wil-stoppen-met-roken

https://www.jellinek.nl/vraag-antwoord/wat-zijn-de-effecten-van-nicotine/

https://jongvolwassenen.ikstopnu.nl/roken-en-stress/roken-om-stress-te-verminderen-werkt-averechts/ 

https://www.nuffieldhealth.com/article/what-are-the-effects-of-exercise-over-time

https://shapescale.com/blog/fitness/exercising/how-your-body-changes-once-you-start-exercising/

https://www.stichtingstopbewust.nl/stoppen-met-roken-conditie/

trimbos.nl

www.voedingscentrum.nl

https://apps.who.int/iris/bitstream/handle/10665/337001/9789240014886-eng.pdf

https://www.who.int/news-room/fact-sheets/detail/physical-activity 

https://www.youtube.com/watch?v=RAfoWVy6XhM


#### Papers

Bjørngaard, J. H., Nordestgaard, A. T., Taylor, A. E., Treur, J. L., Gabrielsen, M. E., Munafo, M. R., ... & Davey Smith, G. (2017). Heavier smoking increases coffee consumption: findings from a Mendelian randomization analysis. International journal of epidemiology, 46(6), 1958-1967.

Caddick, Z. A., Gregory, K., Arsintescu, L., & Flynn-Evans, E. E. (2018). A review of the environmental parameters necessary for an optimal sleep environment. Building and environment, 132, 11-20.

Chellappa, S. L., Steiner, R., Oelhafen, P., Lang, D., Götz, T., Krebs, J., & Cajochen, C. (2013). Acute exposure to evening blue‐enriched light impacts on human sleep. Journal of sleep research, 22(5), 573-580.

Grgic, J., Grgic, I., Pickering, C., Schoenfeld, B. J., Bishop, D. J., & Pedisic, Z. (2020). Wake up and smell the coffee: caffeine supplementation and exercise performance—an umbrella review of 21 published meta-analyses. British journal of sports medicine, 54(11), 681-688.

Hughes, J. R., & Kalman, D. (2006). Do smokers with alcohol problems have more difficulty quitting?. Drug and alcohol dependence, 82(2), 91-102.

Jaehne, A., Loessl, B., Bárkai, Z., Riemann, D., & Hornyak, M. (2009). Effects of nicotine on sleep during consumption, withdrawal and replacement therapy. Sleep medicine reviews, 13(5), 363-377.

King, A. C., Pruitt, L. A., Woo, S., Castro, C. M., Ahn, D. K., Vitiello, M. V., ... & Bliwise, D. L. (2008). Effects of moderate-intensity exercise on polysomnographic and subjective sleep quality in older adults with mild to moderate sleep complaints. The Journals of Gerontology Series A: Biological Sciences and Medical Sciences, 63(9), 997-1004.

Martins, G. L., Guilherme, J. P. L. F., Ferreira, L. H. B., de Souza-Junior, T. P., & Lancha Jr, A. H. (2020). Caffeine and exercise performance: possible directions for definitive findings. Frontiers in sports and active living, 202.

Prosise, G. L., Bonnet, M. H., Berry, R. B., & Dickel, M. J. (1994). Effects of abstinence from smoking on sleep and daytime sleepiness. Chest, 105(4), 1136-1141.

Swanson, J. A., Lee, J. W., Hopp, J. W., & Berk, L. S. (1997). The impact of caffeine use on tobacco cessation and withdrawal. Addictive behaviors, 22(1), 55-68.

Thomas, D. T., Erdman, K. A., & Burke, L. M. (2016). Nutrition and athletic performance. Med Sci Sports Exerc, 48(3), 543-568.


### Motivational-Self-Efficacy Activities

#### Websites, Videos, Other Online Material

https://www.stichtingstopbewust.nl/


#### Papers

Johnson, Adrienne L., Tanya R. Schlam, Timothy B. Baker, and Megan E. Piper. “Understanding What Changes Adults in a Smoking Cessation Study Believe They Need to Make to Quit Smoking: A Qualitative Analysis of Pre- and Post-Quit Perceptions.” Psychology of Addictive Behaviors, June 23, 2022. https://doi.org/10.1037/adb0000856.

Knowles, Ruth Dailey. Positive Self-Talk. AJN, American Journal of Nursing 81(3):p 535, March 1981.

Lunenburg, F. C. (2011). Goal-setting theory of motivation. International journal of management, business, and administration, 15(1), 1-6.

McCaul, K. D., Hockemeyer, J. R., Johnson, R. J., Zetocha, K., Quinlan, K., & Glasgow, R. E. (2006). Motivation to quit using cigarettes: a review. Addictive behaviors, 31(1), 42-56.

Meijer, E., Gebhardt, W. A., van Laar, C., van den Putte, B., & Evers, A. W. (2018). Strengthening quitter self-identity: An experimental study. Psychology & health, 33(10), 1229-1250.

Priebe, C. S., Atkinson, J., & Faulkner, G. (2017). Run to Quit: An evaluation of a scalable physical activity-based smoking cessation intervention. Mental Health and Physical Activity, 13, 15-21

Sejati, A., & Djanah, S. N. (2020, February). Literature Review Study: Supporting and Inhibiting Factors of the Success to Stop Smoking. In 4th International Symposium on Health Research (ISHR 2019) (pp. 18-23). Atlantis Press.


### Practical Activities

#### Websites, Videos, Other Online Material

fietsnetwerk.nl

heart.org

https://www.kenniscentrumsportenbewegen.nl/producten/beweegrichtlijnen/

https://www.nhs.uk/live-well/exercise/exercise-health-benefits/

runnersmap.nl

https://sport.nl/sportclub-overzichtspagina

https://sport.nl/sportwijzer

supportervanallehardlopers.nl/hardloopplanner/start

wandel.nl


#### Papers

Cropley, M., Ussher, M., & Charitou, E. (2007). Acute effects of a guided relaxation routine (body scan) on tobacco withdrawal symptoms and cravings in abstinent smokers. Addiction, 102(6), 989-993.

Dickson-Spillmann, M., Haug, S., & Schaub, M. P. (2013). Group hypnosis vs. relaxation for smoking cessation in adults: a cluster-randomised controlled trial. BMC Public Health, 13, 1-9.

Gardner, B., Smith, L., Lorencatto, F., Hamer, M., & Biddle, S. J. (2016). How to reduce sitting time? A review of behaviour change strategies used in sedentary behaviour reduction interventions among adults. Health psychology review, 10(1), 89-112.

Hagger, M. S. (2019). Habit and physical activity: Theoretical advances, practical implications, and agenda for future research. Psychology of Sport and Exercise, 42, 118-129.

Holden, S. S., Zlatevska, N., & Dubelaar, C. (2016). Whether smaller plates reduce consumption depends on who’s serving and who’s looking: a meta-analysis. Journal of the Association for Consumer Research, 1(1), 134-146.

Limsanon, T., & Kalayasiri, R. (2015). Preliminary effects of progressive muscle relaxation on cigarette craving and withdrawal symptoms in experienced smokers in acute cigarette abstinence: a randomized controlled trial. Behavior Therapy, 46(2), 166-176.

Shahab, L., Sarkar, B. K., & West, R. (2013). The acute effects of yogic breathing exercises on craving and withdrawal symptoms in abstaining smokers. Psychopharmacology, 225, 875-882.


### Reinforcement-reward activities

#### Websites, Videos, Other Online Material

Ikstopnu.nl

https://positivepsychology.com/journaling-for-mindfulness/ 

Trimbos.nl 


#### Papers

Seligman, M. E., Steen, T. A., Park, N., & Peterson, C. (2005). Positive psychology progress: empirical validation of interventions. American psychologist, 60(5), 410.


### Self-Related Activities

#### Websites, Videos, Other Online Material

https://www.ikstopnu.nl/

https://www.ikstopnu.nl/motivatie/5x-een-mooier-uiterlijk/#handen

https://www.rokeninfo.nl/hulp/stoppen-roken-vrienden

https://www.stichtingstopbewust.nl/stoppen-met-roken-gevolgen-uiterlijk/


#### Papers

Mercken, L., Candel, M., Van Osch, L., & de Vries, H. (2011). No smoke without fire: The impact of future friends on adolescent smoking behaviour. British journal of health psychology, 16(1), 170-188.


## Testimonials (testimonials_with_user_data.csv)

Albers, N., Hizli, B., Scheltinga, B. L., Meijer, E., & Brinkman, W. P. (2023). Setting physical activity goals with a virtual coach: vicarious experiences, personalization and acceptance. Journal of Medical Systems, 47(1), 15.

Hizli, B., Albers, N., & Brinkman, W.-P. (2022). Data and code underlying the master thesis: Goal-setting dialogue for physical activity with a virtual coach (Version 1) [Data set]. 4TU.ResearchData. https://doi.org/10.4121/20047328.V1
