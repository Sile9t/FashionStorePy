from typing import List, Optional
from pydantic import BaseModel, ConfigDict, EmailStr, Field

# roles will be applied with permit.io

"""
    User dto models
"""
class UserAbsDto(BaseModel):
    username: str
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class UserCreateDto(UserAbsDto):
    password: str


#TODO: add user birth_date and age fields
class UserDto(UserAbsDto):
    id: int = Field(frozen=True)
    

"""
    Brand dto models
"""
class BrandDto(BaseModel):
    id: int = Field(frozen=True)
    name: str
    country: str
    website: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


"""
    Clothing type dto models
"""
class ClothingTypeDto(BaseModel):
    id: int = Field(frozen=True)
    name: str

    model_config = ConfigDict(from_attributes=True)


"""
    Clothing dto models
"""
class ClothingDto(BaseModel):
    id: int = Field(frozen=True)
    name: str
    description: Optional[str] = None
    brand_id: int
    brand: Optional[BrandDto] = None
    type_id: int
    type: Optional[ClothingTypeDto] = None
    price: float = Field(ge=0)

    model_config = ConfigDict(from_attributes=True)
