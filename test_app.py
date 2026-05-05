
from app import app

def test_hello():
    # Simulate a web browser going to the main page
    response = app.test_client().get('/')
    
    # Check if the website loaded successfully (Status code 200 means "OK")
    assert response.status_code == 200
    
    # Check if the text "Hello" is actually on the page
    assert b"Hello" in response.data