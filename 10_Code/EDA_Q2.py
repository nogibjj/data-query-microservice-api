import helper_db

cursor = helper_db.connect_to_db()
list = []
cursor.execute(
"""SELECT * FROM import.globallandtemperaturesbycountry where country = 'Afghanistan';"""
)
for i in cursor.fetchall():
  list.append(i)