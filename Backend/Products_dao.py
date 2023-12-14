from db_connection import get_db_connection
import mysql.connector


def get_products(connections):
    cursor = connections.cursor()
    query = "SELECT * FROM PRODUCTS_VIEW"
    cursor.execute(query)
    result = []
    for (product_name, category_name, price_per_unit) in cursor:
        result.append(
            {
                'product_name': product_name,
                'category_name': category_name,
                'price_per_unit': price_per_unit
            }
        )

    return result


def add_product(connections, new_product):
    try:
        cursor = connections.cursor()

        query_1 = "INSERT INTO PRODUCTS (PRODUCT_NAME) VALUES (%s);"
        data_1 = [new_product['product_name']]
        cursor.execute(query_1, data_1)
        connections.commit()
        print("Product added successfully!!")

    except mysql.connector.Error as err:
        print(f"Error:{err}")
    try:
        query_2 = ("INSERT INTO PRD_CAT (PRODUCT_ID,CATEGORY_ID,PRICE_PER_UNIT) SELECT PRODUCT_ID,%s,"
                   "%s FROM PRODUCTS WHERE PRODUCT_NAME=%s")
        data_2 = [new_product['category_id'],new_product['price_per_unit'], new_product['product_name']]
        cursor.execute(query_2, data_2)
        connections.commit()
        print("Product with category added successfully!!")

    except mysql.connector.Error as err:
        print(f"Unable to complete request!!- Error:{err}")
        return cursor.lastrowid

    finally:
        cursor.close()


def delete_products(connections, delete_product):
    try:
        cursor = connections.cursor()

        query_1 = "DELETE FROM PRD_CAT WHERE PRODUCT_ID IN (SELECT PRODUCT_ID FROM PRODUCTS WHERE PRODUCT_NAME=%s);"
        data_1 = [delete_product['product_name']]

        cursor.execute(query_1, data_1)
        connections.commit()
    except mysql.connector.Error as err:
        err=str(err)
        if "1451" in err:
            print(f"Unable to complete request. There are existing orders in this product category!! Error:{err}")
        else:
            print(f"Error:{err}")
    try:
        query_2 = "DELETE FROM PRODUCTS WHERE PRODUCT_NAME = %s;"
        data_2 = [delete_product['product_name']]
        cursor.execute(query_2, data_2)
        connections.commit()
        print("Product deleted successfully!!")
    except mysql.connector.Error as err:
        print(f"Unable to complete request!!- Error:{err}")
        return cursor.lastrowid

    finally:
        cursor.close()


if __name__ == '__main__':
    connection = get_db_connection()
    print(get_products(connection))
    add_data = {
        'product_name': 'MASK',
        'category_id': '2',
        'price_per_unit': '2'
    }
    (add_product(connection, add_data))
    delete_data = {
        'product_name': 'overcoat',
            }
    delete_products(connection, delete_data)
