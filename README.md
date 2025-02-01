# FAQ Multilingual Web Application

This is a **Django-based FAQ web application** where users can view FAQs in multiple languages. It allows administrators to add frequently asked questions (FAQs) and their answers, and users can view them in their preferred language.

**Note:** I tried deploying the project on Heroku, but there is an error during deployment.

---

## Features

- **Multilingual Support**: FAQs are available in different languages.
- **Admin Interface**: Admins can add, edit, and delete FAQs through the Django admin panel.
- **Cache Support**: FAQs are cached using Redis for better performance.
- **Rich Text Editor**: The FAQ questions and answers can be formatted using the CKEditor.
- **REST API**: Exposes a REST API for fetching FAQs in a specified language.

---

## Technologies Used

- **Backend**: Django (Python web framework)
- **Cache**: Redis (for caching FAQ translations)
- **Web Server**: Gunicorn (for deployment on Heroku)
- **Styling**: Bootstrap and custom CSS
- **Rich Text Editor**: CKEditor for better formatting of FAQ content
- **Deployment**: Heroku (for live hosting)

---

## Installation

### Prerequisites

Ensure the following are installed on your system:

- Python 3.12 or later
- pip (Python package installer)
- Git

### 1. Clone the Repository

Clone the repository to get started:

```bash
git clone https://github.com/your-username/faq-multilingual-app.git
cd faq-multilingual-app
```


2. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies:

```bash
python -m venv venv
```
3. Install Dependencies
   
Install the required packages:

```bash
pip install -r requirements.txt
```
4. Create a Superuser
   
To access the Django admin panel, create a superuser:

```bash
python manage.py createsuperuser 
```
For the superuser, use the following credentials:

Username: admin
Password: devansh123

5. Run the Development Server
   
To test the application locally, run:

```bash
python manage.py runserver
```

Access the app by navigating to http://127.0.0.1:8000/admin/ in your browser.

Deployment on Heroku

1. Create a Heroku App
   
If you don't have the Heroku CLI, install it.

Log in to Heroku:

```bash
heroku login
```

Create a new Heroku app:

```bash
heroku create multilingual-app
```

2. Add Redis
   
Add the required Heroku add-ons for the  cache:

```bash
heroku addons:create heroku-redis:hobby-dev
```


3. Deploy the App to Heroku
   
Add, commit, and push your changes to Heroku:

```bash
git add .
git commit -m "Deploy the FAQ app"
git push heroku main
```

4. Run the App
   
Once the deployment is complete, open your app in the browser:

```bash
heroku open
```

Key Commands Used

Here’s a list of the key commands used in this project:

* python manage.py migrate: Run migrations to set up the database.
* python manage.py runserver: Run the development server locally.
* heroku create: Create a new Heroku app.
* heroku addons:create heroku-redis:hobby-dev: Add Redis cache.
* git add . && git commit -m "Commit message" && git push heroku main: Push changes to Heroku.
---
API Endpoints
The project exposes a REST API that allows users to retrieve FAQs in different languages. Below is a list of the available endpoints:
---

1. GET /api/faqs/
Description:
Fetch a list of all FAQs in the specified language.

Example Request:
```bash
GET /api/faqs/
```

Example Response:

```
[
  {
    "id": 1,
    "question": "What is this FAQ app?",
    "answer": "This is a multilingual FAQ web application."
  }
]
```

2. GET /api/faqs/{id}/
Description:
Fetch a specific FAQ by its id.

Example Request:
```bash
GET /api/faqs/1/?lang=hi 
```

Example Response:(ENGLISH)

```
{
  "id": 1,
  "question": "What is this FAQ app?",
  "answer": "This is a multilingual FAQ web application."
}
```

Example Request:

```bash
GET /api/faqs/?lang=bn
```

Example Response:(Bengali)

```
{
  "id": 1,
  "question": "What is this FAQ app?",
  "answer": "This is a multilingual FAQ web application."
}
```


Troubleshooting
If you encounter any issues during deployment on Heroku, check the logs by running:

```bash

heroku logs --tail
```
This will provide insights into any issues or errors with the deployment.

For any additional questions or concerns, feel free to reach out or open an issue in the repository.

---

### Summary of Changes:

1. I have organized the `README.md` into clear sections with bullet points and proper headings.
2. Added a section on **API Endpoints** for easy reference.
3. The **Key Commands Used** section is now more detailed with clear instructions for the user.
4. **Deployment on Heroku** instructions are clear and concise, with steps to deploy and troubleshoot.

Feel free to update the repository link and customize any sections further as needed!







