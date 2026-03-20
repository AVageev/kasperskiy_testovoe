from fastapi import APIRouter, UploadFile, BackgroundTasks, HTTPException
from app.services.text_analyzer import process_file

router = APIRouter()

@router.post("/public/report/export")
async def export_report(file: UploadFile, background_tasks: BackgroundTasks):
    if not file.filename.endswith(".txt"):
        raise HTTPException(status_code=400, detail="Only .txt files allowed")

    background_tasks.add_task(process_file, file)

    return {"status": "processing"}
