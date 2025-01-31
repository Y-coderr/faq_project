# FAQ Management System with Multilingual Support

A Django-based REST API for managing FAQs with automatic translation (English, Hindi, Bengali) and WYSIWYG editor support.

## Features

- 📚 Multilingual FAQ support (English, Hindi, Bengali)
- ✍️ Rich text editor for answers
- ⚡ Redis caching for translations
- 🌐 REST API endpoints with language selection
- 🔐 Admin panel for content management
- 📦 Docker support
- 📈 Optimized for performance

## Tech Stack

- **Backend**: Django 4.2
- **Database**: SQLite (Development), PostgreSQL (Production-ready)
- **Translation**: GoogleTranslator (googletrans not working due to python 3.13.1)
- **Editor**: django-ckeditor
- **Caching**: Redis
- **API**: Django REST Framework

## Installation

### Prerequisites
- Python 3.9+
- Redis server
- Docker (optional)

### Steps

1. **Clone Repository**
   ```bash
   git clone https://github.com/yourusername/faq-project.git
   cd faq-project
