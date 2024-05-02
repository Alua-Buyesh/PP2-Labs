import psycopg2
import csv

def connect_to_db():
    try:
        conn = psycopg2.connect(
            database="Tsis10db",
            user="postgres",
            host="localhost",
            password="1234",
            port=5433
        )
        return conn
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        return None

def upload_from_csv(conn, filename):
    try:
        cur = conn.cursor()
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if len(row[2])<12:
                    insert_or_update_user(conn,row[0],row[1],row[2])
        conn.commit()
        cur.close()
        print("Data uploaded from CSV successfully.")
    except (psycopg2.Error, FileNotFoundError) as e:
        print("Error uploading data from CSV:", e)

def create_phonebook_table(conn):
    try:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS phonebook (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                phone_number VARCHAR(11),
                UNIQUE (first_name, last_name)
            );
        """)
        conn.commit()
        cur.close()
        print("PhoneBook table created successfully.")
    except psycopg2.Error as e:
        print("Error creating PhoneBook table:", e)



def insert_or_update_user(conn, first_name, last_name, phone_number):
    try:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO phonebook (first_name, last_name, phone_number) 
            VALUES (%s, %s, %s)
            ON CONFLICT (first_name, last_name)
            DO UPDATE SET phone_number = EXCLUDED.phone_number;
        """, (first_name, last_name, phone_number))
        conn.commit()
        print("User inserted or updated successfully")
    except psycopg2.Error:
        cur = conn.cursor()
        cur.execute("""
            ALTER TABLE phonebook
            ADD CONSTRAINT unique_name_combination UNIQUE (first_name, last_name);

        """)
        conn.commit()
        print("Error fixed. Try again")



def insert_from_console(conn):
    try:
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        phone_number = input("Enter phone number:")
        if first_name and last_name and phone_number:
            insert_or_update_user(conn, first_name, last_name, phone_number)
    except psycopg2.Error as e:
        print("Error inserting/updating data from console:", e)

def search_records(conn, pattern):
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT * FROM phonebook 
            WHERE first_name ILIKE %s 
            OR last_name ILIKE %s 
            OR phone_number ILIKE %s;
        """, (f'%{pattern}%', f'%{pattern}%', f'%{pattern}%'))
        rows = cur.fetchall()
        for row in rows:
            print(row)
        print("Search completed successfully")
    except psycopg2.Error as e:
        print("Error searching records:", e)

def delete_data(conn, pattern):
    try:
        cur = conn.cursor()
        cur.execute("""
            DELETE FROM phonebook 
            WHERE first_name ILIKE %s 
            OR last_name ILIKE %s 
            OR phone_number LIKE %s;
        """, (f'%{pattern}%', f'%{pattern}%', f'%{pattern}%'))
        conn.commit()
        print("Data deleted successfully")
    except psycopg2.Error as e:
        print("Error deleting data:", e)

def show_table(conn):
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM phonebook;")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
    except psycopg2.Error as e:
        print("Error displaying table:", e)


def main():
    conn = connect_to_db()
    
    
    if conn:
        create_phonebook_table(conn)
        insert_from_console(conn)
        upload_from_csv(conn, 'Tsis10/contacts2.csv')
        print("Do you want to delete a name? YES/NO")
        c = input()
        if c == "YES":
            username = input("Enter the first name or last name to delete: ")
            delete_data(conn, username)

        print("Do you want to record? YES/NO")
        c = input()
        if c == "YES":
            username = input("Enter the first name or last name: ")
            search_records(conn, username)
        show_table(conn)
        conn.close()

            
            

if __name__ == "__main__":
    main()
