import pytest
from app import app, read_json

@pytest.fixture
def client():
    """Create a test client for the Flask app with session support"""
    """session thingy for flashes doesn't work"""
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'test_secret_key'  # Required for session flash messages
    with app.test_client() as client:
        # with client.session_transaction() as session:
        #     session.modified = True  # Ensure session modifications are saved
        yield client

def test_read_json():
    """Test if JSON data is loaded correctly from CSV"""
    data = read_json("data/breakfast.csv")
    assert isinstance(data, dict)  # Ensure data is a dictionary
    assert len(data) > 0  # Ensure it has entries
    assert isinstance(list(data.keys())[0], str)  # Ensure keys (dish names) are strings
    assert isinstance(list(data.values())[0], list)  # Ensure values (ingredients/instructions) are lists

def test_breakfast_route(client):
    """Test the /breakfast route for flash messages"""
    response = client.get('/breakfast', follow_redirects=True)
    assert response.status_code == 200  # Ensure the page loads correctly

    # Check if the flash message is in the response data
    response_data = response.get_data(as_text=True)
    assert "You should have" in response_data, "Expected flash message not found in response"


def test_dinner_route(client):
    """Test the /dinner route"""
    response = client.get('/dinner')
    assert response.status_code == 200  # Ensure it loads correctly
    assert b"Dinner Menu" in response.data  # Ensure template has expected content