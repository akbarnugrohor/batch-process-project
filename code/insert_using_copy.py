import psycopg2

conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=akbar8")
cur = conn.cursor()

# create table

cur.execute("""
            create table if not exists users_using_copy(
                id serial primary key,
            email text,
            name text,
            phone text,
            postal_code text
            ) 
            """)

conn.commit()

# insert data

with open(r"C:\Users\akbar\Documents\DigitalSkola - Data Engineer\Project\Project 3\source\users_w_postal_code.csv","r") as f:
    next(f)
    cur.copy_from(f,"users_using_copy",sep=",",columns=("email","name","phone","postal_code"))

conn.commit()