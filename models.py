from app import db
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    has_course_access = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime, default=datetime.utcnow)
    access_expires_at = db.Column(db.DateTime)  # Quando o acesso expira (3 meses após último login)
    
    # Relationships
    progress = db.relationship('ModuleProgress', backref='user', lazy=True, cascade='all, delete-orphan')
    quiz_results = db.relationship('QuizResult', backref='user', lazy=True, cascade='all, delete-orphan')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def update_login_time(self):
        """Atualiza último login e estende acesso por mais 3 meses"""
        self.last_login = datetime.utcnow()
        self.access_expires_at = datetime.utcnow() + timedelta(days=90)  # 3 meses
        db.session.commit()
    
    def has_valid_access(self):
        """Verifica se o usuário ainda tem acesso válido (não expirou)"""
        if not self.access_expires_at:
            return False
        return datetime.utcnow() < self.access_expires_at
    
    def extend_access(self):
        """Estende o acesso por mais 3 meses a partir de agora"""
        self.access_expires_at = datetime.utcnow() + timedelta(days=90)
        db.session.commit()
    
    def days_until_expiry(self):
        """Retorna quantos dias restam até a expiração do acesso"""
        if not self.access_expires_at:
            return 0
        delta = self.access_expires_at - datetime.utcnow()
        return max(0, delta.days)
    
    def get_current_module(self):
        """Get the current module the user should work on"""
        completed_modules = [p.module_id for p in list(self.progress) if p.completed]
        if not completed_modules:
            return 1
        return max(completed_modules) + 1 if max(completed_modules) < 9 else 9
    
    def get_progress_percentage(self):
        """Calculate overall progress percentage"""
        completed_modules = len([p for p in list(self.progress) if p.completed])
        return (completed_modules / 9) * 100  # 9 modules total
    
    def can_access_module(self, module_id):
        """Check if user can access a specific module"""
        if module_id == 1:
            return True
        
        # Check if previous module is completed
        prev_module = ModuleProgress.query.filter_by(
            user_id=self.id, 
            module_id=module_id - 1
        ).first()
        
        return prev_module and prev_module.completed
    
    def can_take_final_exam(self):
        """Check if user can take the final exam"""
        completed_modules = len([p for p in list(self.progress) if p.completed])
        return completed_modules >= 9
    
    def __repr__(self):
        return f'<User {self.email}>'
    
    @staticmethod
    def cleanup_expired_users():
        """Remove dados de usuários com acesso expirado há mais de 30 dias"""
        from datetime import datetime, timedelta
        
        # Data limite: usuários que expiraram há mais de 30 dias
        cleanup_date = datetime.utcnow() - timedelta(days=30)
        
        # Encontrar usuários expirados há mais de 30 dias
        expired_users = User.query.filter(
            User.access_expires_at.isnot(None),
            User.access_expires_at < cleanup_date
        ).all()
        
        for user in expired_users:
            # Deletar progresso e resultados (cascade delete)
            db.session.delete(user)
        
        db.session.commit()
        return len(expired_users)

class ModuleProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    module_id = db.Column(db.Integer, nullable=False)
    completed = db.Column(db.Boolean, default=False)
    completed_at = db.Column(db.DateTime)
    
    __table_args__ = (db.UniqueConstraint('user_id', 'module_id'),)

class QuizResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    module_id = db.Column(db.Integer, nullable=True)  # NULL for final exam
    score = db.Column(db.Float, nullable=False)  # Percentage score
    total_questions = db.Column(db.Integer, nullable=False)
    correct_answers = db.Column(db.Integer, nullable=False)
    answers = db.Column(db.Text)  # JSON string of user answers
    taken_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_final_exam = db.Column(db.Boolean, default=False)
    
    def passed(self):
        return self.score >= 70.0

class ModuleVideo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    module_id = db.Column(db.Integer, nullable=False, unique=True)
    video_url = db.Column(db.String(500), nullable=False)
    video_title = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
