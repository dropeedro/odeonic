import requests
from jose import jwt, JWTError

KEYCLOAK_URL = "http://localhost:8080"  # URL del servidor Keycloak
REALM_NAME = "odeonic-app"  # Nombre de tu Realm en Keycloak

def get_public_key():
    # Obtén la clave pública de Keycloak para verificar los tokens
    url = f"{KEYCLOAK_URL}/realms/{REALM_NAME}/protocol/openid-connect/certs"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["keys"][0]  # Retorna la primera clave pública
    else:
        raise RuntimeError("Could not fetch public key from Keycloak")

def verify_token(token: str):
    try:
        public_key = get_public_key()
        payload = jwt.decode(token, public_key, algorithms=["RS256"])
        return payload
    except JWTError:
        raise ValueError("Invalid token")
