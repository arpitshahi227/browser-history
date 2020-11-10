from . import backend as backend
from .backends import fail as fail
from typing import Any, Optional

log: Any

def set_keyring(keyring: Any) -> None: ...
def get_keyring(): ...
def disable() -> None: ...
def get_password(service_name: Any, username: Any): ...
def set_password(service_name: Any, username: Any, password: Any) -> None: ...
def delete_password(service_name: Any, username: Any) -> None: ...
def get_credential(service_name: Any, username: Any): ...
def recommended(backend: Any): ...
def init_backend(limit: Optional[Any] = ...) -> None: ...
def load_keyring(keyring_name: Any): ...
def load_env(): ...
def load_config(): ...
