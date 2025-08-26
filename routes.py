from flask import render_template, request, redirect, url_for, flash, session, jsonify
from app import app, db
from models import User, ModuleProgress, QuizResult
from quiz_data import MODULES, FINAL_EXAM
from datetime import datetime
import json

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        token = request.form.get('token')
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Admin login
        if request.form.get('login_type') == 'admin':
            if username == 'admin' and password == app.config['ADMIN_PASSWORD']:
                session['is_admin'] = True
                session['user_id'] = 'admin'
                flash('Admin login successful!', 'success')
                return redirect(url_for('admin_dashboard'))
            else:
                flash('Invalid admin credentials!', 'error')
                return render_template('login.html')
        
        # Student login with token
        elif token:
            if token == app.config['ADMIN_TOKEN']:
                # Create or get student user
                user = User.query.filter_by(username=token).first()
                if not user:
                    user = User(username=token, email=f"{token}@student.com")
                    db.session.add(user)
                    db.session.commit()
                
                session['user_id'] = user.id
                flash('Login successful!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid token!', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session or session['user_id'] == 'admin':
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    if not user:
        return redirect(url_for('login'))
    
    # Get user progress
    progress = user.get_progress_percentage()
    current_module = user.get_current_module()
    
    # Get module status
    modules_status = []
    for i in range(1, 6):  # 5 modules
        module_progress = ModuleProgress.query.filter_by(
            user_id=user.id, module_id=i
        ).first()
        
        quiz_result = QuizResult.query.filter_by(
            user_id=user.id, module_id=i
        ).order_by(QuizResult.taken_at.desc()).first()
        
        status = {
            'id': i,
            'title': MODULES[i]['title'],
            'completed': module_progress.completed if module_progress else False,
            'accessible': user.can_access_module(i),
            'score': quiz_result.score if quiz_result else None
        }
        modules_status.append(status)
    
    # Check final exam status
    final_exam_accessible = user.can_take_final_exam()
    final_exam_result = QuizResult.query.filter_by(
        user_id=user.id, is_final_exam=True
    ).order_by(QuizResult.taken_at.desc()).first()
    
    return render_template('dashboard.html', 
                         user=user, 
                         progress=progress,
                         modules=modules_status,
                         final_exam_accessible=final_exam_accessible,
                         final_exam_result=final_exam_result)

@app.route('/module/<int:module_id>')
def module_view(module_id):
    if 'user_id' not in session or session['user_id'] == 'admin':
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    if not user or not user.can_access_module(module_id):
        flash('You cannot access this module yet!', 'error')
        return redirect(url_for('dashboard'))
    
    if module_id not in MODULES:
        flash('Module not found!', 'error')
        return redirect(url_for('dashboard'))
    
    module = MODULES[module_id]
    return render_template('module.html', module=module, module_id=module_id)

@app.route('/quiz/<int:module_id>', methods=['POST'])
def take_quiz(module_id):
    if 'user_id' not in session or session['user_id'] == 'admin':
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    if not user or not user.can_access_module(module_id):
        flash('You cannot access this module yet!', 'error')
        return redirect(url_for('dashboard'))
    
    if module_id not in MODULES:
        flash('Module not found!', 'error')
        return redirect(url_for('dashboard'))
    
    # Process quiz answers
    module = MODULES[module_id]
    questions = module['quiz']
    user_answers = {}
    correct_count = 0
    
    for i, question in enumerate(questions):
        answer_key = f'question_{i}'
        user_answer = request.form.get(answer_key, '').strip()
        user_answers[i] = user_answer
        
        if question['type'] == 'multiple_choice':
            if user_answer == question['correct_answer']:
                correct_count += 1
        elif question['type'] == 'open_answer':
            # Simple keyword matching for open answers
            correct_keywords = [kw.lower() for kw in question['correct_keywords']]
            user_words = user_answer.lower().split()
            if any(keyword in user_words for keyword in correct_keywords):
                correct_count += 1
    
    # Calculate score
    total_questions = len(questions)
    score = (correct_count / total_questions) * 100
    
    # Save quiz result
    quiz_result = QuizResult(
        user_id=user.id,
        module_id=module_id,
        score=score,
        total_questions=total_questions,
        correct_answers=correct_count,
        answers=json.dumps(user_answers)
    )
    db.session.add(quiz_result)
    
    # Update module progress if passed
    if score >= 70:
        progress = ModuleProgress.query.filter_by(
            user_id=user.id, module_id=module_id
        ).first()
        
        if not progress:
            progress = ModuleProgress(
                user_id=user.id,
                module_id=module_id
            )
            db.session.add(progress)
        
        progress.completed = True
        progress.completed_at = datetime.utcnow()
        flash(f'Congratulations! You passed with {score:.1f}%', 'success')
    else:
        flash(f'You scored {score:.1f}%. You need 70% to advance. Try again!', 'error')
    
    db.session.commit()
    
    return render_template('quiz_result.html', 
                         score=score, 
                         total_questions=total_questions,
                         correct_answers=correct_count,
                         passed=score >= 70,
                         module_id=module_id)

@app.route('/final-exam')
def final_exam():
    if 'user_id' not in session or session['user_id'] == 'admin':
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    if not user or not user.can_take_final_exam():
        flash('You must complete all modules before taking the final exam!', 'error')
        return redirect(url_for('dashboard'))
    
    return render_template('exam.html', exam=FINAL_EXAM)

@app.route('/final-exam', methods=['POST'])
def submit_final_exam():
    if 'user_id' not in session or session['user_id'] == 'admin':
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    if not user or not user.can_take_final_exam():
        flash('You must complete all modules before taking the final exam!', 'error')
        return redirect(url_for('dashboard'))
    
    # Process final exam answers
    questions = FINAL_EXAM['questions']
    user_answers = {}
    correct_count = 0
    
    for i, question in enumerate(questions):
        answer_key = f'question_{i}'
        user_answer = request.form.get(answer_key, '').strip()
        user_answers[i] = user_answer
        
        if question['type'] == 'multiple_choice':
            if user_answer == question['correct_answer']:
                correct_count += 1
        elif question['type'] == 'open_answer':
            correct_keywords = [kw.lower() for kw in question['correct_keywords']]
            user_words = user_answer.lower().split()
            if any(keyword in user_words for keyword in correct_keywords):
                correct_count += 1
    
    # Calculate score
    total_questions = len(questions)
    score = (correct_count / total_questions) * 100
    
    # Save final exam result
    exam_result = QuizResult(
        user_id=user.id,
        module_id=None,
        score=score,
        total_questions=total_questions,
        correct_answers=correct_count,
        answers=json.dumps(user_answers),
        is_final_exam=True
    )
    db.session.add(exam_result)
    db.session.commit()
    
    if score >= 70:
        flash(f'Congratulations! You passed the final exam with {score:.1f}%!', 'success')
    else:
        flash(f'You scored {score:.1f}% on the final exam. You need 70% to pass. Try again!', 'error')
    
    return render_template('quiz_result.html', 
                         score=score, 
                         total_questions=total_questions,
                         correct_answers=correct_count,
                         passed=score >= 70,
                         is_final_exam=True)

@app.route('/admin')
def admin_dashboard():
    if 'is_admin' not in session or not session['is_admin']:
        flash('Admin access required!', 'error')
        return redirect(url_for('login'))
    
    # Get all students and their progress
    students = User.query.filter_by(is_admin=False).all()
    student_data = []
    
    for student in students:
        completed_modules = len([p for p in student.progress if p.completed])
        total_score = 0
        quiz_count = 0
        
        for result in student.quiz_results:
            total_score += result.score
            quiz_count += 1
        
        avg_score = total_score / quiz_count if quiz_count > 0 else 0
        
        final_exam = QuizResult.query.filter_by(
            user_id=student.id, is_final_exam=True
        ).order_by(QuizResult.taken_at.desc()).first()
        
        student_info = {
            'user': student,
            'completed_modules': completed_modules,
            'progress_percentage': student.get_progress_percentage(),
            'avg_quiz_score': avg_score,
            'final_exam_score': final_exam.score if final_exam else None,
            'final_exam_passed': final_exam.passed() if final_exam else False
        }
        student_data.append(student_info)
    
    # Calculate statistics
    total_students = len(students)
    students_completed = len([s for s in student_data if s['completed_modules'] >= 5])
    students_passed_final = len([s for s in student_data if s['final_exam_passed']])
    
    stats = {
        'total_students': total_students,
        'completion_rate': (students_completed / total_students * 100) if total_students > 0 else 0,
        'final_exam_pass_rate': (students_passed_final / total_students * 100) if total_students > 0 else 0
    }
    
    return render_template('admin.html', students=student_data, stats=stats)
