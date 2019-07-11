import pymysql
import dbconfig

connection = pymysql.connect(host = 'localhost',
							 user = dbconfig.db_user,
							 passwd = dbconfig.db_password)

try:
	with connection.cursor() as cursor:
		sql = "CREATE DATABASE IF NOT EXISTS homelesscats"
		cursor.execute(sql)

		sql = """
		CREATE TABLE IF NOT EXISTS homelesscats.cats
		(
		id INT NOT NULL AUTO_INCREMENT,
		latitude FLOAT(10,6),
		longtitude FLOAT(10,6),
		date DATETIME,
		quantity INT NOT NULL,
		description VARCHAR(1000),
		updated_at TIMESTAMP,
		PRIMARY KEY (id)
		)
		"""
		cursor.execute(sql)
		connection.commit()
finally:
	connection.close()
