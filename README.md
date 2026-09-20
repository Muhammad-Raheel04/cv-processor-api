# CV Processor API

A FastAPI-based API that extracts text from CVs and uses an LLM to convert the extracted content into structured CV data.

## Features

* Upload PDF CVs
* Upload DOCX CVs
* Extract raw text from CV files
* Extract structured CV information using Groq
* Validate extracted data using Pydantic

## Tech Stack

* Python
* FastAPI
* Pydantic
* Groq API
* PyPDF
* python-docx

## Project Structure

```text
cv-processor-api/
│
├── main.py
│
├── routes/
│   └── cv.py
│
├── services/
│   ├── cv_text_extractor.py
│   └── cv_data_extractor.py
│
└── schemas/
    └── cv.py
```

## Setup

Clone the repository and create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file based on the provided `example.env`:

```powershell
Copy-Item example.env .env
```

Then add your API key to `.env`:

```env
GROQ_API_KEY=your_groq_api_key
```

> Never commit your `.env` file or expose your API keys publicly.


## Run the API

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

### Extract CV Text

```http
POST /cv/extract-text
```

Upload a PDF or DOCX file and receive the extracted text.

### Extract Structured CV Data

```http
POST /cv/extract-data
```

Upload a CV and receive structured information such as:

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": null,
  "location": "Islamabad",
  "summary": "...",
  "skills": [],
  "education": [],
  "experience": [],
  "projects": [],
  "certifications": []
}
```

## Future Goal

The long-term goal of this project is to process CVs into reliable structured data that can be used for automated form filling and other recruitment workflows.
