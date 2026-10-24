def test_progression_workflow(client):
    # Register and login user
    client.post(
        "/auth/register",
        json={"email": "progression@example.com", "password": "password123", "role": "intern"}
    )
    login_res = client.post(
        "/auth/login",
        data={"username": "progression@example.com", "password": "password123"}
    )
    token = login_res.json()["access_token"]
    
    # Create submission (Week 4 / 6 workflow check)
    response = client.post(
        "/submissions/",
        json={"title": "Progression Task", "content": "Testing unlock requirements."},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 201
    
    # Fetch submissions to verify progression list state
    get_res = client.get(
        "/submissions/",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert get_res.status_code == 200
    submissions = get_res.json()
    assert len(submissions) >= 1
    assert submissions[0]["title"] == "Progression Task"

