import uuid
from sqlalchemy import String, ForeignKey, TIMESTAMP, Text, text, Integer, Numeric
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import Optional
from app.database import Base

class AnalysisResult(Base):
    __tablename__ = "analysis_results"
    
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("products.id"), nullable=False)
    profitability_score: Mapped[float] = mapped_column(Numeric(5, 2), nullable=False, default=0)
    swot: Mapped[dict] = mapped_column(JSONB, default={}, server_default='{}')
    score_breakdown: Mapped[dict] = mapped_column(JSONB, default={}, server_default='{}')
    trend_analysis: Mapped[dict] = mapped_column(JSONB, default={}, server_default='{}')
    competition_data: Mapped[dict] = mapped_column(JSONB, default={}, server_default='{}')
    feature_gaps: Mapped[dict] = mapped_column(JSONB, default={}, server_default='{}')
    ai_recommendations: Mapped[dict] = mapped_column(JSONB, default={}, server_default='{}')
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), index=True)
    version: Mapped[int] = mapped_column(Integer, default=1, server_default="1")
    
    product = relationship("Product", back_populates="analysis_results")

class UserProject(Base):
    __tablename__ = "user_projects"
    
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    product_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("products.id"), nullable=False)
    blueprint: Mapped[dict] = mapped_column(JSONB, default={}, server_default='{}')
    status: Mapped[str] = mapped_column(String(50), default="active", server_default="active")
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), index=True)
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), onupdate=text("CURRENT_TIMESTAMP"))
