from typing import Any
from pydantic import Field


from fastapi import Depends, status


from app.utils import AppModel

from app.auth.adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from app.auth.router.dependencies import parse_jwt_user_data


class GetMyPostResponse(AppModel):
    id: Any = Field(alias="_id")
    type: str
    price: int
    address: str
    area: float
    rooms_count: int
    description: str
    user_id: Any


@router.get(
    "/{post_id:str}", status_code=status.HTTP_200_OK, response_model=GetMyPostResponse
)
def get_my_post(
    post_id: str,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> GetMyPostResponse:
    post = svc.repository.get_post_by_id(post_id)
    return GetMyPostResponse(**post)
