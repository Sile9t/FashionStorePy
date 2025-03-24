from typing import List
from pydantic import BaseModel, ConfigDict, EmailStr, Field

# roles will be applied with permit.io

"""
    User dto models
"""
class UserAbsDto(BaseModel):
    username: str
    email: EmailStr
    first_name: str | None
    last_name: str | None
    phone: str | None
    address: str | None

    config = ConfigDict(from_attributes=True)


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
    website: str | None

    config = ConfigDict(from_attributes=True)


"""
    Clothing type dto models
"""
class ClothingTypeDto(BaseModel):
    id: int = Field(frozen=True)
    name: str

    config = ConfigDict(from_attributes=True)


"""
    Clothing dto models
"""
class ClothingDto(BaseModel):
    id: int = Field(frozen=True)
    name: str
    description: str | None
    brand_id: int
    brand: BrandDto | None
    type_id: int
    type: ClothingTypeDto | None
    price: float = Field(ge=0)

    config = ConfigDict(from_attributes=True)
