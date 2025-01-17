#!/usr/bin/env bash

set -o errexit # salir si hay error

pip install -r requeriments.txt

python manage.py collectstatic --no-input
python manage.py migrate

python manage.py cargar_datos