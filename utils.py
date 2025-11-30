# utils.py
import os
import time
import uuid
import hashlib
import requests

# Config: default değerler, değiştirilebilir
API_BASE = os.environ.get("CPM_API_BASE", "https://example-cpm-api.local")
TIMEOUT = 10

class APIClient:
    def __init__(self, base_url=None, token=None):
        self.base_url = base_url or API_BASE
        self.token = token

    def _headers(self):
        h = {"User-Agent": "CPMTool/1.0"}
        if self.token:
            h["Authorization"] = f"Bearer {self.token}"
        return h

    def post(self, path, data=None, json=None):
        url = f"{self.base_url.rstrip('/')}/{path.lstrip('/')}"
        resp = requests.post(url, data=data, json=json, headers=self._headers(), timeout=TIMEOUT)
        return resp

    def get(self, path, params=None):
        url = f"{self.base_url.rstrip('/')}/{path.lstrip('/')}"
        resp = requests.get(url, params=params, headers=self._headers(), timeout=TIMEOUT)
        return resp

def generate_fingerprint():
    """
    Basit fingerprint: cihaz/bilgiye bağlı benzersiz ID.
    Reelde daha sofistike olabilir; burada deterministic bir hash üretiyoruz.
    """
    # Kullanıcının makine UUID'si (yerel), zaman damgası + rastgele karışımı
    node = uuid.getnode()
    raw = f"{node}-{os.getpid()}-{time.time()}"
    h = hashlib.sha256(raw.encode()).hexdigest()
    # kısa versiyon
    return h[:32]

def verificar_key_com_fingerprint(api_client: APIClient, key: str, fingerprint: str):
    """
    Sunucuya key + fingerprint doğrulaması gönderir.
    Eğer sunucuda uygun endpoint yoksa bunu sahte/mock olarak kullan.
    """
    try:
        resp = api_client.post("/verify_key", json={"key": key, "fingerprint": fingerprint})
        if resp.status_code == 200:
            return resp.json()
        return {"ok": False, "status_code": resp.status_code, "text": resp.text}
    except Exception as e:
        return {"ok": False, "error": str(e)}

def login(api_client: APIClient, username: str, password: str):
    try:
        resp = api_client.post("/auth/login", json={"username": username, "password": password})
        if resp.status_code == 200:
            data = resp.json()
            token = data.get("token") or data.get("access_token")
            api_client.token = token
            return {"ok": True, "data": data}
        return {"ok": False, "status_code": resp.status_code, "text": resp.text}
    except Exception as e:
        return {"ok": False, "error": str(e)}
