import psycopg2

conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=akbar8")
cur = conn.cursor()

# create table

cur.execute("""
            create table if not exists latihan_table(
                id serial primary key,
            email text,
            name text,
            phone text,
            postal_code text
            ) 
            """)

conn.commit()