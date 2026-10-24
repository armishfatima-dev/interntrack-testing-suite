def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "database": "connected"}

def test_create_submission_protected(client):
    # Register and login to get token
    client.post(
        "/auth/register",
        json={"email": "intern@example.com", "password": "password123", "role": "intern"}
    )
    login_res = client.post(
        "/auth/login",
        data={"username": "intern@example.com", "password": "password123"}
    )
    token = login_res.json()["access_token"]
    
    # Post submission with token header
    response = client.post(
        "/submissions/",
        json={"title": "First Task", "content": "Completed FastAPI security implementation."},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "First Task"
    assert data["status"] == "pending"

def test_get_submissions_unauthorized(client):
    # Attempt to fetch without auth token
    response = client.get("/submissions/")
    assert response.status_code == 401

