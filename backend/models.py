from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Text, ForeignKey, Index
from sqlalchemy.sql import func
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(120), unique=True, index=True, nullable=True)
    hashed_password = Column(String(255), nullable=False)
    display_name = Column(String(100), nullable=False)
    role = Column(String(30), default="staff")  # company_admin / superadmin / admin / staff / nurse / viewer
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class Measurement(Base):
    __tablename__ = "measurements"

    id = Column(Integer, primary_key=True, index=True)
    id_card = Column(String(20), index=True, nullable=False)          # 身分證字號（可遮罩）
    user_name = Column(String(50), index=True, nullable=False)        # 姓名
    gender = Column(String(5), nullable=False)                        # M / F
    age = Column(Integer)
    height = Column(Float)                                            # cm
    weight = Column(Float)                                            # kg
    bmi = Column(Float)
    body_fat = Column(Float)                                          # %
    smi = Column(Float)                                               # kg/m²
    systolic = Column(Integer)                                        # 收縮壓
    diastolic = Column(Integer)                                       # 舒張壓
    pulse = Column(Integer)
    grip_strength = Column(Float)                                     # kg
    chair_stand_time = Column(Float)                                  # 秒
    walking_time = Column(Float)                                      # 秒
    sarcopenia_stage = Column(String(30), index=True)                 # 正常 / 肌少症前期 / 肌少症 / 嚴重肌少症
    abnormal_count = Column(Integer, default=0)
    status = Column(Text)                                             # 異常描述
    measure_date = Column(String(10), index=True)                     # YYYY-MM-DD
    measure_time = Column(String(19), index=True)                     # YYYY-MM-DD HH:MM:SS
    source = Column(String(30), default="manual")                     # manual / csv / excel / api / device
    created_by = Column(String(50))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (
        Index("ix_idcard_measuretime", "id_card", "measure_time", unique=True),
    )


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    operator = Column(String(50))
    action = Column(String(100))
    details = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
