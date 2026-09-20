from io import BytesIO

from docx import Document
from fastapi import File, HTTPException, UploadFile
from pypdf import PdfReader


async def extract_file_text(file: UploadFile = File(...)):
    if file.content_type == "application/pdf":
        contents = await file.read()
        reader = PdfReader(BytesIO(contents))

        text = ""

        for page in reader.pages:
            text += page.extract_text() or ""

        return text
    elif (
        file.content_type
        == "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    ):
        contents = await file.read()
        document = Document(BytesIO(contents))

        text = "\n".join(paragraph.text for paragraph in document.paragraphs)

        return text
    else:
        raise HTTPException(
            status_code=400, detail="Only pdf and DOCX files are supported"
        )
