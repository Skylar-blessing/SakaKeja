# SakaKeja

# 🏡 SakaKeja - Real Estate Management Platform

SakaKeja is a comprehensive, full-stack real estate management platform designed to seamlessly connect property owners with tenants in a modern, digital environment. 

The system empowers tenants to explore a wide range of property listings with rich visuals, make secure payments online, request moving assistance, and share reviews based on their rental experiences. On the other side, property owners can effortlessly list new properties with image uploads, manage and update their existing listings, and track payments from tenants in real-time. 

With built-in support for user authentication, role-based access control, and integrations like PayPal for payments and Cloudinary for media handling, SakaKeja offers a robust, scalable solution tailored for the real estate ecosystem. Whether you're looking to rent, manage, or monitor properties, SakaKeja provides an all-in-one platform that is intuitive, secure, and efficient.


---

## 🔗 Live Demo

> _Coming soon..._ 

---

## 🧪 Features

### 👤 Authentication & User Roles
- JWT-based login
- Email verification
- Role-specific access (Tenant / Owner)

### 🏠 Tenant Features
- Browse properties
- View listings in card/grid format
- Post reviews
- Make payments via PayPal
- Hire movers

### 🧑‍💼 Owner Features
- Post new property listings with image uploads
- View properties
- View payments received

### ⚙️ Admin/Shared
- RESTful API with pagination
- Cloudinary for image hosting
- PostgreSQL for data storage
- Role-based route protection

---

## ⚙️ Setup Instructions

### 🔙 Backend (Flask)

1. Clone the repo and navigate to backend:
   ```bash
   git clone https://github.com/Skylar-blessing/SakaKeja.git
   cd SakaKeja/backend


2. Install dependencies:

   pip install pipenv
   pipenv install

3. Set environment variables:

   export CLOUDINARY_CLOUD_NAME=your_cloud_name

   export CLOUDINARY_API_KEY=your_api_key

   export CLOUDINARY_API_SECRET=your_api_secret

   export EMAIL_USERNAME=your_email

   export EMAIL_PASSWORD=your_email_password

   export MAIL_DEFAULT_SENDER=your_email

   export PAYPAL_CLIENT_ID=your_id

   export PAYPAL_CLIENT_SECRET=your_secret


4. Set up the database:

   pipenv run flask db upgrade
   pipenv run python seed.py  # Optional: seed data

5. Run the backend:

   pipenv run flask run


### 💻 Frontend (React)
1. Navigate to frontend:

   cd ../frontend
   
2. Install dependencies:

   npm install

3. Start the dev server:

   npm start

Visit: http://localhost:3000


### 🛠️ Tech Stack

Frontend:	React, React Router
Backend:	Flask, Flask-RestX, SQLAlchemy
Auth:	JWT, Flask-JWT-Extended
Email:	Flask-Mail
Storage:	PostgreSQL + Alembic
Media:	Cloudinary
Payments:	PayPal SDK


### 🧩 Future Enhancements

Admin panel for global control
SMS notifications
Google login via OAuth
Property filtering/sorting
Responsive mobile views


### 🤝 Contribution Guide
Fork the repo
Create a new branch (git checkout -b feature/your-feature)
Commit your changes (git commit -m 'Add feature')
Push to your branch (git push origin feature/your-feature)
Open a Pull Request


### 📄 License
MIT License





