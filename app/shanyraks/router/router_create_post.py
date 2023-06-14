from fastapi import Depends, status, Response

from app.utils import AppModel

from app.auth.adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from app.auth.router.dependencies import parse_jwt_user_data


class CreatePostRequest(AppModel):
    type: str
    price: int
    address: str
    area: float
    rooms_count: int
    description: str


@router.post("/", status_code=status.HTTP_200_OK)
def create_post(
    input: CreatePostRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    post = svc.repository.create_post(jwt_data.user_id, input.dict())
    return Response("post_id: " + str(post))
