FROM postgres:latest

# Копируем скрипт
COPY restore_databases.sh /docker-entrypoint-initdb.d/restore_databases.sh

# Копируем дампы баз в каталог /docker-entrypoint-initdb.d/
COPY ./farpost_db1.dump /docker-entrypoint-initdb.d/farpost_db1.dump
COPY ./farpost_db2.dump /docker-entrypoint-initdb.d/farpost_db2.dump

# Устанавливаем права на выполнение для скрипта
RUN chmod +x /docker-entrypoint-initdb.d/restore_databases.sh
