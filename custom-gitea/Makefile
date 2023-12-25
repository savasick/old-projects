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
	echo $(CONTAINER_NAME);\
	echo "Gitea with docker";\
	echo "Made for docker to run commands faster";\
	echo "";\
	echo "command 'make start' to run project";\
	echo "";\
	echo "command 'make list' to show all commands";\
	echo "";\
	echo "before start look up .env and app.ini";\
	echo "";\

# print commands list
list:
	@echo "commands list:";\
	echo "make start 			to run app";\
	echo "make stop 			to stop app";\
	echo "make shell 			to run shell session at app container";\
	echo "make shell-db 			to run shell session at database container";\
	echo "make db				to run psql session at database container";\
	echo "make logs			to show logs at containers";\
	echo "make backup			to make data dump";\
	echo "make restore			to restore data from dump";

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
		sudo docker ps;\
		echo "need a while to start up";\
		echo "$(IP_ADDR):$(GIT_PORT)";\
	else\
		export DOCKER_DEFAULT_PLATFORM=linux/amd64;\
		docker-compose up -d --build;\
		docker ps;\
		echo "need a while to start up";\
		echo "$(IP_ADDR):$(GIT_PORT)"; fi

# stop container
stop:
	@if [ "$(OS_NAME)" = "linux" ]; then\
		sudo docker-compose down;\
	else\
		docker-compose down; fi

# open bash at app container
shell:
	@if [ "$(OS_NAME)" = "linux" ]; then\
		sudo docker exec -it $(CONTAINER_NAME) /bin/sh;\
	else\
		docker exec -it $(CONTAINER_NAME) /bin/sh; fi

# open bash at database container
shell-db:
	@if [ "$(OS_NAME)" = "linux" ]; then\
		sudo docker exec -it DB-$(CONTAINER_NAME) /bin/bash;\
	else\
		docker exec -it DB-$(CONTAINER_NAME) /bin/bash; fi

# run psql at container
db:
	@if [ "$(OS_NAME)" = "linux" ]; then\
		sudo docker exec -it DB-$(CONTAINER_NAME) psql -U $(POSTGRES_USER) -d $(POSTGRES_DB_NAME);\
	else\
		docker exec -it DB-$(CONTAINER_NAME) psql -U $(POSTGRES_USER) -d $(POSTGRES_DB_NAME); fi

# show logs 
logs:
	@if [ "$(OS_NAME)" = "linux" ]; then\
		sudo docker-compose -f docker-compose.yml logs -f;\
	else\
		docker-compose -f docker-compose.yml logs -f; fi

# backup data
backup:
	@if [ "$(OS_NAME)" = "linux" ]; then\
		sudo docker exec -it $(CONTAINER_NAME) su - git sh -c '/app/gitea/gitea dump -c /data/gitea/conf/app.ini';\
		echo "gitea-dump.sql store at ./gitea/git/ ";\
		echo "";\
		echo "to restore data rename gitea-dump*.zip to gitea-dump.zip, then store it at root folder and run 'make restore'";\
	else\
		docker exec -it $(CONTAINER_NAME) su - git sh -c '/app/gitea/gitea dump -c /data/gitea/conf/app.ini';\
		echo "gitea-dump.sql store at ./gitea/git/ ";\
		echo "";\
		echo "to restore data rename gitea-dump*.zip to gitea-dump.zip, then store it at root folder and run 'make restore'"; fi

# restore data from dump
restore:
	@if [ "$(OS_NAME)" = "linux" ]; then\
		sudo docker cp gitea-dump.zip $(CONTAINER_NAME):/gitea-dump.zip;\
		sudo docker exec -it $(CONTAINER_NAME) sh -c 'unzip gitea-dump.zip -d ./gitea-dump';\
		sudo docker exec -it $(CONTAINER_NAME) sh -c 'rm -rf gitea-dump.zip';\
		sudo docker exec -it $(CONTAINER_NAME) sh -c 'chown -R git:git ./gitea-dump';\
		sudo docker exec -it $(CONTAINER_NAME) sh -c 'cp -r ./gitea-dump/data/* ./data/gitea';\
		sudo docker exec -it $(CONTAINER_NAME) sh -c 'cp -r ./gitea-dump/app.ini ./data/gitea/conf/app.ini';\
		sudo docker exec -it $(CONTAINER_NAME) sh -c 'cp -r ./gitea-dump/repos/* ./data/git/repositories/';\
		sudo docker exec -it $(CONTAINER_NAME) sh -c 'chown -R git:git ./data';\
		sudo docker exec -it $(CONTAINER_NAME) su - git sh -c '/usr/local/bin/gitea -c '/data/gitea/conf/app.ini' admin regenerate hooks';\
		sudo docker cp $(CONTAINER_NAME):/gitea-dump/gitea-db.sql . ;\
		sudo docker stop $(CONTAINER_NAME);\
		sudo cat gitea-db.sql | sudo docker exec -i DB-${CONTAINER_NAME} psql -U ${POSTGRES_USER};\
		sudo docker start $(CONTAINER_NAME);\
		sudo rm -rf gitea-db.sql;\
		sudo docker exec -it $(CONTAINER_NAME) sh -c 'rm -rf ./gitea-dump';\
	else\
		docker cp gitea-dump.zip $(CONTAINER_NAME):/gitea-dump.zip;\
		docker exec -it $(CONTAINER_NAME) sh -c 'unzip gitea-dump.zip -d /gitea-dump';\
		docker exec -it $(CONTAINER_NAME) sh -c 'rm -rf gitea-dump.zip';\
		docker exec -it $(CONTAINER_NAME) sh -c 'chown -R git:git /gitea-dump';\
		docker exec -it $(CONTAINER_NAME) sh -c 'cp -r ./gitea-dump/data/* ./data/gitea';\
		docker exec -it $(CONTAINER_NAME) sh -c 'cp -r ./gitea-dump/app.ini ./data/gitea/conf/app.ini';\
		docker exec -it $(CONTAINER_NAME) sh -c 'cp -r ./gitea-dump/repos/* ./data/git/repositories/';\
		docker exec -it $(CONTAINER_NAME) sh -c 'chown -R git:git ./data';\
		docker exec -it $(CONTAINER_NAME) su - git sh -c '/usr/local/bin/gitea -c '/data/gitea/conf/app.ini' admin regenerate hooks';\
		docker cp $(CONTAINER_NAME):/gitea-dump/gitea-db.sql . ;\
		docker stop $(CONTAINER_NAME);\
		cat gitea-db.sql | docker exec -i DB-${CONTAINER_NAME} psql -U ${POSTGRES_USER};\
		docker start $(CONTAINER_NAME);\
		rm -rf gitea-db.sql;\
		docker exec -it $(CONTAINER_NAME) sh -c 'rm -rf ./gitea-dump'; fi