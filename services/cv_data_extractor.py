import json
import os

from dotenv import load_dotenv
from groq import Groq
from schemas.cv import CVData

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def extract_cv_data(text: str) -> CVData:
    prompt = f"""
    You are a CV information extraction system.

Extract information from the following CV and return ONLY valid JSON.

The JSON must contain exactly these fields:

{{
    "name": null,
    "email": null,
    "phone": null,
    "location": null,
    "summary": null,
    "skills": [],
    "education": [],
    "experience": [],
    "projects": [],
    "certifications": []
}}

Rules:

1. Extract only information that actually exists in the CV.
2. Never invent information.
3. If information is missing, use null.
4. For skills, return an array of strings.
5. For education, use:
   - degree
   - institution
   - start_date
   - end_date
6. For experience, use:
   - company
   - position
   - start_date
   - end_date
   - description
7. Return JSON only.
8. Preserve the original meaning of the CV.

CV TEXT:

{text}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        temperature=0,
    )

    content = response.choices[0].message.content

    data = json.loads(content)

    return CVData(**data)
