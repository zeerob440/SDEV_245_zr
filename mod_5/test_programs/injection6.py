import sqlite3

user_id = input('enter id')

connect_db = sqlite3.connect('mod_5/test_programs/the_database.db')
db_cursor = connect_db.cursor()
# create SQL query string with placeholder
query_string: str='SELECT * FROM users WHERE user_id = ?'
# use parameterized input
db_cursor.execute(query_string, (user_id,))

result = db_cursor.fetchone()

print(result)