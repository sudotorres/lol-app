import sqlalchemy as sa
import sqlalchemy.orm as so
from app.extensions import db

class Champion(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(100))
    title: so.Mapped[str] = so.mapped_column(sa.String(100))
    blurb: so.Mapped[str] = so.mapped_column(sa.Text)
    square: so.Mapped[str] = so.mapped_column(sa.String(255))
    
    def __repr__(self):
        return f"<Champion {self.name}>"