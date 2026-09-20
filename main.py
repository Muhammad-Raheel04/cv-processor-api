from io import BytesIO

from docx import Document
from fastapi import FastAPI, File, HTTPException, UploadFile
from pypdf import PdfReader

app = FastAPI()

@app.get("/")
def root():
    return {"success": "false", "message": "cv processor api is running"}

@app.post("/extract-text")
async def extract_text(file: UploadFile = File(...)):
    if file.content_type == "application/pdf":
        contents = await file.read()
        reader = PdfReader(BytesIO(contents))

        text = ""

        for page in reader.pages:
            text += page.extract_text() or ""
    elif (
        file.content_type
        == "application/vnd.openxmlformats-officedocument.wordprocessingml.docuement"
    ):
        contents = await file.read()
        document = Document(BytesIO(contents))

        text = "\n".join(paragraph.text for paragraph in document.paragraphs)
    else:
        raise HTTPException(
            status_code=400, detail="Only pdf and DOCX files are supported"
        )
    
    return {"filename": file.filename, "text": text}
