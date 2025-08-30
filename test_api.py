import requests
import json

# API base URL
BASE_URL = "http://localhost:8000"

def test_api():
    """Test the Fitness AI Q&A API"""
    
    # Test 1: Check root endpoint
    print("1. Testing root endpoint...")
    response = requests.get(f"{BASE_URL}/")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()
    
    # Test 2: Check health endpoint
    print("2. Testing health endpoint...")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()
    
    # Test 3: Ask a question (you'll need to provide your OpenAI API key)
    print("3. Testing ask endpoint...")
    print("Note: API key is configured statically - just send your question!")
    
    # Example request - no API key needed
    question_data = {
        "question": "What are the best exercises for building muscle?"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/ask", json=question_data)
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            print(f"Response: {json.dumps(response.json(), indent=2)}")
        else:
            print(f"Error: {response.text}")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API. Make sure the server is running.")
    print()

if __name__ == "__main__":
    test_api()
