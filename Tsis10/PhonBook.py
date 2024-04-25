import psycopg2
import csv, sqlite3

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

def get_next_id(conn):
    try:
        cur = conn.cursor()
        cur.execute("SELECT id FROM PhoneBook WHERE id IS NOT NULL")
        ids = [row[0] for row in cur.fetchall()]
        cur.close()

        if not ids:
            return 1

        next_id = min(set(range(1, max(ids) + 2)) - set(ids))
        return next_id
    except psycopg2.Error as e:
        print("Error getting next ID:", e)
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
            next(reader)
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
        next_id = get_next_id(conn)
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        phone_number = input("Enter phone number: ")
        cur.execute(
            "INSERT INTO PhoneBook (id, first_name, last_name, phone_number) VALUES (%s, %s, %s, %s)",
            (next_id, first_name, last_name, phone_number)
        )
        conn.commit()
        cur.close()
        print("Data inserted from console successfully.")
    except psycopg2.Error as e:
        print("Error inserting data from console:", e)

def update_data_number(conn):
    try:
        cur = conn.cursor()
        user_id = input("Enter user ID to update: ")
        new_phone_number = input("Enter new phone number: ")
        new_phone_number = new_phone_number.strip()
        cur.execute(
            "UPDATE PhoneBook SET phone_number = %s WHERE id = %s",
            (new_phone_number, user_id)
        )
        conn.commit()
        cur.close()
        print("Data updated successfully.")
    except psycopg2.Error as e:
        print("Error updating data:", e)

def update_data_name(conn):
    try:
        cur = conn.cursor()
        user_id = input("Enter user ID to update: ")
        new_first_name = input("Enter new first name: ")
        cur.execute(
            "UPDATE PhoneBook SET first_name = %s WHERE id = %s",
            (new_first_name, user_id)
        )
        conn.commit()
        cur.close()
        print("Data updated successfully.")
    except psycopg2.Error as e:
        print("Error updating data:", e)

def query_data(conn, first_name=None):
    try:
        cur = conn.cursor()
        if first_name:
            cur.execute(f"SELECT * FROM PhoneBook WHERE first_name = %s", (first_name,))
        else:
            cur.execute("SELECT * FROM PhoneBook")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
    except psycopg2.Error as e:
        print("Error querying data:", e)

def delete_data(conn, username):
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM PhoneBook WHERE first_name = %s", (username,))
        conn.commit()
        cur.close()
        print("Data deleted successfully.")
    except psycopg2.Error as e:
        print("Error deleting data:", e)


def main():
    conn = connect_to_db()
    if conn:
        create_phonebook_table(conn)
        upload_from_csv(conn, 'Tsis11/contacts2.csv')
        insert_from_console(conn)
        print("Do you want to change the first name? YES/NO")
        
        a = input()
        if a == "YES":
            update_data_name(conn)
        print("Do you want to change the number? YES/NO")
        b = input()
        if b == "YES":
            update_data_number(conn)
        print("Do you want to delete a name? YES/NO")
        c = input()
        if c == "YES":
            username = input("Enter the first name to delete: ")
            delete_data(conn, username)
        p=True
        while p:
            print("Do you want know number of some person?")
            a = input()
            if a =="YES":
                print("Who?")
                f= input()
                query_data(conn, f)
                return
            p = False
        conn.close()

if __name__ == "__main__":
    main()
