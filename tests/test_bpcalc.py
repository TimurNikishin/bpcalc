def test_home(client):
    response = client.get("/")
    assert b"<title>Blood Pressure Category Calculator</title>" in response.data