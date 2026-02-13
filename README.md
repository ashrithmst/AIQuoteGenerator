# AI Quote Generator 🎯

A beginner-friendly Django web application that displays random motivational and inspirational quotes.

## 🚀 Features
- Displays a random quote on each refresh
- Admin panel to add new quotes
- Clean and simple UI
- Built using Django framework

## 🛠️ Tech Stack
- Python
- Django
- HTML
- CSS
- SQLite (default Django database)

## 📌 How It Works
- Quotes are stored in the database.
- Each time the homepage loads, a random quote is selected and displayed.
- Admin users can add new quotes through Django Admin Panel.

## 🔧 Installation

```bash
git clone https://github.com/ashrithmst/AIQuoteGenerator.git
cd AIQuoteGenerator
pip install django
python manage.py migrate
python manage.py runserver
