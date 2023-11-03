from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.users import user_router


app = FastAPI()
app.title = "Mi aplicacion con FastAPI"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)
base.metadata.create_all(bind=engine)



movies = [
    {
        "id":1,
        "title":"Avatar",
        "overview":"En una ...",
        "year":"2009",
        "rating":7.8,
        "category":"acción"
    },
    {
        "id":3,
        "title":"Avatar",
        "overview":"En una ...",
        "year":"2009",
        "rating":7.8,
        "category":"terror"
    }
]
@app.get('/', tags = ['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')




