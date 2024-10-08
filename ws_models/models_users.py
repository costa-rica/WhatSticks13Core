from .base import Base, DatabaseSession
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, \
    Date, Boolean
from itsdangerous.url_safe import URLSafeTimedSerializer#new 2023
from datetime import datetime
from flask_login import UserMixin
from .config import config
import os
from flask import current_app


def default_username(context):
    return context.get_current_parameters()['email'].split('@')[0]


class Users(Base, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    email = Column(String(255), unique = True)
    password = Column(Text)
    username = Column(Text, default=default_username)
    timezone = Column(Text, default="Etc/GMT")
    location_permission_device = Column(Boolean, default=False)# was location_permission
    location_permission_ws = Column(Boolean, default=False)# was location_reoccuring_permission
    admin_permission = Column(Boolean, default=False)
    notifications = Column(Boolean, default=False)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)
    loc_day = relationship('UserLocationDay', backref='user_loc_day', lazy=True)
    pending_user_id = relationship('PendingUsers', backref='user_pending_user_id', lazy=True)


    def get_reset_token(self):
        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        return serializer.dumps({'user_id': self.id})

    @staticmethod
    def verify_reset_token(token):
        print("--- in verify_reset_token ---")
        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        try:
            payload = serializer.loads(token, max_age=1000)
            user_id = payload.get("user_id")
        except:
            return None
        
        db_session = DatabaseSession()
        try:
            user = db_session.query(Users).get(user_id)
        finally:
            print("*** db_session closed after verify_reset_token ***")
            db_session.close()  # Ensure the session is closed after use

        # return sess.query(Users).get(user_id)
        return user

    def __repr__(self):
        return f'Users(id: {self.id}, email: {self.email}, username: {self.username}, ' \
        f'location_permission_ws: {self.location_permission_ws})'

class PendingUsers(Base):
    __tablename__ = 'pending_users'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id"))
    email = Column(String(255), unique = True)
    password = Column(Text)
    username = Column(Text, default=default_username)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)

    def __repr__(self):
        return f'PendingUsers(id: {self.id}, user_id: {self.user_id}, email: {self.email}, ' \
        f'username: {self.username}, time_stamp_utc: {self.time_stamp_utc})'


