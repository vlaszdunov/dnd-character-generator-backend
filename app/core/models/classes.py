from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ARRAY, String
from .base import Base


class UnitClass(Base):
    __tablename__ = "unit_classes"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    hit_dice: Mapped[int] = mapped_column(nullable=False)
    armor_proficiency: Mapped[str] = mapped_column(nullable=False)
    weapons_proficiency: Mapped[str] = mapped_column(nullable=False)
    tools_proficiency: Mapped[str] = mapped_column()
    saving_throws: Mapped[list[str]] = mapped_column(ARRAY(String), nullable=False)
    skills: Mapped[list[str]] = mapped_column(ARRAY(String), nullable=False)
