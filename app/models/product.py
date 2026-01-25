import uuid
from sqlalchemy import String, Numeric, Integer, Date, TIMESTAMP, Text, text
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime, date
from typing import Optional
from app.database import Base

class Product(Base):
    __tablename__ = "products"
    
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    codecanyon_id: Mapped[str] = mapped_column(String(100), unique=True, nullable=False, index=True)
    url: Mapped[str] = mapped_column(Text, nullable=False)
    title: Mapped[str] = mapped_column(String(500), nullable=False)
    slug: Mapped[str] = mapped_column(String(500), nullable=False)
    category: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    subcategory: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    price: Mapped[Optional[float]] = mapped_column(Numeric(10, 2), nullable=True)
    total_sales: Mapped[int] = mapped_column(Integer, default=0, server_default="0", index=True)
    rating: Mapped[Optional[float]] = mapped_column(Numeric(3, 2), nullable=True)
    review_count: Mapped[int] = mapped_column(Integer, default=0, server_default="0")
    launch_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    last_update_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    author_name: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    author_id: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    technologies: Mapped[list] = mapped_column(JSONB, default=[], server_default='[]')
    features: Mapped[list] = mapped_column(JSONB, default=[], server_default='[]')
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    screenshots: Mapped[list] = mapped_column(JSONB, default=[], server_default='[]')
    profitability_score: Mapped[Optional[float]] = mapped_column(Numeric(5, 2), nullable=True, index=True)
    sales_velocity: Mapped[Optional[float]] = mapped_column(Numeric(10, 2), nullable=True)
    revenue_potential: Mapped[Optional[float]] = mapped_column(Numeric(12, 2), nullable=True)
    market_saturation: Mapped[Optional[float]] = mapped_column(Numeric(5, 2), nullable=True)
    scraped_at: Mapped[Optional[datetime]] = mapped_column(TIMESTAMP, nullable=True)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), index=True)
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), onupdate=text("CURRENT_TIMESTAMP"))
    product_metadata: Mapped[dict] = mapped_column(JSONB, default={}, server_default='{}')
