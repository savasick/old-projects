<p align="center">
    <a href="https://laravel.com">
        <img src="./help/img/laravel.png" height="168">
    </a>
</p>
laravel with docker 

#


to start
```bash
cp .env ./src
docker-compose up -d --build
docker-compose exec php composer install
docker-compose exec php php artisan key:generate
```

&
```bash
make start
```
###### look at .env file before start

>http://localhost:8000/


#

for help
```bash
make help
```
#
#### laravel v10.13.5
#### nginx:stable-alpine
#### mysql:5.7
#### php:8.1-fpm-alpine


<a href="https://laravel.com/docs/10.x/readme">docs link</a>\
<a href="https://github.com/laravel/laravel">github</a>

