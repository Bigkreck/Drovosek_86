import sqlite3


class SQLiconnect:

    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    # Добавляем нового пользователя в БД
    def add_user(self, user_id, user_name, first_name):
        with self.connection:
            return self.cursor.execute('INSERT INTO `users` (`user_id`, `user_name`, `first_name`) VALUES '
                                       '(?,?,?)', (user_id, user_name, first_name)).fetchall()

    def add_products(self, name, price, image, type, description):
        with self.connection:
            return self.cursor.execute('INSERT INTO `products` (name, price, image, types, description) '
                                       'VALUES (?,?,?,?)', (name, price, image, type, description)).fetchall()

    def get_products(self, name):
        with self.connection:
            return self.cursor.execute('SELECT * FOR products WHERE name = ?', (name, )).fetchall()

    def get_product_image(self, type):
        with self.connection:
            return self.cursor.execute('SELECT * FROM images WHERE type = ?', (type, )).fetchall()

    def get_user(self, user_id):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id, )).fetchall()
            return bool(len(result))

    def add_image(self, image_id, types):
        with self.connection:
            return self.cursor.execute('INSERT INTO `images` (`file_id`, `type`) VALUES (?,?)',
                                         (image_id, types)).fetchall()

    def close_connect(self):
        self.connection.close()
