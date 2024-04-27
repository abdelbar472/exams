
from model import *



@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        id = request.form['id']
        password = request.form['password']
        user = proffesor.query.filter_by(id=id).first()
        student = student.query.filter_by(id=id).first()
        if user:
            if user.password == password:
                session['logged_in'] = True
                session['id'] = id
                return redirect(url_for('home'))
            else:
                return render_template('login.html', message='Invalid credentials')
        elif student:
            if student.password == password:
                session['logged_in'] = True
                session['id'] = id
                return redirect(url_for('home'))
            else:
                return render_template('login.html', message='Invalid credentials')
        else:
            return render_template('login.html', message='User not found')
    return render_template('login.html')
@app.route('/add_exam', methods=['POST', 'GET'])
def add_exam():
    if request.method == 'POST':
        name = request.form['name']
        proffesor_id = session['id']
        proffesor_name = proffesor.query.filter_by(id=proffesor_id).first().name
        exam = exam(name=name, proffesor_id=proffesor_id, proffesor_name=proffesor_name)
        db.session.add(exam)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_exam.html')
@app.route('/add_question/<int:id>', methods=['POST', 'GET'])
def add_question(id):
    if request.method == 'POST':
        question = request.form['question']
        exam_id = id
        exam_name = exam.query.filter_by(id=exam_id).first().name
        question = question(question=question, exam_id=exam_id, exam_name=exam_name)
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_question.html', id=id)
@app.route('/get_exam/<int:id>', methods=['POST', 'GET'])
def get_exam(id):
    student = student.query.filter_by(id=id).first()
    if student:
        exams = exam.query.all()
        return render_template('get_exam.html', exams=exams)
    return redirect(url_for('login'))
@app.route('addquestion/<int:id>', methods=['POST', 'GET'])
def exam_req(id, student=None):
    student = student.query.filter_by(id=id).first()
    if student:
        questions = question.query.filter_by(exam_id=id).all()
        return render_template('exam_question.html', questions=questions)
    return redirect(url_for('home'))
@app.route('/submit', methods=['POST', 'GET'])
'''
class login(Resource):
    def post(self):
        data = request.get_json()
        id = data['id']
        password = data['password']
        user = proffesor.query.filter_by(id=id).first()
        student = student.query.filter_by(id=id).first()
        if user:
            if user.password == password:
                session['logged_in'] = True
                session['id'] = id
                return {'message': 'Login successful'}, 200
            else:
                return {'message': 'Invalid credentials'}, 401
        elif student:
            if student.password == password:
                session['logged_in'] = True
                session['id'] = id
                return {'message': 'Login successful'}, 200
            else:
                return {'message': 'Invalid credentials'}, 401
        else:
            return {'message': 'User not found'}, 404


class add_exam(Resource):
    def post(self):
        data = request.get_json()
        name = data['name']
        proffesor_id = session['id']
        proffesor_name = proffesor.query.filter_by(id=proffesor_id).first().name
        exam = exam(name=name, proffesor_id=proffesor_id, proffesor_name=proffesor_name)
        db.session.add(exam)
        db.session.commit()
        return {'message': 'Exam added successfully'}, 200
class add_question(Resource):
    def post(self, id):

        data = request.get_json()
        question = data['question']
        exam_id = data['exam_id']
        exam_name = exam.query.filter_by(id=exam_id).first().name
        question = question(question=question, exam_id=exam_id, exam_name=exam_name)
        db.session.add(question)
        db.session.commit()
        return {'message': 'Question added successfully'}, 200
class get_exam(Resource):
    def get(self, id):
        student = student.query.filter_by(id=id).first()
        if student:
            exams = exam.query.all()
            exams = [{'name': exam.name, 'id': exam.id} for exam in exams]
            return {'exams': exams}, 200
        else:
            return {'message': 'Unauthorized access'}, 401

class get_question(Resource):
    def get(self, id, exam_id):
        student = student.query.filter_by(id=id).first()
        if student:
            questions = question.query.filter_by(exam_id=exam_id).all()
            questions = [{'question': question.question, 'id': question.id} for question in questions]
            return {'questions': questions}, 200
        else:
            return {'message': 'Unauthorized access'}, 401
class submit(Resource):
    def post(self):
        data = request.get_json()
        student_id = session['id']
        exam_id = data['exam_id']
        answers = data['answers']
        result = 0
        for question_id, answer in answers.items():
            question = question.query.filter_by(id=question_id).first()
            if question.answer == answer:
                result += 1
        return {'result': result}, 200
class solve(Resource):
    def get(self, id, exam_id):
        student = student.query.filter_by(id=id).first()
        if student:
            questions = question.query.filter_by(exam_id=exam_id).all()
            questions = [{'question': question.question, 'id': question.id} for question in questions]
            return {'questions': questions}, 200
        else:
            return {'message': 'Unauthorized access'}, 401
class add_student(Resource):
    def post(self):
        data = request.get_json()
        name = data['name']
        password = data['password']
        student = student(name=name, password=password, id=random.randint(1000, 9999)
        db.session.add(student)
        db.session.commit()
        return {'message': 'Student added successfully'}, 200
        '''
if __name__ == '__main__':
    app.run(debug=True)