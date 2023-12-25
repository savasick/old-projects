# Makefile 4 crew

# import .env
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
	echo "BookShelf with docker";\
	echo "Made for docker to run commands faster";\
	echo "";\
	echo "command 'make start' to run project";\
	echo "";\
	echo "command 'make list' to show all commands";\


# print commands list
list:
	@echo "commands list:";\
	echo "make start 			to run app";\
	echo "make start-dev 			to run dev-app";\
	echo "make stop 			to stop app";\
	echo "make shell 			to run shell session at app container";\
	echo "make shell-db 			to run shell session at database container";\
	echo "make db				to run psql session at database container";\
	echo "make logs			to show logs at containers";\
	echo "make create-superuser		to create admin, to access admin panel";\
	echo "make requirements		to see requirements";\
	echo "make migrate			to migrate model to db";\
	echo "make static			to make static dir";\
	echo "make flush			to flush db";\
	echo "make create-app APP=nameapp	to start new django app";\
	echo "make backup			to backup database to file dump.sql";\
	echo "make restore			to restore data to database from file dump.sql";

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
		sudo docker-compose up -d --build;\
	else\
		export DOCKER_DEFAULT_PLATFORM=linux/amd64;\
		docker-compose up -d --build; fi

# start container
start-dev:
	@if [ "$(OS_NAME)" = "linux" ]; then\
		sudo docker-compose -f docker-compose.dev.yml up -d --build;\
	else\
		export DOCKER_DEFAULT_PLATFORM=linux/amd64;\
		docker-compose -f docker-compose.dev.yml up -d --build; fi

# stop container
stop-dev:
	@if [ "$(OS_NAME)" = "linux" ]; then\
		sudo docker-compose -f docker-compose.dev.yml down;\
	else\
		docker-compose -f docker-compose.dev.yml down; fi


# stop container
stop:
	@if [ "$(OS_NAME)" = "linux" ]; then\
		sudo docker-compose down;\
	else\
		docker-compose down; fi

# open bash at container
shell:
	@if [ "$(OS_NAME)" = "linux" ]; then\
		sudo docker exec -it $(CONTAINER_NAME) /bin/sh;\
	else\
		docker exec -it $(CONTAINER_NAME) /bin/sh; fi

# open bash at container db-git-serv
shell-db:
	@if [ "$(OS_NAME)" = "linux" ]; then\
		sudo docker exec -it DB-$(CONTAINER_NAME) /bin/bash;\
	else\
		docker exec -it DB-$(CONTAINER_NAME) /bin/bash; fi

# run psql at container
db:
	@if [ "$(OS_NAME)" = "linux" ]; then\
		sudo docker exec -it DB-$(CONTAINER_NAME) psql -U $(DB_USER) -d $(DB_DATABASE);\
	else\
		docker exec -it DB-$(CONTAINER_NAME) psql -U $(DB_USER) -d $(DB_DATABASE); fi

# show logs 
logs:
	@if [ "$(OS_NAME)" = "linux" ]; then\
		sudo docker-compose -f docker-compose.yml logs -f;\
	else\
		docker-compose -f docker-compose.yml logs -f; fi


# create admin
create-superuser:
	@if [ "$(OS_NAME)" = "linux" ]; then\
		sudo docker-compose exec web python manage.py createsuperuser;\
	else\
		docker-compose exec web python manage.py createsuperuser; fi

# show requirements
requirements:
	@cat ./app/requirements.txt

# migrate to db
migrate:
	@if [ "$(OS_NAME)" = "linux" ]; then\
		sudo docker-compose exec web python manage.py migrate;\
	else\
		docker-compose exec web python manage.py migrate; fi

# creating new migrations based
makemigrations:
	@if [ "$(OS_NAME)" = "linux" ]; then\
		sudo docker-compose exec web python manage.py makemigrations;\
	else\
		docker-compose exec web python manage.py makemigrations; fi

# flush db
flush:
	@if [ "$(OS_NAME)" = "linux" ]; then\
		sudo docker-compose exec web python manage.py flush --no-input;\
	else\
		docker-compose exec web python manage.py flush --no-input; fi

# make static dir
static:
	@if [ "$(OS_NAME)" = "linux" ]; then\
		sudo docker-compose exec web python manage.py collectstatic --no-input --clear;\
	else\
		docker-compose exec web python manage.py collectstatic --no-input --clear; fi

# start new django app
create-app:
	@if [ "$(OS_NAME)" = "linux" ]; then\
		sudo docker-compose exec web python manage.py startapp $(APP);\
		sudo chown -R $(USER):$(USER) ./app/$(APP);\
	else\
		docker-compose exec web python manage.py startapp $(APP);\
		chown -R $(USER) ./app/$(APP); fi

# to backup data from db
backup:
	@if [ "$(OS_NAME)" = "linux" ]; then\
		sudo docker exec -t DB-$(CONTAINER_NAME) pg_dumpall -c -U $(DB_USER) > dump.sql ;\
	else\
		docker exec -t DB-$(CONTAINER_NAME) pg_dumpall -c -U $(DB_USER) > dump.sql ; fi

# to restore data to db
restore:
	@if [ "$(OS_NAME)" = "linux" ]; then\
		sudo cat dump.sql | sudo docker exec -i DB-$(CONTAINER_NAME) psql -U $(DB_USER) -d $(DB_DATABASE);\
	else\
		cat dump.sql | docker exec -i DB-$(CONTAINER_NAME) psql -U $(DB_USER) -d $(DB_DATABASE); fi