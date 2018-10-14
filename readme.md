# Løbefisk

## Setup for local development
Modify `/loebefisk/local.sample.py` to contain your desired local settings and
rename it to `/loebefisk/local.py`. When you're done, setup your local
development environment by running the following commands: 

```shell
git clone https://github.com/tskovlund/loebefisk.git
cd loebefisk
virtualenv -p python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
# follow the interactive creation
python manage.py runserver
```
