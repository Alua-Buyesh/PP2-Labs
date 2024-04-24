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

def create_phonebook_table(conn):
    try:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS PhoneBook (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                phone_number VARCHAR(15)
            );
        """)
        conn.commit()
        cur.close()
        print("PhoneBook table created successfully.")
    except psycopg2.Error as e:
        print("Error creating PhoneBook table:", e)

def upload_from_csv(conn, filename):
    try:
        cur = conn.cursor()
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            for row in reader:
                cur.execute(
                    "INSERT INTO PhoneBook (first_name, last_name, phone_number) VALUES (%s, %s, %s)",
                    (row[0], row[1], row[2])
                )
        conn.commit()
        cur.close()
        print("Data uploaded from CSV successfully.")
    except (psycopg2.Error, FileNotFoundError) as e:
        print("Error uploading data from CSV:", e)

def insert_from_console(conn):
    try:
        cur = conn.cursor()
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        phone_number = input("Enter phone number: ")
        cur.execute(
            "INSERT INTO PhoneBook (first_name, last_name, phone_number) VALUES (%s, %s, %s)",
            (first_name, last_name, phone_number)
        )
        conn.commit()
        cur.close()
        print("Data inserted from console successfully.")
    except psycopg2.Error as e:
        print("Error inserting data from console:", e)



def main():
    conn = connect_to_db()
    if conn:
        create_phonebook_table(conn)
        upload_from_csv(conn, 'contacts.csv')
        insert_from_console(conn)
        conn.close()

if __name__ == "__main__":
    main()