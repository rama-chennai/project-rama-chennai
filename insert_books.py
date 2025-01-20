import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="bookscape"
        )
        if connection.is_connected():
            print("Successfully connected to MySQL")
            return connection
    except Error as err:
        print(f"Error: {err}")
        return None

def insert_book_data(connection, book_data):
    cursor = connection.cursor()
    insert_query = """
    INSERT INTO books (book_id, search_key, book_title, book_subtitle, book_authors, 
                       book_description, industryIdentifiers, text_readingModes, image_readingModes, 
                       pageCount, categories, language, imageLinks, ratingsCount, averageRating, country, 
                       saleability, isEbook, amount_listPrice, currencyCode_listPrice, amount_retailPrice, 
                       currencyCode_retailPrice, buyLink, year)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, book_data)
    connection.commit()
    cursor.close()
    print("Book data inserted successfully.")

