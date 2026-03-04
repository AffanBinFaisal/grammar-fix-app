const API_URL = 'http://localhost:8000';
let token = localStorage.getItem('token');

// Check if user is already logged in
if (token) {
    checkAuth();
}

// Tab switching
function showTab(tabName) {
    document.querySelectorAll('.tab-content').forEach(tab => {
        tab.classList.remove('active');
    });
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    
    document.getElementById(`${tabName}-tab`).classList.add('active');
    event.target.classList.add('active');
}

// Login
document.getElementById('login-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const email = document.getElementById('login-email').value;
    const password = document.getElementById('login-password').value;
    
    try {
        const formData = new URLSearchParams();
        formData.append('username', email);
        formData.append('password', password);
        
        const response = await fetch(`${API_URL}/auth/token`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: formData
        });
        
        if (!response.ok) {
            throw new Error('Invalid credentials');
        }
        
        const data = await response.json();
        token = data.access_token;
        localStorage.setItem('token', token);
        
        showMessage('auth-message', 'Login successful!', 'success');
        setTimeout(() => {
            loadApp();
        }, 500);
        
    } catch (error) {
        showMessage('auth-message', error.message, 'error');
    }
});

// Register
document.getElementById('register-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const email = document.getElementById('register-email').value;
    const password = document.getElementById('register-password').value;
    
    try {
        const response = await fetch(`${API_URL}/users/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email, password })
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Registration failed');
        }
        
        showMessage('auth-message', 'Registration successful! Please login.', 'success');
        setTimeout(() => {
            showTab('login');
            document.querySelector('.tab-btn').click();
        }, 1500);
        
    } catch (error) {
        showMessage('auth-message', error.message, 'error');
    }
});

// Text Correction
document.getElementById('correction-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const text = document.getElementById('input-text').value;
    
    try {
        const response = await fetch(`${API_URL}/text-correction/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({ text })
        });
        
        if (!response.ok) {
            throw new Error('Text correction failed');
        }
        
        const data = await response.json();
        
        document.getElementById('original-text').textContent = data.original_text;
        document.getElementById('corrected-text').textContent = data.corrected_text;
        document.getElementById('correction-result').style.display = 'block';
        
        showMessage('app-message', 'Text corrected successfully!', 'success');
        
    } catch (error) {
        showMessage('app-message', error.message, 'error');
    }
});

// Check authentication and load user data
async function checkAuth() {
    try {
        const response = await fetch(`${API_URL}/users/me`, {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });
        
        if (!response.ok) {
            throw new Error('Authentication failed');
        }
        
        const user = await response.json();
        loadApp(user.email);
        
    } catch (error) {
        logout();
    }
}

// Load app section
function loadApp(email = null) {
    if (email) {
        document.getElementById('user-email').textContent = email;
    } else {
        checkAuth();
        return;
    }
    
    document.getElementById('auth-section').style.display = 'none';
    document.getElementById('app-section').style.display = 'block';
}

// Logout
function logout() {
    token = null;
    localStorage.removeItem('token');
    document.getElementById('auth-section').style.display = 'block';
    document.getElementById('app-section').style.display = 'none';
    document.getElementById('login-form').reset();
    document.getElementById('register-form').reset();
    document.getElementById('correction-form').reset();
    document.getElementById('correction-result').style.display = 'none';
}

// Show message
function showMessage(elementId, message, type) {
    const messageEl = document.getElementById(elementId);
    messageEl.textContent = message;
    messageEl.className = `message ${type}`;
    messageEl.style.display = 'block';
    
    setTimeout(() => {
        messageEl.style.display = 'none';
    }, 3000);
}
