import mysql.connector

__cnx = None


# Database Configuration
def get_db_connection():
    global __cnx
    if __cnx is None:
        db_config = {
                'host': 'localhost',
                'user': 'root',
                'password': 'root',
                'database': 'clothing_store_mgmt_system',
            }

    __cnx = mysql.connector.connect(**db_config)

    return __cnx
