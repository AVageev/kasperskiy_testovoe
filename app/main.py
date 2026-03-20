from fastapi import FastAPI
from app.api import report

app = FastAPI(title="Report Service")

app.include_router(report.router)
