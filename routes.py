from flask import render_template, request, redirect, url_for, flash, session, jsonify
from app import app, db
from models import User, ModuleProgress, QuizResult, ModuleVideo
from quiz_data import MODULES, FINAL_EXAM
from datetime import datetime
import json
import secrets
import string

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Check if it's admin login
        if request.form.get('login_type') == 'admin':
            username = request.form.get('username')
            password = request.form.get('password')
            
            if username == 'admin' and password == '*Frenzeltech103':
                session['is_admin'] = True
                session['user_id'] = 'admin'
                flash('Login de administrador realizado com sucesso!', 'success')
                return redirect(url_for('admin_dashboard'))
            else:
                flash('Credenciais de administrador inválidas!', 'error')
                return render_template('login.html')
        
        # Student login - first verify email/password, then token
        else:
            email = request.form.get('email')
            password = request.form.get('password')
            token = request.form.get('token')
            
            if not email or not password:
                flash('Email e senha são obrigatórios!', 'error')
                return render_template('login.html')
            
            # Check if user exists
            user = User.query.filter_by(email=email).first()
            
            if user and user.check_password(password):
                # User authenticated, now check token for course access
                if token:
                    if token == CURRENT_STUDENT_TOKEN:
                        user.has_course_access = True
                        user.update_login_time()  # Atualiza login e estende acesso por 3 meses
                        session['user_id'] = user.id
                        flash(f'Login realizado com sucesso! Acesso liberado por {user.days_until_expiry()} dias.', 'success')
                        return redirect(url_for('dashboard'))
                    else:
                        flash('Token de acesso inválido!', 'error')
                        return render_template('login.html')
                else:
                    # User authenticated but no token provided
                    if user.has_course_access and user.has_valid_access():
                        user.update_login_time()  # Atualiza login e estende acesso
                        session['user_id'] = user.id
                        flash(f'Login realizado com sucesso! Acesso válido por {user.days_until_expiry()} dias.', 'success')
                        return redirect(url_for('dashboard'))
                    elif user.has_course_access and not user.has_valid_access():
                        flash('Seu acesso ao curso expirou! Entre em contato para renovar.', 'warning')
                        return render_template('login.html')
                    else:
                        flash('Você precisa inserir o token de acesso ao curso!', 'error')
                        return render_template('login.html')
            else:
                flash('Email ou senha incorretos!', 'error')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if not email or not password or not confirm_password:
            flash('Todos os campos são obrigatórios!', 'error')
            return render_template('register.html')
        
        if password != confirm_password:
            flash('As senhas não coincidem!', 'error')
            return render_template('register.html')
        
        # Check if user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Este email já está cadastrado!', 'error')
            return render_template('register.html')
        
        # Create new user
        user = User(email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        flash('Cadastro realizado com sucesso! Agora faça o login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

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
    if not user or not user.has_course_access:
        flash('Você precisa ter acesso ao curso para ver o dashboard!', 'error')
        return redirect(url_for('login'))
    
    # Verificar se o acesso ainda é válido
    if not user.has_valid_access():
        flash('Seu acesso ao curso expirou! Entre em contato para renovar.', 'warning')
        session.clear()
        return redirect(url_for('login'))
    
    # Get user progress
    progress = user.get_progress_percentage()
    current_module = user.get_current_module()
    
    # Get module status
    modules_status = []
    for i in range(1, 10):  # 9 modules
        module_progress = ModuleProgress.query.filter_by(
            user_id=user.id, module_id=i
        ).first()
        
        quiz_result = QuizResult.query.filter_by(
            user_id=user.id, module_id=i
        ).order_by(QuizResult.taken_at.desc()).first()
        
        status = {
            'id': i,
            'title': MODULES[i]['title'],
            'description': MODULES[i]['description'],
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
                         final_exam_result=final_exam_result,
                         days_until_expiry=user.days_until_expiry(),
                         access_expires_at=user.access_expires_at)

@app.route('/module/<int:module_id>')
def module_view(module_id):
    if 'user_id' not in session or session['user_id'] == 'admin':
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    if not user or not user.has_course_access:
        flash('Você não tem acesso ao curso!', 'error')
        return redirect(url_for('login'))
    
    # Verificar se o acesso ainda é válido
    if not user.has_valid_access():
        flash('Seu acesso ao curso expirou! Entre em contato para renovar.', 'warning')
        session.clear()
        return redirect(url_for('login'))
    
    if not user.can_access_module(module_id):
        flash('Você não pode acessar este módulo ainda!', 'error')
        return redirect(url_for('dashboard'))
    
    if module_id not in MODULES:
        flash('Módulo não encontrado!', 'error')
        return redirect(url_for('dashboard'))
    
    module = MODULES[module_id]
    
    # Get video for this module
    module_video = ModuleVideo.query.filter_by(module_id=module_id).first()
    
    return render_template('module.html', 
                         module=module, 
                         module_id=module_id,
                         video=module_video)

@app.route('/quiz/<int:module_id>', methods=['POST'])
def take_quiz(module_id):
    if 'user_id' not in session or session['user_id'] == 'admin':
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    if not user or not user.has_course_access:
        flash('Você não tem acesso ao curso!', 'error')
        return redirect(url_for('login'))
    
    # Verificar se o acesso ainda é válido
    if not user.has_valid_access():
        flash('Seu acesso ao curso expirou! Entre em contato para renovar.', 'warning')
        session.clear()
        return redirect(url_for('login'))
    
    if not user.can_access_module(module_id):
        flash('Você não pode acessar este módulo ainda!', 'error')
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
        flash(f'Parabéns! Você passou com {score:.1f}%', 'success')
    else:
        flash(f'Você obteve {score:.1f}%. Precisa de 70% para avançar. Tente novamente!', 'error')
    
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
    if not user or not user.has_course_access:
        flash('Você não tem acesso ao curso!', 'error')
        return redirect(url_for('login'))
    
    # Verificar se o acesso ainda é válido
    if not user.has_valid_access():
        flash('Seu acesso ao curso expirou! Entre em contato para renovar.', 'warning')
        session.clear()
        return redirect(url_for('login'))
    
    if not user.can_take_final_exam():
        flash('Você deve completar todos os módulos antes de fazer o exame final!', 'error')
        return redirect(url_for('dashboard'))
    
    return render_template('exam.html', exam=FINAL_EXAM)

@app.route('/final-exam', methods=['POST'])
def submit_final_exam():
    if 'user_id' not in session or session['user_id'] == 'admin':
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    if not user or not user.has_course_access:
        flash('Você não tem acesso ao curso!', 'error')
        return redirect(url_for('login'))
    
    # Verificar se o acesso ainda é válido
    if not user.has_valid_access():
        flash('Seu acesso ao curso expirou! Entre em contato para renovar.', 'warning')
        session.clear()
        return redirect(url_for('login'))
    
    if not user.can_take_final_exam():
        flash('Você deve completar todos os módulos antes de fazer o exame final!', 'error')
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
        flash(f'🎉 Parabéns! Você passou no exame final com {score:.1f}%! Você ainda tem mais um passo para finalizar seu curso.', 'success')
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
    
    return render_template('admin.html', students=student_data, stats=stats, current_token=CURRENT_STUDENT_TOKEN)

@app.route('/admin/videos')
def admin_videos():
    if 'is_admin' not in session or not session['is_admin']:
        flash('Admin access required!', 'error')
        return redirect(url_for('login'))
    
    # Get all module videos
    videos = ModuleVideo.query.all()
    video_dict = {v.module_id: v for v in videos}
    
    # Create list with all modules and their video status
    modules_with_videos = []
    for i in range(1, 10):
        module_info = {
            'id': i,
            'title': MODULES[i]['title'],
            'video': video_dict.get(i),
            'has_video': i in video_dict
        }
        modules_with_videos.append(module_info)
    
    return render_template('admin_videos.html', modules=modules_with_videos)

@app.route('/admin/videos/<int:module_id>', methods=['POST'])
def update_module_video(module_id):
    if 'is_admin' not in session or not session['is_admin']:
        flash('Admin access required!', 'error')
        return redirect(url_for('login'))
    
    video_url = request.form.get('video_url', '').strip()
    video_title = request.form.get('video_title', '').strip()
    
    if not video_url:
        # Remove video if URL is empty
        existing_video = ModuleVideo.query.filter_by(module_id=module_id).first()
        if existing_video:
            db.session.delete(existing_video)
            db.session.commit()
            flash(f'Vídeo removido do Módulo {module_id}!', 'success')
    else:
        # Add or update video
        existing_video = ModuleVideo.query.filter_by(module_id=module_id).first()
        if existing_video:
            existing_video.video_url = video_url
            existing_video.video_title = video_title
            existing_video.updated_at = datetime.utcnow()
        else:
            new_video = ModuleVideo(
                module_id=module_id,
                video_url=video_url,
                video_title=video_title
            )
            db.session.add(new_video)
        
        db.session.commit()
        flash(f'Vídeo atualizado para o Módulo {module_id}!', 'success')
    
    return redirect(url_for('admin_videos'))

# Global variable to store the current student access token
CURRENT_STUDENT_TOKEN = 'frenzeltechbest'

@app.route('/admin/generate-token', methods=['POST'])
def generate_new_token():
    if 'is_admin' not in session or not session['is_admin']:
        return jsonify({'success': False, 'error': 'Admin access required'}), 403
    
    global CURRENT_STUDENT_TOKEN
    
    try:
        # Generate a new random token
        # Use a combination of letters and numbers for easy sharing
        alphabet = string.ascii_lowercase + string.digits
        new_token = ''.join(secrets.choice(alphabet) for _ in range(12))
        
        # Update the global token
        CURRENT_STUDENT_TOKEN = new_token
        
        return jsonify({
            'success': True, 
            'new_token': new_token,
            'message': f'Novo token gerado: {new_token}'
        })
        
    except Exception as e:
        return jsonify({
            'success': False, 
            'error': str(e)
        }), 500
