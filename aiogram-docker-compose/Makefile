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
	echo "Aiogram with docker";\
	echo "Made for docker to run commands faster";\
	echo "";\
	echo "command 'make start' to run project";\
	echo "";\
	echo "command 'make list' to show all commands";\
	echo "";\

# print commands list
list:
	@echo "commands list:";\
	echo "make start 			to run app";\
	echo "make stop 			to stop app";\
	echo "make shell 			to run shell session at app container";\
	echo "make logs			to show logs at containers";\
	echo "make requirements		to see requirements";\

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
		sudo docker-compose ps;\
	else\
		export DOCKER_DEFAULT_PLATFORM=linux/amd64;\
		docker-compose up -d --build;\
		docker-compose ps; fi

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

# show logs 
logs:
	@if [ "$(OS_NAME)" = "linux" ]; then\
		sudo docker-compose -f docker-compose.yml logs -f;\
	else\
		docker-compose -f docker-compose.yml logs -f; fi

# show requirements
requirements:
	@cat ./requirements.txt

