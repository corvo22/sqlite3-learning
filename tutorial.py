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
	curs.execute("INSERT INTO customers VALUES ('Mary', 'Berry', 'marryberry@test.com')")
	curs.execute("INSERT INTO customers VALUES ('Tom', 'Test', 'tomtest@test.com')")
	curs.execute("INSERT INTO customers VALUES ('Mick', 'Malone', 'mickmalone@test.com')")

	conn.close()
if __name__ == "__main__":
	main()
