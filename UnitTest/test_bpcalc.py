def test_page_title(client):
    response = client.get("/")
    assert b"<title>Blood Pressure Category Calculator</title>" in response.data
    
def test_submission_low(client):
    response = client.post("/", data={"systolic": "70", "diastolic": "40"})

    assert b"Low blood pressure" in response.data

def test_submission_ideal(client):
    response = client.post("/", data={"systolic": "110", "diastolic": "70"})

    assert b"Ideal blood pressure" in response.data

def test_submission_prehigh(client):
    response = client.post("/", data={"systolic": "130", "diastolic": "85"})

    assert b"Pre-High blood pressure" in response.data

def test_submission_high(client):
    response = client.post("/", data={"systolic": "170", "diastolic": "95"})

    assert b"High blood pressure" in response.data

def test_submission_invalid_1(client):
    response = client.post("/", data={"systolic": "200", "diastolic": "95"})

    assert b"Submitted invalid values" in response.data

def test_submission_invalid_2(client):
    response = client.post("/", data={"systolic": "120", "diastolic": "35"})

    assert b"Submitted invalid values" in response.data
    
def test_submission_invalid_3(client):
    response = client.post("/", data={"systolic": "180", "diastolic": "110"})

    assert b"Submitted invalid values" in response.data
