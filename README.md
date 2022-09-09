# DRYADE_API

DRYADE API ZEN AREA FOR TESTING AND HAVE FUN WITH DJANGO

## Basic Commands

``` bash
    alias dryade_migrate="docker-compose -f local.yml run --rm django python manage.py migrate"
    alias dryade_migrations="docker-compose -f local.yml run --rm django python manage.py makemigrations"
    alias dryade_superuser="docker-compose -f local.yml run --rm django python manage.py createsuperuser"
    alias dryade_pytest="docker-compose -f local.yml run --rm django pytest"
    alias dryade_run="docker-compose -f local.yml run --rm"
    alias dryade_exec="docker-compose -f local.yml exec"
    alias dryade_backup="docker-compose -f local.yml exec postgres backup"
    alias dryade_restore="docker-compose -f local.yml exec postgres restore"
    alias dryade_up="docker-compose -f local.yml up"
    alias dryade_down="docker-compose -f local.yml down"
    alias dryade_build="docker-compose -f local.yml up --build"
    alias dryade_debug="docker-compose -f local.yml run --rm --service-ports django"
    alias dryade_docs="docker-compose -f local.yml up docs"
    alias dryade_coverage="docker-compose -f local.yml run --rm django coverage run -m pytest"
    alias dryade_coverage_report="docker-compose -f local.yml run --rm django coverage report"
    alias dryade_coverage_html="docker-compose -f local.yml run --rm django coverage html"
    alias dryade_shell_plus="docker-compose -f local.yml run --rm django python manage.py shell_plus"
```

Run this commande after Migrations

``` bash
    sudo chmod -R 777 dryade_api/orders
```
