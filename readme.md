# Løbefisk

## Setup for local development
Clone the repository and navigate into it.

```shell
git clone https://github.com/tskovlund/loebefisk.git
cd loebefisk
```

Modify `/loebefisk/local.sample.py` to contain your desired local settings and
rename it to `/loebefisk/local.py`. When you're done, setup your local
development environment by running the following commands: 

```shell
virtualenv -p python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
# follow the interactive creation
python manage.py runserver
```
