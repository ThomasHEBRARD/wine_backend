from datetime import datetime

from rest_framework_jwt.settings import api_settings


def create_token(user, expiration_delta=api_settings.JWT_EXPIRATION_DELTA):
    payload = api_settings.JWT_PAYLOAD_HANDLER(user)
    if expiration_delta:
        payload["exp"] = datetime.utcnow() + expiration_delta
    else:
        del payload["exp"]
    return api_settings.JWT_ENCODE_HANDLER(payload)
