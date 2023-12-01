import redis

# Создать подключение к редис
redis_db = redis.from_url('redis://localhost')
# создать запись базы данных
redis_db.set('age', 27)
# Получить значение данные из базы
data = redis_db.get('age')
print(data)

# Задать время существования переменной  в базе

redis_db.set("name", "Axad", 5)
data2 = redis_db.get("name")
print(data2)
