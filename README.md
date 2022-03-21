# nginx-django-react-boilerplate
It is Django + React + Nginx + LetsEncrypt + PostgreSQL + Redis + Celery + Telegram Bot application.
I used https://github.com/saasitive/django-react-boilerplate and made some improvements.
# Dev Project Setup
1.  ```git clone``` via ssh
2. Install docker и docker-compose by this tutorials:
- https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-ru
- https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04-ru
3. Start project via command
```./bin/dev```
4. After succesful start up, on address ```localhost``` you must see project main page, also you must go to ```localhost/api``` and
```localhost/admin```, and make sure you see drf and django.
5. Go to path frontend and run ```npm i```, you must run this locally, not in docker.
6. Run ```nmp start``` frontend path. Go to ```localhost:3000``` make sure that you see project main page. During dev you must work with frontend on this address, because ```localhost``` will not change when you made changes in code,  ```localhost:3000``` will change, cause it has webpack

# Prod Project Setup
1. First of all you need change test.domain to your domain in all project files.
2. Run ```./init-letsencrypt.sh``` and make sure you don't have any errors
3. Change staging to 0 in init-letsencrypt.sh on line 12
4. Run ```./init-letsencrypt.sh``` and wait untill you get ssl
5. Stop all docker containers
6. Start project via command
```./bin/dev```

# Bin files
- ```./bin/dev``` - dev start up
- ```./bin/lint``` - linters
- ```./bin/manage``` - alias for python3 manage.py, accepts arguments
- ```./bin/shell``` - alias for python3 manage.py shell
- ```./bin/prod``` - prod start up
