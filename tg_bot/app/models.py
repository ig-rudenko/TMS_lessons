from datetime import datetime
from typing import Optional, Sequence, Self

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Table, select, desc
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import backref, relationship
from sqlalchemy.orm import mapped_column

from app.database.base import Base, Manager
from app.database.connector import db_conn


class User(Base, Manager):
    __tablename__ = "users_user"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(150), unique=True)
    first_name: Mapped[Optional[str]] = mapped_column(String(150))
    last_name: Mapped[Optional[str]] = mapped_column(String(150))
    email: Mapped[str] = mapped_column(String(254))
    password: Mapped[str] = mapped_column(String(128))
    last_login: Mapped[Optional[datetime]] = mapped_column()
    is_superuser: Mapped[bool] = mapped_column(default=False)
    is_staff: Mapped[bool] = mapped_column(default=False)
    is_active: Mapped[bool] = mapped_column(default=True)
    date_join: Mapped[Optional[datetime]] = mapped_column()
    tg_id: Mapped[Optional[int]] = mapped_column(unique=True)


class Ingredient(Base, Manager):
    __tablename__ = "app_ingredient"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))

    def __str__(self) -> str:
        return self.name


recipe_ingredients = Table(
    "app_recipe_ingredients",
    Base.metadata,
    Column("recipe_id", Integer, ForeignKey("app_recipe.id")),
    Column("ingredient_id", Integer, ForeignKey("app_ingredient.id")),
)


class Recipe(Base, Manager):
    __tablename__ = "app_recipe"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), comment="Название рецепта")
    description: Mapped[str] = mapped_column(String, comment="Описание рецепта")
    preview_image: Mapped[str] = mapped_column(String(255), comment="Картинка")
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    time_minutes: Mapped[int] = mapped_column(default=1, comment="Время приготовления")
    user_id: Mapped[int] = mapped_column(ForeignKey("users_user.id"))
    user = relationship(User, backref=backref("recipes", uselist=True))
    ingredients = relationship(Ingredient, secondary=recipe_ingredients, backref="recipes", uselist=True)
    category: Mapped[str] = mapped_column(String(1))

    __mapper_args__ = {
        "polymorphic_on": category,  # Optional for polymorphic relationships (if needed)
    }

    @classmethod
    async def first_10(cls) -> Sequence[Self]:
        async with db_conn.session as session:
            result = await session.execute(select(cls).order_by(desc(Recipe.created_at)).limit(10))
            return result.scalars().all()
