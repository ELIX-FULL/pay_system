# должны сделать роутеры для
# 1. Запрос на добавления карты - async def add_new_card()
# 2. Запрос на получения информации об определенной карте определенного пользователя
from fastapi import APIRouter
from datetime import datetime
from database.cardservice import add_card_db, get_exact_user_cards_db, delete_card_db, check_card_db, get_exact_card_db
from card import CardAddValidator


card_router = APIRouter(prefix='/card', tags=['Работа с Картами'])

@card_router.put('/add-card')
async def add_new_card_router(data: CardAddValidator):
    new_card_data = data.model_dump
    checker = check_card_db(data.card_number)

# Если нет в базе такой карты пользователя, то добавляем
    if not checker:
        result = add_card_db(exp_date=datetime.now(), **new_card_data)
        return {'message': result}
    else:
        return {'message': 'Пользователь уже с такой картой уже имеется'}
# Роутер показания всех карт по id пользователя
@card_router.get('/get-card-id')
async def get_exact_user_cards(user_id: int):
    user_cards = get_exact_user_cards_db(user_id)
    if user_cards:
        return {"user_cards": user_cards}
    else:
        return {'message': 'Пользователь не добавлял карт'}

# Роутер определенной карты пользователя по id карты и id пользовтеля
@card_router.get("/get-exact-card")
async def get_exact_card(user_id: int, card_id: int):
    exact_card = get_exact_card_db(user_id, card_id)
    if exact_card:
        return {"exact_card": exact_card}
    else:
        return {'message': 'У пользователя нету карты или неверен id'}


# роутер удаления карты
@card_router.delete("/delete-card-number")
async def delete_card(card_number: int):
    result = delete_card_db(card_number)
    if result:
        return {"message": result}
    else:
        return {'message': 'Такой карты не существует'}
