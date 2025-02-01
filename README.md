# FAQ Management System with Multilingual Support

A Django-based REST API for managing FAQs with automatic translation (English, Hindi, Bengali) and WYSIWYG editor support.

## Features

- 📚 Multilingual FAQ support (English, Hindi, Bengali)
- ✍️ Rich text editor for answers
- ⚡ Redis caching for translations
- 🌐 REST API endpoints with language selection
- 🔐 Admin panel for content management
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
   git clone https://github.com/Y-coderr/faq-project.git
   cd faq-project

2. **Apply Migrations**
```bash
python manage.py migrate
```

3. **Run the Server**
```bash
python manage.py runserver
```

## Superuser Login

### Using an Existing Superuser
1. Start the Django development server:
   ```bash
   python manage.py runserver
   ```
2. Open your browser and go to:
   ```
   http://127.0.0.1:8000/admin/
   ```
3. Enter the superuser credentials (provided by the admin or previously created):
   - **Username:** `<your-superuser-username>`
   - **Password:** `<your-superuser-password>`
   - For example (This Superuser created by me , you create your own):-
   - **Username:** `kadam`
   - **Password:** `Kadam@1602`
4. Click **Login** to access the Django Admin panel.

### Creating a New Superuser
If you don’t have an existing superuser, create one using the following command:
```bash
python manage.py createsuperuser
```
You will be prompted to enter:
- **Username** (e.g., `admin`)
- **Email address** (optional)
- **Password** (must be strong)

Once the superuser is created, you can log in at:
```
http://127.0.0.1:8000/admin/
```
using the credentials you just created.

## Additional Notes
- Ensure your database is correctly set up before creating a superuser.
- If you forget the superuser password, you can reset it with:
  ```bash
  python manage.py changepassword <username>
  ```
- If you need to create a superuser without prompts, use:
  ```bash
  python manage.py createsuperuser --username admin --email admin@example.com --noinput
  python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').update(password='pbkdf2_sha256$...')"


## Example API Useage
```bash
# Fetch FAQs in English (default)
curl http://localhost:8000/api/faqs/

# Fetch FAQs in Hindi
curl http://localhost:8000/api/faqs/?lang=hi

# Fetch FAQs in Bengali
curl http://localhost:8000/api/faqs/?lang=bn
```

  
## Project Screenshots
   **Admin Login Page**
![2](https://github.com/user-attachments/assets/a2a2d137-5de4-44ba-8e71-80057e36752e)

   **After Login**
![1](https://github.com/user-attachments/assets/71463e2b-a4e5-4f9c-940d-35884fab12a6)

   **Create FAQ**
![3](https://github.com/user-attachments/assets/df4a45de-8d9f-406b-a87b-2d81b397419b)

   **Change FAQ**
![8](https://github.com/user-attachments/assets/c73e8382-648d-4988-aef8-51e38e27a275)

   **Add User**
![4](https://github.com/user-attachments/assets/ff697126-0904-4120-a352-dd036ef1db8e)

   **Accessing FAQ's**
   1.
   ```bash
      http://127.0.0.1:8000/api/faqs/
   ```
![5](https://github.com/user-attachments/assets/95c51b04-2418-43af-a8ab-f5faaf9cbf68)

   2.
   ```bash
      http://127.0.0.1:8000/api/faqs/?lang=hi
   ```
![6](https://github.com/user-attachments/assets/90e3f3d4-27e0-4fbe-9318-96e40ead062c)

   3.
   ```bash
      http://127.0.0.1:8000/api/faqs/?lang=bn
   ```
![7](https://github.com/user-attachments/assets/35a9dfea-e973-40d5-82d8-9f38d4a55050)
