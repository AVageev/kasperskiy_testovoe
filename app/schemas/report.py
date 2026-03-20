from pydantic import BaseModel

class ReportResponse(BaseModel):
    status: str
