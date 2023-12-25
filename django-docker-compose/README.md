# Django with docker-compose

Repo include `django` , `gunicorn` , `postgresql` , `nginx`

Hosted locally


# Usage

Run app:
```bash
docker-compose up -d --build
```

Run dev:
```bash
docker-compose -f docker-compose.dev.yml up -d --build
```

Logs app:
```bash
docker-compose logs
```

Down app:
```bash
docker-compose down -v
```


# Endpoints

Reachable at:\
<a href="http://localhost">localhost</a> ,
<a href="http://localhost:8000">localhost:8000</a>\
<a href="http://127.0.0.1">127.0.0.1</a> , 
<a href="http://127.0.0.1:8000">127.0.0.1:8000</a>

Admin at:\
<a href="http://localhost/admin">localhost/admin</a> ,
<a href="http://127.0.0.1/admin">127.0.0.1/admin</a>

###### login / password for admin page: <strong> admin </strong>