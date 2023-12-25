# Makefile 4 crew

# import .env.dev
ifneq (,$(wildcard ./.env))
    include .env
    export
endif

G='\033[0;32m'
NC='\033[0m'

# It ain't much, but it's honest work
.PHONY: help
help:
	@echo  ${G};\
	echo '       7JJ.        .YJ7       ';\
	echo '       ^!!^::    ::^!!^       ';\
	echo '          7PP^  ^PP7          ';\
	echo ' JYJ   7YJ5PP5JJ5PP5JY7   JYJ ';\
	echo ' 5P5   JPP7^^JPP?^^7PPJ   5P5 ';\
	echo ' Y5J   JPP.  ~PP~  .PPJ   J5Y ';\
	echo '    Y555555YY5555YY555555Y    ';\
	echo '    ^^^YPPPPPPPPPPPPPPY^^^    ';\
	echo '       7YY555YYYY555YY7       ';\
	echo '          ?PP^  ^PP7          ';\
	echo '       ^!!^::    ::^!!^       ';\
	echo '       7YY.        .YY7       ';\
	echo ${NC};\
	echo $(CONTAINER_NAME);\
	echo "Laravel with docker";\
	echo "Made for docker to run commands faster";\
	echo "";\
	echo "command 'make start' to run project";\
	echo "";\
	echo "command 'make list' to show all commands";\
	echo "";\
	echo "before start look up .env";\
	echo "";\

# print commands list
list:
	@echo "commands list:";\
	echo "make start 			to run app";\
	echo "make stop 			to stop app";\
	echo "make shell 			to run shell session at app container";\
	echo "make shell-db 			to run shell session at database container";\
	echo "make shell-server		to run shell session at nginx container";\
	echo "make db				to run mysql session at database container";\
	echo "make logs			to show logs at containers";\
	echo "make tinker			to run artisan console";\
	echo "make migrate			to migrate model to db"

# var os name
OS_NAME := $(shell uname -s | tr A-Z a-z)
# var architecture type
OS_PROC := $(shell uname -m | tr A-Z a-z)

# print os & proc type
os:
	@echo $(OS_NAME);\
	echo $(OS_PROC);

# start container
start:
	@if [ "$(OS_NAME)" = "linux" ]; then\
		cp .env ./src;\
		sudo docker-compose up -d --build;\
		sudo docker-compose exec php composer install;\
		sudo docker-compose exec php php artisan key:generate;\
		sudo docker-compose ps;\
	else\
		export DOCKER_DEFAULT_PLATFORM=linux/amd64;\
		cp .env ./src;\
		docker-compose up -d --build;\
		docker-compose exec php composer install;\
		docker-compose exec php php artisan key:generate;\
		docker-compose ps; fi

# stop container
stop:
	@if [ "$(OS_NAME)" = "linux" ]; then\
		sudo docker-compose down;\
	else\
		docker-compose down; fi

# open shell at container
shell:
	@if [ "$(OS_NAME)" = "linux" ]; then\
		sudo docker exec -it php-$(CONTAINER_NAME) /bin/sh;\
	else\
		docker exec -it php-$(CONTAINER_NAME) /bin/sh; fi

# open bash at container database
shell-db:
	@if [ "$(OS_NAME)" = "linux" ]; then\
		sudo docker exec -it mysql-$(CONTAINER_NAME) /bin/bash;\
	else\
		docker exec -it mysql-$(CONTAINER_NAME) /bin/bash; fi

# open sh at container nginx
shell-server:
	@if [ "$(OS_NAME)" = "linux" ]; then\
		sudo docker exec -it nginx-$(CONTAINER_NAME) /bin/sh;\
	else\
		docker exec -it nginx-$(CONTAINER_NAME) /bin/sh; fi

# run mysql at container
db:
	@if [ "$(OS_NAME)" = "linux" ]; then\
		sudo docker exec -it mysql-$(CONTAINER_NAME) mysql -h ${DB_HOST} -P 3306 --protocol=tcp -u ${DB_USERNAME} --password=${DB_PASSWORD};\
	else\
		docker exec -it mysql-$(CONTAINER_NAME) mysql -h ${DB_HOST} -P 3306 --protocol=tcp -u ${DB_USERNAME} --password=${DB_PASSWORD}; fi

# show logs 
logs:
	@if [ "$(OS_NAME)" = "linux" ]; then\
		sudo docker-compose -f docker-compose.yml logs -f;\
	else\
		docker-compose -f docker-compose.yml logs -f; fi

# migrate model to db
migrate:
	@if [ "$(OS_NAME)" = "linux" ]; then\
		sudo docker-compose exec php php artisan migrate;\
	else\
		docker-compose exec php php artisan migrate; fi

# artisan console
tinker:
	@if [ "$(OS_NAME)" = "linux" ]; then\
		sudo docker-compose exec php php artisan tinker;\
	else\
		docker-compose exec php php artisan tinker; fi