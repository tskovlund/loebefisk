# Løbefisk

## Setup
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
