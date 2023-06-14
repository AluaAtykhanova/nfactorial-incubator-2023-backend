from fastapi import Depends, status, Response

from app.auth.adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from app.auth.router.dependencies import parse_jwt_user_data


@router.delete("/{post_id:str}", status_code=status.HTTP_200_OK)
def delete_my_post(
    post_id: str,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    svc.repository.delete_post(post_id)
    return {"message": "Ресурс успешно удален"}
