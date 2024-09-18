from pydantic import BaseModel


class UserRegister(BaseModel):
    username: str
    fullname: str
    email: str
    password: str
    retrain_password: str


