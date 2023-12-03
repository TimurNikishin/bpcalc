import sys

response_title = b"<title>Blood Pressure Category Calculator</title>"
response_low = b"Low blood pressure"
response_ideal = b"Ideal blood pressure"
response_prehigh = b"Pre-High blood pressure"
response_high = b"High blood pressure"
response_invalid = b"Submitted invalid values"


def test_page_title(client):
    try:
        response = client.get("/")
        assert response_title in response.data
        print('page_title test Passed')
    except AssertionError:
        print('page_title test Failed')
        sys.exit(1)
    
def test_submission(client):
    response = client.post("/", data={"systolic": "110", "diastolic": "70"})
    assert response_ideal in response.data
    response = client.post("/", data={"systolic": "130", "diastolic": "85"})
    assert response_prehigh in response.data
    response = client.post("/", data={"systolic": "170", "diastolic": "95"})
    assert response_high in response.data
    response = client.post("/", data={"systolic": "200", "diastolic": "95"})
    assert response_invalid in response.data
    response = client.post("/", data={"systolic": "120", "diastolic": "35"})
    assert response_invalid in response.data
    response = client.post("/", data={"systolic": "180", "diastolic": "110"})
    assert response_invalid in response.data
