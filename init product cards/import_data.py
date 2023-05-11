import csv
import psycopg2

# Соединение с базой данных PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="tastedeluxe",
    user="aishat",
    password="=0Ze=!g)pi>WU~0"
)

# Открытие курсора для выполнения запросов к базе данных
cur = conn.cursor()

# Чтение данных из CSV файла и вставка их в базу данных
with open('hot-food.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)  # пропускаем заголовок файла
    for row in reader:
        cur.execute(
            "INSERT INTO products_productcard (name, price, image, category, food_type) VALUES (%s, %s, %s, %s, %s);",
            (row[0], row[1], row[2], row[3], row[4])
        )

# Сохранение изменений в базе данных и закрытие соединения
conn.commit()
cur.close()
conn.close()
