def test_register_user(client):
    response = client.post(
        "/auth/register",
        json={"email": "test@example.com", "password": "securepassword123", "role": "intern"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data

def test_login_success(client):
    # Register first
    client.post(
        "/auth/register",
        json={"email": "login@example.com", "password": "securepassword123", "role": "intern"}
    )
    
    # Try logging in
    response = client.post(
        "/auth/login",
        data={"username": "login@example.com", "password": "securepassword123"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_wrong_password(client):
    response = client.post(
        "/auth/login",
        data={"username": "wrong@example.com", "password": "wrongpassword"}
    )
    assert response.status_code == 401

