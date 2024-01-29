from pydantic import BaseModel, Field, PrivateAttr

class Test(BaseModel):
    field: str = Field(description="My field")
    _field: str = PrivateAttr()
    
    def __init__(self, **data):
        super().__init__(**data)
        self._field = self.field