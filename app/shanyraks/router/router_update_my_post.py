from fastapi import Depends, status

from typing import Any
from pydantic import Field

from app.utils import AppModel

from app.auth.adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from app.auth.router.dependencies import parse_jwt_user_data


class UpdateMyPostRequest(AppModel):
    type: str
    price: int
    address: str
    area: float
    rooms_count: int
    description: str


class UpdateMyPostResponse(AppModel):
    id: Any = Field(alias="_id")
    type: str
    price: int
    address: str
    area: float
    rooms_count: int
    description: str


@router.patch(
    "/{post_id:str}",
    status_code=status.HTTP_200_OK,
    response_model=UpdateMyPostResponse,
)
def update_my_post(
    post_id: str,
    input: UpdateMyPostRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    post = svc.repository.update_post_by_id(post_id, input.dict())
    return post
