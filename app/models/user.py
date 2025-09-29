from pydantic import BaseModel

class User(BaseModel):
    GID: str
    name: str
    email_id: str
    password: str
