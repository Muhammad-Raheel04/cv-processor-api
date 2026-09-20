from fastapi import APIRouter, File, UploadFile
from schemas.cv import CVData
from services.cv_data_extractor import extract_cv_data
from services.cv_text_extractor import extract_file_text

router = APIRouter(prefix="/cv", tags=["CV"])


@router.post("/extract-text")
async def extract_text(file: UploadFile = File(...)):
    text = await extract_file_text(file)

    return {
        "filename": file.filename,
        "text": text,
    }

@router.post("/extract-data", response_model=CVData)
async def extract_data(file: UploadFile = File(...)):
    text = await extract_file_text(file)

    return extract_cv_data(text)
