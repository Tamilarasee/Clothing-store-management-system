from db_connection import get_db_connection
import mysql.connector


def get_category(connections):
    cursor = connections.cursor()
    query = "SELECT * FROM CATEGORY"
    cursor.execute(query)
    result = []
    for (category_id, category_name) in cursor:
        result.append(
            {
                'category_id': category_id,
                'category_name': category_name
            }
        )

    return result

if __name__ == '__main__':
    from db_connection import get_db_connection

    connection = get_db_connection()
    # print(get_all_products(connection))
    print(get_category(connection))