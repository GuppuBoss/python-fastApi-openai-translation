# Translation Service

A FastAPI-based web application that provides real-time text translation services using OpenAI's GPT-4 model. The application supports translating text into multiple languages simultaneously and provides both a web interface and REST API endpoints.

## Features

- 🌐 **Multi-language Translation**: Translate text into multiple languages at once
- 🤖 **AI-Powered**: Uses OpenAI's GPT-4 for high-quality translations
- 🚀 **FastAPI Backend**: Modern, fast Python web framework
- 💾 **Database Storage**: PostgreSQL database for storing translation tasks
- 🎨 **Web Interface**: Clean, responsive Bootstrap-based UI
- 🔄 **Background Processing**: Asynchronous translation processing
- 📊 **Task Tracking**: Monitor translation status and retrieve results

## Tech Stack

- **Backend**: FastAPI, SQLAlchemy, PostgreSQL
- **AI**: OpenAI GPT-4
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: PostgreSQL
- **Deployment**: Gunicorn, Uvicorn

## Prerequisites

Before running this project, make sure you have:

- Python 3.8 or higher
- PostgreSQL database
- OpenAI API key

## Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd python
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   pip install -r requirements.txt

   ```

   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory with the following variables:

   ```env
   DATABASE_URL=postgresql://username:password@localhost:5432/database_name
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Set up the database**
   - Create a PostgreSQL database
   - Update the `DATABASE_URL` in your `.env` file with your database credentials
   - The application will automatically create the required tables on startup

## Running the Application

### Development Mode

1. **Start the FastAPI server**

   ```bash
   cd app
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

2. **Access the application**
   - Web Interface: http://localhost:8000/index
   - API Documentation: http://localhost:8000/docs
   - Alternative API Docs: http://localhost:8000/redoc

### Production Mode

```bash
cd app
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

## API Endpoints

### 1. Web Interface

- **GET** `/index` - Main translation interface

### 2. Translation API

- **POST** `/translate` - Submit a translation request

  ```json
  {
    "text": "Hello, world!",
    "languages": ["Spanish", "French", "German"]
  }
  ```

- **GET** `/translate/{task_id}` - Get translation status and results
- **GET** `/translate/content/{task_id}` - Get full translation task details

## Usage Examples

### Using the Web Interface

1. Navigate to http://localhost:8000/index
2. Enter the text you want to translate
3. Specify target languages (comma-separated)
4. Click "Translate" to submit your request
5. Use the provided task ID to check translation status

### Using the API

```bash
# Submit a translation request
curl -X POST "http://localhost:8000/translate" \
     -H "Content-Type: application/json" \
     -d '{
       "text": "Hello, how are you?",
       "languages": ["Spanish", "French", "Italian"]
     }'

# Check translation status
curl "http://localhost:8000/translate/1"
```

## Project Structure

```
python/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application and routes
│   ├── models.py        # SQLAlchemy database models
│   ├── schemas.py       # Pydantic request/response models
│   ├── crud.py          # Database operations
│   ├── database.py      # Database connection and session
│   ├── utils.py         # Translation logic using OpenAI
│   └── templates/
│       └── index.html   # Web interface template
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Environment Variables

| Variable         | Description                     | Required |
| ---------------- | ------------------------------- | -------- |
| `DATABASE_URL`   | PostgreSQL connection string    | Yes      |
| `OPENAI_API_KEY` | OpenAI API key for GPT-4 access | Yes      |

## Database Schema

The application uses a single table `translation_task` with the following structure:

- `id`: Primary key (Integer)
- `text`: Original text to translate (Text)
- `languages`: Target languages (JSON array)
- `status`: Translation status (String)
- `translations`: Translation results (JSON object)

## Error Handling

The application includes comprehensive error handling for:

- Database connection issues
- OpenAI API errors
- Invalid request formats
- Missing translation tasks

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For issues and questions, please open an issue in the repository.
