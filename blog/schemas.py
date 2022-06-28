from typing import List
from pydantic import BaseModel


class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    class Config():
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []

    class Config():
        orm_mode = True

# we can mention the fields which we want to show in the class model.(either title, body or both)
class ShowBlog(BaseModel): # to view fields in api, it is needed to call BaseModel or Blog class instead of Blog
    title: str
    body: str
    creator: ShowUser

    class Config():
        orm_mode = True