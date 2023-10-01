from pydantic import BaseModel, Field
from typing import  Optional, List




class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(default="Mi pelicula", min_length=5, max_length=15)
    overview: str = Field(default="Descripcion de la pelicula", min_length=15, max_length=50)
    year: int = Field(default=2023, le=2023)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=3, max_length=20)

    class Config:
        schema_extra = {
            "Example":{
                "id":1,
                "title":"Mi pelicula",
                "overview":"Descripcion de la pelicula",
                "year":"2023",
                "rating":7.8,
                "category":"acción"

            }
        }
