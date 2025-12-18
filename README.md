# My Awesome Cart 🛒

## Introduction
**My Awesome Cart** is a Django-based e-commerce web application that allows users to browse products, add them to a cart, and explore blog content. It demonstrates core e-commerce functionality such as product listings, cart management, and an admin dashboard for managing products and blog posts.

This project is ideal for learning how Django can be used to build full-stack e-commerce platforms with dynamic data, admin management, templating, and user interactions.

## Project Type
Fullstack

## Deployed App
Frontend: _Not deployed_  
Backend: _Not deployed_  
Database: _Not deployed_

> You can deploy this on services like **Render / Railway / Heroku** for a full live demo.

## Directory Structure
My_awesome_cart/
├─ blog/ # Blog app for posts and content
├─ customAdmin/ # Custom admin functionality
├─ shop/ # Main ecommerce app
├─ static/ # Static assets (CSS, JS, images)
├─ media/ # Uploaded media (shop images)
├─ mac/ # (Unused / IDE related)
├─ manage.py # Django management file
├─ requirements.txt # Python dependencies
├─ db.sqlite3 # SQLite database

python
Copy code

## Features

- Product browsing with categories
- Add products to cart
- Cart view with update and removal options
- Blog section with posts
- Django admin dashboard to manage products and blog posts
- Static and media file support

## Design decisions or assumptions

- Used **Django templates** for server-side rendering of UI.
- Used **SQLite** for simple local database storage (can be replaced with PostgreSQL/MySQL).
- Separated concerns with apps (`shop`, `blog`, and `customAdmin`) for modularity.
- Assumed basic authentication/admin handled via Django admin.

## Installation & Getting started
Follow these steps to run the project locally:

Clone the repository
git clone https://github.com/Pravansh5/My_awesome_cart.git

Navigate into the project directory
cd My_awesome_cart

Create a virtual environment
python -m venv venv

Activate the virtual environment

Windows
venv\Scripts\activate

macOS / Linux
source venv/bin/activate

Install dependencies
pip install -r requirements.txt

Apply database migrations
python manage.py migrate

Create an admin user (optional)
python manage.py createsuperuser

Run the development server
python manage.py runserver

Open your browser and visit:
http://127.0.0.1:8000/

Usage

Browse the homepage to view available products

Click on products to view detailed information

Add items to the cart and manage quantities

Navigate to /admin to log in as an admin and manage products and blog posts

Credentials

Use the Django admin credentials you create using:
python manage.py createsuperuser

Demo credentials (for testing purposes):

Username: admin

Password: admin123

APIs Used

This project uses internal Django views and templates and does not rely on any external APIs.

API Endpoints

GET / – Homepage listing products

GET /cart/ – View cart

POST /add-to-cart/ – Add product to cart

GET /blog/ – Blog listing

GET /admin/ – Django admin panel

(Add real endpoints if API/REST views are implemented in the future.)

Technology Stack

Backend: Django (Python)

Frontend: Django Templates (HTML, CSS, JavaScript)

Database: SQLite (default Django database)

Static Assets: CSS and JavaScript files stored in static/

Media Storage: Uploaded product images stored in media/
