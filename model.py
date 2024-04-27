

from main import *
class student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
class proffesor(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
class exam(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    proffesor_id = db.Column(db.Integer, db.ForeignKey('proffesor.id'), nullable=False)
    proffesor_name = db.Column(db.String(255), db.ForeignKey('proffesor.name'))
class question(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question = db.Column(db.String(255), nullable=False)
    exam_id = db.Column(db.Integer, db.ForeignKey('exam.id'), nullable=False)
    exam_name = db.Column(db.String(255), db.ForeignKey('exam.name'))
if __name__ == '__main__':
    with app.app_context():
        db.create_all()