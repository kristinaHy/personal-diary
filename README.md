# Personal Diary

A simple web application for managing your personal diary. This project allows users to record, organize, and manage their daily entries in a secure and user-friendly way.

---

## Features

- **Secure Login**: User authentication to ensure privacy.
- **Diary Entries**: Add, edit, and delete daily entries.
- **Rich Text Editor**: Write your diary entries with a built-in editor for better formatting.
- **Search Functionality**: Easily find entries by keywords or dates.
- **Responsive Design**: Access your diary from any device, including desktop, tablet, and mobile.

---

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript (React.js optional)
- **Backend**: Python (Django)
- **Database**: SQLite or PostgreSQL
- **Version Control**: Git & GitHub
- **Deployment**: Docker, AWS, or Heroku

---

## Installation

### Prerequisites
- Python
- Git installed on your system
- Virtual environment (optional but recommended)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/personal-diary.git
   cd personal-diary
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000
   ```

---

