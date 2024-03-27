# DataAnalyticsFarpost

Тестовое задание Аналитика(Farpost): Python Developer

По вопросам обращаться в ТГ: @vers4ch

Используемая бд: PostgreSQL, прилагаю docker-контейнер. 
В базы были добавлены фейковые юзеры, записи и так далее, для проверки скорости. 

!!!Для тестирования скрипта рекомендую использовать пользователя: Versach, так как для него были специально созданы записи логов, комментариев.


>>
К базам прилагаю dbs.pdf, где схемы видны наглядно, а также красным цветом выделены таблицы и связи, которых не хватало для осуществления требований. Я решил добавить таблицу Comment, так как мы ссылаемся на id лога, в котором уже содержится нужная информация, что позволяет избежать дублирование данных и ускоряет процесс сборки нужной информации, избегая хранение временных значений.


Скрипт написан на Python, библа: SQLAlchemy версия: psycopg2.

**Если git не хочет или неправильно клонирует репозиторий, это может быть связано с лимитами Git LFS, файл farpost_db1.dump весит >100мб. Для этого я залил проект на Yandex Disk https://disk.yandex.ru/d/x_6TCbYBt4RBqg**


## Инструкция
```shell
git clone https://github.com/vers4ch/DataAnalyticsFarpost.git
```
### Запуск PostgreSQL
```shell
cd DataAnalyticsFarpost/postgres
```
**Соберем образ:**
Для Unix:
```shell
sudo docker build -t far-db .
```
Для Windows(на Windows не проверялось, всё писалось и тестировалось на MacOS Sonoma(Apple M1)):
```shell
docker build -t far-db .
```

Запустим контейнер(строго с этими значениями, иначе могут возникнуть проблемы со скриптом)
```shell
docker run -d --name far-db-container -e POSTGRES_PASSWORD=admin -p 5433:5432 far-db
```
### Запуск Python-скрипта
```shell
cd ..
```
```shell
pip install -r requirements.txt
```
```shell
python run.py
```
Для примера введите логин: Versach