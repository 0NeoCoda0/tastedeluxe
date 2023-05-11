import csv
import psycopg2
import os

conn = psycopg2.connect(
    host="localhost",
    database="tastedeluxe",
    user="aishat",
    password="=0Ze=!g)pi>WU~0"
)
cur = conn.cursor()
file_list = []
dirlist = os.listdir()

for filename in dirlist:
    if '.csv' in filename:
        file_list.append(filename)

def write_data(file_name):
    # Открытие курсора для выполнения запросов к базе данных
    
    # Чтение данных из CSV файла и вставка их в базу данных
    with open(file_name, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)  # пропускаем заголовок файла
        for row in reader:
            cur.execute(
                "INSERT INTO products_productcard (name, price, image, category, food_type) VALUES (%s, %s, %s, %s, %s);",
                (row[0], row[1], row[2], row[3], row[4]))
    # Сохранение изменений в базе данных и закрытие соединения
    


for name in file_list:
    write_data(name)

conn.commit()
cur.close()
conn.close()