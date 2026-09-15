from pydantic import BaseModel, Field, field_validator
from typing import Optional, List
from datetime import datetime


# ---------- Auth ----------
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=4)
    display_name: str
    email: Optional[str] = None
    role: str = "staff"


class UserLogin(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    display_name: str
    email: Optional[str]
    role: str
    is_active: bool
    created_at: Optional[datetime]

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserOut


# ---------- Measurement ----------
class MeasurementBase(BaseModel):
    id_card: str
    user_name: str
    gender: str
    age: Optional[int] = None
    height: Optional[float] = None
    weight: Optional[float] = None
    bmi: Optional[float] = None
    body_fat: Optional[float] = None
    smi: Optional[float] = None
    systolic: Optional[int] = None
    diastolic: Optional[int] = None
    pulse: Optional[int] = None
    grip_strength: Optional[float] = None
    chair_stand_time: Optional[float] = None
    walking_time: Optional[float] = None
    measure_time: Optional[str] = None  # YYYY-MM-DD HH:MM:SS

    @field_validator("gender")
    @classmethod
    def gender_ok(cls, v):
        v = v.upper()
        if v not in ("M", "F", "男", "女"):
            raise ValueError("gender 必須是 M/F 或 男/女")
        return "M" if v in ("M", "男") else "F"


class MeasurementCreate(MeasurementBase):
    pass


class MeasurementOut(MeasurementBase):
    id: int
    bmi: Optional[float]
    sarcopenia_stage: Optional[str]
    abnormal_count: Optional[int]
    status: Optional[str]
    measure_date: Optional[str]
    measure_time: Optional[str]
    source: Optional[str]
    created_by: Optional[str]
    created_at: Optional[datetime]

    class Config:
        from_attributes = True


class MeasurementQuery(BaseModel):
    q: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    stage: Optional[str] = None
    page: int = 1
    page_size: int = 50


class StatsOut(BaseModel):
    total_records: int
    unique_users: int
    avg_grip: float
    avg_chair: float
    avg_walk: float
    multi_abnormal_rate: float
    summary_text: str
    sarcopenia_pie: List[dict]
    monthly_trends: dict


class ImportResult(BaseModel):
    success: int
    skipped: int
    failed: int
    deleted: int = 0
    messages: List[str]
