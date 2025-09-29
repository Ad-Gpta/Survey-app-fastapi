# FastAPI backend for React with login

- Run `pip install -r requirements.txt` to install dependencies.
- Start the server: `uvicorn app.main:app --reload`
- The login endpoint is available at `/login` (POST, expects JSON: `{ "username": "testuser", "password": "testpass" }`)
