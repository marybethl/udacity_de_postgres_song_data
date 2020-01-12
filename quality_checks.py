import psycopg2

#TODO: Clean-up stackoverflow references and comment out better

def databaseSummary(cur):
	""" 
	Function that will print tables in the database.
	For use after check_tables.py is completed.
	This assures tables were created as there's no
	log in check_tables.py

	Parameters:
    - cur: connection to database
	"""

	# create sparkify database with UTF8 encoding
	cur.execute("SELECT table_name FROM information_schema.tables WHERE TABLE_TYPE = 'BASE TABLE' \
	AND TABLE_SCHEMA not in ('pg_catalog','information_schema');")

	#https://stackoverflow.com/questions/18495737/why-do-i-get-extra-commas-in-my-python-slqlite-select-results
	#result = cur.fetchall()

	result = [row[0] for row in cur.fetchall()]
	print('Tables in Database: %s' % table_names)

#https://stackoverflow.com/questions/1349332/python-passing-a-function-into-another-function
def summarizeTables(cur, table_names):
	"""
	Function that will loop through tables output
	from databaseSummary function.
	Will print out a summary of columns in each table
	"""

	# create sparkify database with UTF8 encoding
	for i in table_names:
		#print(i)
		table_name = i
		sql = "SELECT column_name FROM information_schema.columns WHERE table_name = %s;"

		#https://stackoverflow.com/questions/28117576/python-psycopg2-where-in-statement 
		#print(cur.mogrify(sql, (table_name,)))
		#morgify helpful

		cur.execute(sql, (table_name,))
		column_names = [row[0] for row in cur.fetchall()]
		
		#combine strings
		table_phrase = "Columns in Table: " + i
		print(table_phrase)
		print(column_names)
		print("\n")


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    databaseSummary(cur)
    summarizeTables(cur, databaseSummary(cur))

    conn.close()

if __name__ == "__main__":
    main()
