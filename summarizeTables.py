import psycopg2

conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
cur = conn.cursor()

cur.execute("SELECT table_name FROM information_schema.tables WHERE TABLE_TYPE = 'BASE TABLE' \
AND TABLE_SCHEMA not in ('pg_catalog','information_schema');")

#https://stackoverflow.com/questions/18495737/why-do-i-get-extra-commas-in-my-python-slqlite-select-results
#result = cur.fetchall()

table_names = [row[0] for row in cur.fetchall()]

#cur.execute("SELECT column_name, data_type, is_nullable FROM information_schema.columns WHERE table_name = 'songs';")
#result = cur.fetchall()

print('Tables in Database: %s' % table_names)

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

	
	