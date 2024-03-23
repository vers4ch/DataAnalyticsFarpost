#!/bin/bash

set -e

# Создаем базы на сервере
psql -U postgres -c "CREATE DATABASE farpost_db1"
psql -U postgres -c "CREATE DATABASE farpost_db2"

# Восстановление баз из дампов
psql -U postgres -d farpost_db1 -f /docker-entrypoint-initdb.d/farpost_db1.dump
psql -U postgres -d farpost_db2 -f /docker-entrypoint-initdb.d/farpost_db2.dump

