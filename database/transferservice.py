from datetime import datetime

from database.models import Transfer, UserCard
from database import get_db


# Проверка карты для создание перевода
def validate_card(card_number, db):
    exact_card = db.query(UserCard).filter_by(card_number=card_number).first()
    return exact_card


# Создать перевод денег
def create_transaction_db(card_from, card_to, amount):
    db = next(get_db())

    # Проверка на наличия в базе обеих карт (card_from, card_to)
    checker_card_from = validate_card(card_from, db)
    checker_card_to = validate_card(card_to, db)

    # Если обе карты существуют в базе данных
    if checker_card_from and checker_card_to:
        # Проверка баланса того кто переводит деньги
        if checker_card_from.balance >= amount:
            # Минусуем у того пользовательно кто отправит деньги
            checker_card_from.balance -= amount
            # Добавляем тому кто получает деньги
            checker_card_to.balance += amount

            # Сохраняем в базе
            new_transaction = Transfer(card_from_id=card_from, card_to_id=card_to,
                                       amount=amount, transaction_date=datetime.now())
            db.add(new_transaction)
            db.commit()

            # Выдаем ответ
            return "Перевод успешно выполнен"
        else:
            return "Недостаточно средств на балансе"
    else:
        return "Одна из карт не существует"


# Получить все переводы по карте
def get_card_transaction_db(card_from_id):
    db = next(get_db())

    card_transaction = db.query(Transfer).filter_by(card_from_id=card_from_id).all()

    return card_transaction


# Отменить перевод
def cancel_transfer_db(card_from, card_to, amount, transfer_id):
    pass

    # # Проверка на наличия в базе обеих карт (card_from, card_to)
    # checker_card_from = validate_card(card_from, db)
    # checker_card_to = validate_card(card_to, db)
    #
    # # Если обе карты существуют в базе данных
    # if checker_card_from and checker_card_to:
    #     # Проверка баланса того кто возращает деньги
    #     if checker_card_from.balance >= amount:
    #         # Минусуем у того пользовательно кто отправит деньги
    #         checker_card_from.balance -= amount
    #         # Добавляем тому кто получает деньги
    #         checker_card_to.balance += amount
    #
    #         # Сохраняем в базе
    #         new_transaction = Transfer(card_from_id=card_from, card_to_id=card_to,
    #                                    amount=amount, transaction_date=datetime.now())
    #         db.add(new_transaction)
    #         db.commit()
    #
    #         # Выдаем ответ
    #         return "Перевод успешно выполнен"
    #     else:
    #         return "Недостаточно средств на балансе"
    #






# ОТМЕНА ПЛАТЕЖА!!!!
