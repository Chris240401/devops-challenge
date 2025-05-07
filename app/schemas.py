from pydantic import BaseModel, Field

class Message(BaseModel):
    message: str
    to: str
    from_: str = Field(..., alias="from")
    timeToLifeSec: int

    model_config = {
        "populate_by_name": True
    }
