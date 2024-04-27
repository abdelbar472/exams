
from model import *



@app.route('/login', methods=['POST', 'GET'])
def login(student=None):
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
@app.route('/home'/'<int:id>', methods=['POST', 'GET'])
def home(student=None,id):
    if session.get('logged_in'):
        id = session['id']
        user = proffesor.query.filter_by(id=id).first()
        student = student.query.filter_by(id=id).first()
        if user:
            exams = exam.query.all()
            return render_template('home.html', exams=exams)
        elif student:
            exams = exam.query.all()
            return render_template('home.html', exams=exams)
    return redirect(url_for('login'))





@app.route('/exam/<int:id>', methods=['POST', 'GET'])
def exam(id):
    if 'logged_in' in session:
        user_id = session['id']
        student_user = student.query.filter_by(id=user_id).first()
        if student_user:
            if request.method == 'POST':
                question_id = request.form['question_id']
                submitted_answer = request.form['answer']
                question_obj = question.query.filter_by(id=question_id).first()
                if question_obj:
                    if question_obj.right_answer == submitted_answer:
                        session['result'] = session.get('result', 0) + 1
                    return redirect(url_for('exam', id=id))
                else:
                    return "Question not found", 404
            else:
                exams = exam.query.all()
                return render_template('exam.html', exams=exams)
        else:
            return "Unauthorized access", 403
    else:
        return "Please log in first", 401

@app.route('/result', methods=['GET'])
def result():
    if 'logged_in' in session:
        result = session.get('result', 0)
        return f"You answered {result} questions correctly."
    else:
        return "Please log in first", 401
@app.route('/addquestion', methods=['POST'])
def add_question():
    if 'logged_in' in session:
        user_id = session['id']
        user = proffesor.query.filter_by(id=user_id).first()
        if user:
            question_text = request.form['question']
            exam_id = request.form['exam_id']
            new_question = question(question=question_text, exam_id=exam_id)
            db.session.add(new_question)
            db.session.commit()
            return redirect(url_for('home'))
        else:
            return "Unauthorized access", 403
    else:
        return "Please log in first", 401

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