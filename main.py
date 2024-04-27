from flask import Flask, render_template, request, redirect, url_for,session, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import false
from importlib.resources import Resource
from sqlalchemy.testing import db
from datetime import datetime
from random import random
from datetime import timedelta
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.secret_key = '1c947b92aa43e0863c14c4ff25f07b490a1c1225a913bedc36fb3d0be862376d'  # Replace with your own secret key
app.permanent_session_lifetime = timedelta(hours=2)
db = SQLAlchemy(app)
