"""
    tables.py
    This file defines the tables to be used in sqlalchemy of app.py
"""
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

BASE = declarative_base()


# pylint: disable=E1101
# pylint: disable=R0903
class Comment(BASE):
    """Defines the Messages table"""

    __tablename__ = "comment"
    id = Column(Integer, primary_key=True)
    tab = Column(String(50))
    name = Column(String(100))
    text = Column(String(1000))
    likes = Column(Integer)
    time = Column(DateTime(timezone=False))

    def __init__(self, text, name, tab, time):
        self.text = text
        self.name = name
        self.tab = tab
        self.likes = 0
        self.time = time

    def __repr__(self):
        return "Comment: %s, On Tab: %s" % (self.text, self.tab)


# pylint: disable=E1101
# pylint: disable=R0903
class Theme(BASE):
    """Defines the Themes table"""

    __tablename__ = "theme"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(50))
    login_type = Column(String(50))
    pattern = Column(String(50))
    value = Column(String(255))

    # pylint: disable=R0913
    def __init__(self, name, email, login_type, pattern, value):
        self.name = name
        self.email = email
        self.login_type = login_type
        self.pattern = pattern
        self.value = value

    def __repr__(self):
        return "Name: %s, Pattern: %s, Value: %s" % (
            self.name,
            self.pattern,
            self.value,
        )


class Like(BASE):
    """Defines the table for liking comments"""

    __tablename__ = "likes"
    email = Column(String(50), primary_key=True)
    login_type = Column(String(50), primary_key=True)
    comment_id = Column(Integer, ForeignKey("comment.id"), primary_key=True)

    def __init__(self, user_email, user_login_type, cid):
        self.email = user_email
        self.login_type = user_login_type
        self.comment_id = cid

    def __repr__(self):
        return "%s:%s Liked Comment %i" % (self.login_type, self.email, self.comment_id)


class FavoriteParks(BASE):
    """Define user email, login_type and favorite park ids"""

    __tablename__ = "favorite_parks"
    email = Column(String(100), primary_key=True)
    login_type = Column(String(50), primary_key=True)
    park_id = Column(String(100), primary_key=True)

    def __init__(self, email, login_type, park_id):
        self.email = email
        self.login_type = login_type
        self.park_id = park_id

    def __repr__(self):
        return "User email: %s, Login tpye: %s, park id: %s" % (
            self.email,
            self.login_type,
            self.park_id,
        )


class UserInformation(BASE):
    """ Define User to store their last input in weather widget """

    __tablename__ = "user_information"
    id = Column(Integer, autoincrement=True, primary_key=True)
    email = Column(String(100), primary_key=True)
    weather_input = Column(String(50))

    def __init__(self, email, weather_input):
        self.email = email
        self.weather_input = weather_input

    def __repr__(self):
        return "User email: %s, last input: %s" % (
            self.email,
            self.weather_input
        )
class PersonalTab(BASE):
    '''Defines the Themes table'''
    __tablename__ = 'personal_tab'
    id = Column(Integer, primary_key=True)
    email = Column(String(100))
    login_type = Column(String(50))
    personal_values = Column(String(300))

    # pylint: disable=R0913
    def __init__(self, email, login_type, personal_values):
        self.email = email
        self.login_type = login_type
        self.personal_values = personal_values

    def __repr__(self):
        return 'Name: %s, Login Type: %s, Tab Values: %s' % (
            self.name,
            self.login_type,
            self.personal_values
        )
