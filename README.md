# 🎬 PicFlix – Video Sharing Platform

A full-stack video sharing platform that allows users to upload content, choose categories, and enjoy personalized content suggestions.

## ✨ Features

### User Management

- **Secure Authentication**: Registration and login with bcrypt password hashing
- **Personal Profiles**: Customizable profiles including name, profile picture, description, and favorite categories
- **User Search**: Find other users by name

### Video System

- **Video Upload**: Support for multiple formats (MP4, AVI, MOV, MKV)
- **Category Management**: Organize videos by categories
- **Personalized Feed**: Smart recommendations based on user preferences
- **Engagement**: Like/dislike videos and track interactions

### Smart Recommendations

- **Logged-in Users**: Personalized feed based on favorite categories
- **Guest Users**: Curated selection of popular content

## 🛠️ Technologies

- **Language & Framework**: Python 3.10+ with Flask
- **Security**: bcrypt for password hashing
- **Templating**: Jinja2 template engine
- **Database**: SQL-based database
- **Configuration**: python-dotenv for environment variable management
- **Cloud Storage**: Cloudinary for video and image hosting

### Database Connection Pooling

To improve database connection efficiency and avoid repeatedly opening and closing connections, the application uses **connection pooling** via the `dbutils.pooled_db` library.  
This approach manages up to 10 active connections simultaneously, enhancing the application's performance and stability.

## 📁 Project Structure

```
picflix/
├── app.py                  # Main application entry point
├── config.py               # Configuration and setup
├── db.py                   # Database connection
├── requirements.txt        # Python dependencies
├── build.sh                # Shell script to automate project setup/build tasks
├── .env                    # Environment variables (not in repo)
├── .env.example            # Environment variables template
├── .gitignore              # Git ignore rules
├── README.md               # Project documentation
├── certs/                  # Security certificates for HTTPS/SSL
│   ├── ca.pem              # Certificate Authority (CA) certificate used for SSL/TLS       
├── models/                 # Database models and CRUD operations
│   ├── __init__.py
│   ├── users.py
│   ├── videos.py
│   ├── likes.py
│   └── categories.py
├── routes/                 # Application routes
│   ├── __init__.py
│   ├── auth_routes.py
│   ├── video_routes.py
│   └── user_routes.py
├── templates/              # Jinja2 HTML templates
│   ├── index.html
│   ├── login.html
│   ├── profile.html
│   └── signup.html
├── static/                 # Static assets (CSS, JS)
│   ├── css/
│   ├── fonts/
│   ├── images/
│   └── js/
├── database/               # Database related files
│   ├── schema.sql          # Database schema
│   └── seed_data.sql       # Sample data
```

## 🚀 Installation & Setup

### Prerequisites

- Python 3.10 or higher
- SQL database (SQLite/PostgreSQL/MySQL)
- Cloudinary account for file storage

### 1. Clone the Repository

```bash
git clone https://github.com/Hadar-Gerashi/Picflix.git
cd Picflix
```

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Setup

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your configuration
```
```
SECRET_KEY = your_secret_key_here
PORT = 8094
CLOUD_NAME= your_cloud_name_here
API_KEY= your_api_key_here
API_SECRET= your_api_secret_here
DB_HOST= your_db_host
DB_USER= your_db_user
DB_PASS= your_db_password
DB_NAME= your_db_name
DB_PORT= your_db_port
CLOUD_VIDEO_URL= your_cloud_video_url
CLOUD_IMAGE_URL= your_cloud_image_url
```

### 5. Run the Application

```bash
python app.py
```

Visit [http://localhost:8080](http://localhost:8080) in your browser.

## 📋 Requirements.txt Example

```
Flask==3.1.1
python-dotenv==1.0.0
bcrypt==4.0.1
werkzeug>=3.1.0
Jinja2==3.1.2
cloudinary==1.39.0
pymysql
dbutils
pyodbc>=5.0.0
gunicorn
```

## 🔐 Security Features

- **Password Security**: All passwords are hashed using bcrypt
- **Session Management**: Secure session handling with Flask sessions
- **File Upload Security**: Validated file types and secure cloud storage
- **Environment Variables**: Sensitive data stored in environment variables

## 📸 File Storage

- **Videos**: Uploaded and stored on Cloudinary cloud storage
- **Profile Images**: Uploaded and stored on Cloudinary cloud storage
- **File Validation**: Only approved file formats are accepted
- **Cloud Integration**: Automatic optimization and CDN delivery via Cloudinary

## 📋 API Endpoints

| Method | Endpoint                               | Description                                 | Blueprint |
|--------|----------------------------------------|---------------------------------------------|-----------|
| GET    | `/`                                    | Redirect to home page                       | video     |
| GET    | `/home`                                | Home page with personalized video feed      | video     |
| GET    | `/uploads/<filename>`                  | Serve uploaded video files                  | video     |
| GET    | `/upload_video`                        | Video upload form page                      | video     |
| POST   | `/upload_video`                        | Process video upload with categories        | video     |
| POST   | `/delete_video`                        | Delete video and file                       | video     |
| POST   | `/toggle_like`                         | Like/unlike video (AJAX)                    | video     |
| GET    | `/login`                               | Login form page                             | auth      |
| POST   | `/login`                               | User authentication                         | auth      |
| GET    | `/signup`                              | Registration form page                      | auth      |
| POST   | `/signup`                              | User registration with categories           | auth      |
| GET    | `/logout`                              | User logout and session clear               | auth      |
| GET    | `/profile/<int:user_id>`               | User profile page                           | user      |
| POST   | `/profile/<int:user_id>`               | Update profile image (upload/remove)        | user      |
| POST   | `/profile/<int:user_id>/update_text`   | Update profile description text             | user      |
| GET    | `/search_users`                        | Search users by name (AJAX)                 | user      |

### **URL Examples:**

- Login: `http://localhost:8080/login`
- Signup: `http://localhost:8080/signup`
- Home: `http://localhost:8080/home`
- Profile: `http://localhost:8080/profile/<user_id>`
- Video Upload: `http://localhost:8080/upload_video`

## 👨‍💻 Author

**Hadar** - Software Engineering Student  
Developed as part of final studies project

## 📞 Support

If you encounter any issues or have questions, please open an issue on GitHub or contact the maintainer.

**Happy Streaming! 🎬**
