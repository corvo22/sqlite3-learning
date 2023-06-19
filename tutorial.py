import sqlite3


def create_database(conn, curs) -> None:
	
	# create a table
	curs.execute("""CREATE TABLE customers (
				first_name TEXT,
				last_name TEXT,
				email TEXT	
		)""")

	# commit and close
	conn.commit()

def main():
	conn = sqlite3.connect('customers.db')
	curs = conn.cursor()

	create_database(conn, curs)

	# add one row to table

	curs.execute("INSERT INTO customers VALUES ('Mary', 'Berry', 'marryberry@test.com')")
	curs.execute("INSERT INTO customers VALUES ('Tom', 'Test', 'tomtest@test.com')")
	curs.execute("INSERT INTO customers VALUES ('Mick', 'Malone', 'mickmalone@test.com')")

	# add many row to table

	list_of_customers = [('Thalia', 'Grace', 'thaliagrace@test.com'), 
						('Percy', 'Jackson', 'percyjackson@test.com'),
						('Anabeth','Chase','anabethchase@test.com'),
						('Jason', 'Grace', 'jasongrace@test.com')]

	curs.executemany("INSERT INTO customers VALUES (?,?,?)", list_of_customers)

	# Query the db Note that fetchone and fetchmany treat the database like a stack. Last entries
	# are the first returned

	# Primary Key / Row ID: ID for each element in the db

	curs.execute("SELECT rowid, * FROM customers")
	print(curs.fetchall())
	record = curs.fetchall()

	# Specific Querries

	curs.execute("SELECT * FROM customers WHERE last_name = 'Grace'")
	print(curs.fetchall())

	# the % serves as a wildcard
	curs.execute("SELECT * FROM customers WHERE last_name LIKE '%e'")
	print(curs.fetchall())

	# Updating Records, must commit afterwards. 
	# This way works, but this would match ANY Malone, to edit 
	# a specific record we should use record ID
	curs.execute(""" UPDATE customers SET first_name = 'Micky'
					WHERE last_name = 'Malone' """)

	curs.execute(""" UPDATE customers SET first_name = 'Johnny'
					WHERE rowid = 2 """)

	conn.commit()

	curs.execute("SELECT rowid, * FROM customers")
	print(curs.fetchall())

	conn.close()

	# Delete / drop from table
	curs.execute("DELETE from customers where rowid = 1")
	conn.commit()


if __name__ == "__main__":
	main()