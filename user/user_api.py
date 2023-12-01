from fastapi import APIRouter
from datetime import datetime

from database.userservice import register_user_db, edit_user_db, delete_user_db, get_exact_user_db, check_user_email_db

from user import UserRegisterValidator, EditUserValidator

user_router = APIRouter(prefix='/user', tags=['Работа с пользователем'])

# Регистрацию пользователя
@user_router.post('/register')
async def register_user(data: UserRegisterValidator):
    # Переводим из типа pydantic в обычный словарь
    new_user_data = data.model_dump()

    # Вызов функции для проверки почты в базе
    checker = check_user_email_db(data.email)

    # Если нет в базе такого email пользователя, то добавляем
    if not checker:
        result = register_user_db(reg_date=datetime.now(), **new_user_data)
        return {'message': result}
    else:
        return {'message': 'Пользователь уже с таким email существует'}

# Получения информации о пользователе
@user_router.get('/info')
async def get_user(user_id: int):
    result = get_exact_user_db(user_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Такого пользователя нету. Жаль'}

# Изменить данные пользователя
@user_router.put('/edit-data')
async def edit_user(data: EditUserValidator):
    # переводим из pydantic на простой словарь
    change_data = data.model_dump()

    result = edit_user_db(**change_data)

    return {'message': result}

# Удаления пользователя
@user_router.delete('/delete-user')
async def delete_user(user_id: int):
    result = delete_user_db(user_id)

    if result:
        return {'message': 'Пользователь удален'}
    else:
        return {'message': 'Такого пользователя нету я не могу удалить'}