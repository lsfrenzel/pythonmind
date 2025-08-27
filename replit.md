# Learning Management System (LMS)

## Overview

This is a Flask-based Learning Management System that provides a structured learning experience through modules and quizzes. The system supports both student and admin roles, with students progressing through sequential learning modules and taking quizzes to advance, culminating in a final exam.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Backend Architecture
- **Framework**: Flask web framework with SQLAlchemy ORM
- **Database**: SQLite for development with configurable database URL for production
- **Authentication**: Session-based authentication with token-based student access and admin credentials
- **Models**: User, ModuleProgress, and QuizResult entities with established relationships

### Frontend Architecture
- **Template Engine**: Jinja2 templating with Flask
- **UI Framework**: Bootstrap with dark theme and Font Awesome icons
- **Responsive Design**: Mobile-friendly interface with progress indicators and interactive elements

### Data Storage
- **Primary Database**: SQLAlchemy with DeclarativeBase for model definitions
- **Session Management**: Flask sessions for user state management
- **Data Structure**: Relational model with user progress tracking and quiz result storage

### Learning Module System
- **Sequential Learning**: Module progression requires completion of previous modules
- **Quiz System**: Each module includes multiple choice and open-answer questions
- **Progress Tracking**: Real-time progress calculation and completion status
- **Final Exam**: Comprehensive exam unlocked after completing all modules

### Authentication & Authorization
- **Student Access**: Persistent authentication with 3-month access duration
- **Admin Access**: Username/password authentication with elevated privileges
- **Role-Based Features**: Different interfaces and capabilities for students vs admins
- **Session Security**: Configurable session secrets and proxy fix middleware
- **Progress Persistence**: Student progress automatically saved and maintained for 3+ months
- **Access Management**: Automatic expiration tracking and renewal on login
- **Data Cleanup**: Automatic removal of expired user data after 30 days of expiration

## External Dependencies

### Python Packages
- **Flask**: Web framework for routing and request handling
- **Flask-SQLAlchemy**: Database ORM integration
- **Werkzeug**: Password hashing and WSGI utilities

### Frontend Libraries
- **Bootstrap**: CSS framework for responsive design
- **Font Awesome**: Icon library for UI elements
- **Custom CSS**: Progress circles and module card styling

### Configuration Dependencies
- **Environment Variables**: DATABASE_URL, SESSION_SECRET, ADMIN_TOKEN, ADMIN_PASSWORD
- **Database**: SQLite by default, configurable for other databases via DATABASE_URL
- **Deployment**: WSGI-ready with proxy fix for production deployment