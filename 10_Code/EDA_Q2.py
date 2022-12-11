import helper_db

cursor = helper_db.connect_to_db()
list1 = []
cursor.execute(
"""SELECT * FROM import.temp_clean;"""
)
for i in cursor.fetchall():
  list1.append(i)

print(list1)