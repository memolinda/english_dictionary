import mysql.connector
import difflib
from difflib import get_close_matches

connection = mysql.connector.connect(
    user = 'ardit700_student',
    password = 'ardit700_student',
    host = '108.167.140.122',
    database = 'ardit700_pm1database'
)

cursor = connection.cursor()

word = input("Enter a word: ")

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()



if results:
    for result in results:
        print(result[1])

# elif len(get_close_matches(word, results[0]))>0:
#     print('Did you mean %s instead?' % get_close_matches(word, results[0])[0])
else:
    print("No word found!")