# Fitness AI Q&A API

A FastAPI-based application that provides AI-powered answers to fitness and health questions using OpenAI's GPT model.

## Features

- 🤖 AI-powered Q&A system for fitness questions
- 🔐 Secure API key handling
- 📝 Structured request/response format
- 🏥 Health check endpoint
- 📚 Auto-generated API documentation

## Installation

1. Make sure you have Python 3.7+ installed
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Starting the Server

Run the FastAPI application:
```bash
python main.py
```

Or using uvicorn directly:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at `http://localhost:8000`

### API Endpoints

#### 1. Root Endpoint
- **GET** `/`
- Returns API information and available endpoints

#### 2. Health Check
- **GET** `/health`
- Returns API health status and OpenAI configuration status

#### 3. Ask Question
- **POST** `/ask`
- Send a question and get an AI response

**Request Body:**
```json
{
    "question": "What are the best exercises for building muscle?",
    "api_key": "your-openai-api-key-here"
}
```

**Response:**
```json
{
    "question": "What are the best exercises for building muscle?",
    "answer": "Here are some of the best exercises for building muscle...",
    "model_used": "gpt-3.5-turbo"
}
```

### API Key Configuration

You can provide your OpenAI API key in two ways:

1. **In the request body** (recommended for testing):
   ```json
   {
       "question": "Your question here",
       "api_key": "sk-your-openai-api-key"
   }
   ```

2. **Environment variable** (recommended for production):
   ```bash
   export OPENAI_API_KEY="sk-your-openai-api-key"
   ```

### Testing the API

1. Start the server:
   ```bash
   python main.py
   ```

2. Run the test script:
   ```bash
   python test_api.py
   ```

3. Or use curl:
   ```bash
   curl -X POST "http://localhost:8000/ask" \
        -H "Content-Type: application/json" \
        -d '{
            "question": "What are the best exercises for building muscle?",
            "api_key": "your-openai-api-key-here"
        }'
   ```

### API Documentation

Once the server is running, you can access:
- **Interactive API docs**: `http://localhost:8000/docs`
- **Alternative API docs**: `http://localhost:8000/redoc`

## Example Usage

### Python
```python
import requests

response = requests.post("http://localhost:8000/ask", json={
    "question": "How many calories should I eat to lose weight?",
    "api_key": "your-openai-api-key"
})

print(response.json())
```

### JavaScript
```javascript
const response = await fetch('http://localhost:8000/ask', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        question: 'What is the best workout routine for beginners?',
        api_key: 'your-openai-api-key'
    })
});

const data = await response.json();
console.log(data);
```

## Error Handling

The API returns appropriate HTTP status codes:
- `200`: Success
- `400`: Bad request (missing API key, invalid input)
- `500`: Internal server error

## Security Notes

- Never commit your OpenAI API key to version control
- Use environment variables in production
- Consider implementing rate limiting for production use
- The API key is not stored or logged

## Dependencies

- FastAPI: Web framework
- OpenAI: OpenAI API client
- Uvicorn: ASGI server
- Pydantic: Data validation
- Requests: HTTP client (for testing)
