from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

#farpost_db1
class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    login = Column(String)
    email = Column(String)

    blogs = relationship("Blog", back_populates="owner")


class Blog(Base):
    __tablename__ = 'blog'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship("Users", back_populates="blogs")
    posts = relationship("Post", back_populates="blog")


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    header = Column(String)
    text = Column(String)
    author_id = Column(Integer, ForeignKey('users.id'))
    blog_id = Column(Integer, ForeignKey('blog.id'))

    author = relationship("Users")
    blog = relationship("Blog", back_populates="posts")
    




#farpost_db2
class EventType(Base):
    __tablename__ = 'event_type'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class SpaceType(Base):
    __tablename__ = 'space_type'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Logs(Base):
    __tablename__ = 'logs'
    id = Column(Integer, primary_key=True)
    datetime = Column(Date)
    author_id = Column(Integer, ForeignKey('users.id'))
    space_type_id = Column(Integer, ForeignKey('space_type.id'))
    event_type_id = Column(Integer, ForeignKey('event_type.id'))

    author = relationship("Users")
    space_type = relationship("SpaceType")
    event_type = relationship("EventType")
    comments = relationship("Comment")

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    log_id = Column(Integer, ForeignKey('logs.id'))
    post_id = Column(Integer)
    text = Column(Text)

    log = relationship("Logs", back_populates="comments")

