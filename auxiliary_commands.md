# FLASK BASED WWW with CV
-------------------------
* `pip install -r requirements.txt`.
* `flask --app main.py --debug run` - start www server on localhost:5000 wit   h debug, if file is named app.py or wsgi.py dont use --app flag.
* `flask --app main.py run --debug --host=0.0.0.0 --port=666`
* `gh repo create https://github.com/marcinszlaz/cv_www.git --public`.
* `gh repo edit --description "description"`.
* `gh repo view`.
* `git init`.
* `git branch -M main`.
* `git remote add origin https://github.com/marcinszlaz/cv_www`.
* `git push -u origin main`. 

# RUNNING APPLICATION BY GUNICORN
---------------------------------
* `gunicorn -k gevent -w 4 -b 10.215.14.30:5015 'main:app'` - without reverse proxy, on non root ports (80-443 require root privileges), main - module, app - variable in module
* `gunicorn -k gevent -w 4` when you use reverse proxy don't use -b 0.0.0.0 because that way you can bypass the proxy

# CREATING DOCKER IMAGE
------------------------
* `docker tag <image_id> cv_www:v1.0` - create image based on <imae_id> for example python:slim 3.12,
* `docker build -t cv_www:v1.x ./ ` - build new docker image "./" is important! - means current folder.
* `docker run -d --name cv_www-v1.0 --restart unless-stopped -v $(pwd)/templates:/app/templates:ro -v$(pwd)/static/:/app/static/:ro -p 10.215.14.3:5015:5015 cv_www:v1.0` - run it this way! In case of running docker container alone without nginx reverse proxy
* * `docker-compose up -d --build` - in case you run docker-compose file with reverse proxy (nginx)
* `docker-compose up -d` after first build, -d - detached,
* `docker-compose logs -f` real time logs from running containers
