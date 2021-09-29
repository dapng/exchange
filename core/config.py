from mmap import ACCESS_COPY
from starlette.config import Config


config = Config(".env")


DATABASE_URL = config("EE_DATABASE_URL", cast=str, default="")
ACCESS_TOKEN_EXPIRE_MINUTES = 60
ALGORITHM = "HS256"
SECRET_KEY = config("EE_SECRET_KEY", cast=str, default="74b8a54869f764c5ef86de33846a1b5c5fd191babcf771a4607d6c0652a3acb2")