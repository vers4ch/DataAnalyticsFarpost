import csv
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from models import Users, Post, Logs, Comment

# Подключение к базам данных
engine1 = create_engine('postgresql://postgres:admin@localhost:5433/farpost_db1')
engine2 = create_engine('postgresql://postgres:admin@localhost:5433/farpost_db2')

# Создание сессии для каждой базы данных
Session1 = sessionmaker(bind=engine1)
Session2 = sessionmaker(bind=engine2)
session1 = Session1()
session2 = Session2()

# Функция для получения данных для comment.csv
def generate_comments_csv(login):
        # Получаем пользователя
        user = session1.query(Users).filter_by(login=login).first()
        if user:
            # Получаем все post_id комментариев пользователя из farpost_db2
            log_ids = [log.id for log in session2.query(Logs).filter_by(author_id=user.id)]
            comment_post_ids = [comment.post_id for comment in session2.query(Comment).filter(Comment.log_id.in_(log_ids))]
            
            post_comments_count = {}
            for post_id in comment_post_ids:
                post = session1.query(Post).filter_by(id=post_id).first()
                if post:
                    header = post.header
                    author_login = session1.query(Users).filter_by(id=post.author_id).first().login
                    key = (header, author_login)
                    post_comments_count[key] = post_comments_count.get(key, 0) + 1
            
            return post_comments_count
        else:
            print("Пользователь не найден")
            return {}
        
# Функция для записи данных в comment.csv
def create_comment_csv(login):
    # Получаем данные
    post_comments_count = generate_comments_csv(login)

    # Записываем данные в CSV файл
    with open('comments.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Логин пользователя', 'Заголовок поста', 'Логин автора', 'Количество комментариев']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for (header, author_login), count in post_comments_count.items():
            writer.writerow({'Логин пользователя': login, 'Заголовок поста': header, 'Логин автора': author_login, 'Количество комментариев': count})



# Функция для general.csv     
def create_general_csv(user_login):
    user_actions = session2.query(Logs.datetime, func.count(Logs.id).filter(Logs.event_type_id == 2), func.count(Logs.id).filter(Logs.event_type_id == 5), func.count(Logs.id).filter(Logs.space_type_id == 2)).\
        filter(Logs.author_id == session1.query(Users.id).filter(Users.login == user_login).scalar()).\
        group_by(Logs.datetime).all()

    with open('general.csv', 'w', newline='') as csvfile:
        fieldnames = ['Дата', 'Количество входов на сайт', 'Количество выходов с сайта', 'Количество действий внутри блога']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for date, action_count, logout_count, blog_action_count in user_actions:
            writer.writerow({'Дата': date, 'Количество входов на сайт': action_count, 'Количество выходов с сайта': logout_count, 'Количество действий внутри блога': blog_action_count})
            


def main(user_login):
    create_comment_csv(user_login)
    create_general_csv(user_login)

if __name__ == "__main__":
    user_login = input("Введите логин пользователя: ")
    main(user_login)
