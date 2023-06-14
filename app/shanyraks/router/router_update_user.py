from fastapi import Depends, status

from typing import Any
from pydantic import Field

from app.utils import AppModel

from app.auth.adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from app.auth.router.dependencies import parse_jwt_user_data


class UpdateUserRequest(AppModel):
    city: str
    phone: str
    name: str


class UpdateUserResponse(AppModel):
    id: Any = Field(alias="_id")
    city: str
    phone: str
    name: str


@router.patch(
    "/users/me", status_code=status.HTTP_200_OK, response_model=UpdateUserResponse
)
def update_user(
    input: UpdateUserRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    user = svc.repository.update_user(jwt_data.user_id, input.dict())
    return user
