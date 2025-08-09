from pydantic import BaseModel

class CaptionRequest(BaseModel):
    topic: str
    tone: str | None = "professional"


class ImageRequest(BaseModel):
    prompt: str


class PostRequest(BaseModel):
    topic: str
    prompt: str | None = None
