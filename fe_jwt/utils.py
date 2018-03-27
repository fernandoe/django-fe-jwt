from rest_framework_jwt.utils import jwt_payload_handler


def fe_jwt_payload_handler(user):
    result = jwt_payload_handler(user)
    if user.entity is not None:
        result['entity'] = str(user.entity.pk)
    return result
