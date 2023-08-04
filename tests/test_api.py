import pytest
import requests

@pytest.mark.duckduckgo
@pytest.mark.api
def test_duckduckgo_simple_answer_api():
    # Arrange
    url = "https://api.duckduckgo.com/?q=python+programmimg&format=json"
    # Act
    response = requests.get(url)
    body = response.json()
    # Assert
    assert response.status_code == 200
    assert "Abstract" in body

