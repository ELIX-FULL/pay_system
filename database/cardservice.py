from datetime import datetime
from database import get_db
from database.models import UserCard


# Добавления карты
def add_card_db(user_id, card_number, balance, card_name, exp_date):
    db = next(get_db())

    new_card = UserCard(user_id=user_id, card_number=card_number,
                        balance=balance, card_name=card_name,
                        exp_date=exp_date)
    db.add(new_card)
    db.commit()

    return 'Карта успешно добавлено'


# Вывести все карты определенного пользователя через user_id
def get_exact_user_cards_db(user_id):
    db = next(get_db())

    exact_user_cards = db.query(UserCard).filter_by(user_id=user_id).first()

    return exact_user_cards


# Вывести определенную карту
def get_exact_card_db(user_id, card_id):
    db = next(get_db())

    exact_user_card = db.query(UserCard).filter_by(user_id=user_id, card_id=card_id).first()

    return exact_user_card

# Проверка карты на наличия в БД
def check_card_db(card_number):
    db = next(get_db())

    checker = db.query(UserCard).filter_by(card_number=card_number).first()

    return checker


# Удаления карту
def delete_card_db(card_id):
    db = next(get_db())

    delete_card = db.query(UserCard).filter_by(card_id=card_id).first()

    if delete_card:
        db.delete(delete_card)
        db.commit()

        return 'Карта успешно удален'
    else:
        return 'Карта не найдено!'
