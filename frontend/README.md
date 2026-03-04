# Frontend Setup

A simple HTML/CSS/JavaScript frontend for the FastAPI Auth App.

## Features

- User Registration
- User Login with JWT authentication
- Text Correction using LanguageTool API
- Clean and responsive UI

## How to Run

1. Make sure your FastAPI backend is running:
   ```bash
   cd ..
   uvicorn app.main:app --reload
   ```

2. Open `index.html` in your web browser, or use a simple HTTP server:
   ```bash
   # Using Python
   python -m http.server 8080
   
   # Or using Node.js
   npx http-server -p 8080
   ```

3. Access the frontend at `http://localhost:8080`

## Usage

1. **Register**: Create a new account with your email and password
2. **Login**: Sign in with your credentials
3. **Correct Text**: Enter text with grammar/spelling errors and get corrections

## API Endpoints Used

- `POST /users/` - Register new user
- `POST /auth/token` - Login and get access token
- `GET /users/me` - Get current user info
- `POST /text-correction/` - Correct text grammar and spelling
