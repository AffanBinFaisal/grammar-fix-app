# FastAPI Auth App

A full-stack authentication application built with FastAPI and vanilla JavaScript, featuring JWT-based authentication and AI-powered text correction.

## Features

- **User Authentication**: Secure JWT-based registration and login system
- **Password Security**: Bcrypt hashing for password protection
- **Text Correction**: AI-powered grammar and spelling correction using LanguageTool API
- **SQLite Database**: Lightweight database with SQLAlchemy ORM
- **CORS Enabled**: Ready for frontend integration
- **Clean Frontend**: Simple, responsive UI with vanilla JavaScript

## Tech Stack

**Backend:**
- FastAPI
- SQLAlchemy
- Python-JOSE (JWT)
- Passlib (Bcrypt)
- LanguageTool API

**Frontend:**
- HTML5
- CSS3
- Vanilla JavaScript

## Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd fastapi-auth-app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize the database**
   ```bash
   python init_db.py
   ```

## Usage

1. **Start the server**
   ```bash
   uvicorn app.main:app --reload
   ```

2. **Access the application**
   - API: `http://localhost:8000`
   - Frontend: Open `frontend/index.html` in your browser
   - API Docs: `http://localhost:8000/docs`

## API Endpoints

### Authentication
- `POST /register` - Register a new user
- `POST /token` - Login and receive JWT token

### Users
- `GET /users/me` - Get current user profile

### Text Correction
- `POST /text-correction/` - Correct grammar and spelling (requires authentication)

## Project Structure

```
fastapi-auth-app/
├── app/
│   ├── __init__.py
│   ├── main.py           # Application entry point
│   ├── auth.py           # Authentication logic
│   ├── models.py         # Database models
│   ├── schemas.py        # Pydantic schemas
│   ├── crud.py           # Database operations
│   ├── database.py       # Database configuration
│   ├── dependencies.py   # Dependency injection
│   └── routers/
│       ├── auth.py       # Auth endpoints
│       ├── users.py      # User endpoints
│       └── text_correction.py  # Text correction endpoints
├── frontend/
│   ├── index.html        # Main UI
│   ├── app.js            # Frontend logic
│   └── style.css         # Styling
├── requirements.txt      # Python dependencies
└── init_db.py           # Database initialization
```

## Security Notes

- JWT tokens are used for authentication
- Passwords are hashed using bcrypt
- CORS is currently set to allow all origins (update for production)
- Secret key should be stored in environment variables for production

## License

MIT
