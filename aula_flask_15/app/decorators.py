from functools import wraps
from flask import abort
from flask_login import current_user
from app.models import Permissao

def pode_ver(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if current_user.papel.verifica_perm(Permissao.VER):
            return f(*args, **kwargs)
        abort(403)
    return wrap

def verificar_permissao(permissao: int):
    def decorator(f):
        @wraps(f)
        def wrap(*args, **kwargs):
            if current_user.papel.verifica_perm(permissao):
                return f(*args, **kwargs)
            abort(403)
        return wrap        
    return decorator

def verificar_papel(papel: str):
    def decorator(f):
        @wraps(f)
        def wrap(*args, **kwargs):
            if current_user.papel.nome == papel:
                return f(*args, **kwargs)
            abort(403)
        return wrap
    return decorator
       