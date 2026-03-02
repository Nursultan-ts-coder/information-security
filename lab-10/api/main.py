"""
Simple FastAPI Server for NGINX Reverse Proxy Demo
Run with: uvicorn main:app --host 127.0.0.1 --port 5000
"""

from fastapi import FastAPI
from datetime import datetime
import os

app = FastAPI(title="NGINX Demo API")

# Get port from environment variable (useful for load balancing demo)
PORT = os.environ.get("PORT", "5000")


@app.get("/")
def root():
    """Root endpoint"""
    return {
        "message": "Hello from FastAPI!",
        "server_port": PORT,
        "timestamp": datetime.now().isoformat()
    }


@app.get("/api/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "server_port": PORT}


@app.get("/api/users")
def get_users():
    """Sample users endpoint"""
    return {
        "users": [
            {"id": 1, "name": "Alice", "email": "alice@example.com"},
            {"id": 2, "name": "Bob", "email": "bob@example.com"},
            {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
        ],
        "served_by_port": PORT
    }


@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    """Get specific user"""
    users = {
        1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
        2: {"id": 2, "name": "Bob", "email": "bob@example.com"},
        3: {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
    }
    if user_id in users:
        return {"user": users[user_id], "served_by_port": PORT}
    return {"error": "User not found", "served_by_port": PORT}


@app.post("/api/echo")
def echo(data: dict):
    """Echo back the received data"""
    return {
        "received": data,
        "server_port": PORT,
        "timestamp": datetime.now().isoformat()
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=int(PORT))
