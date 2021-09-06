import psycopg2
try:
    connection = psycopg2.connect(
        host="localhost",
        database="pythonDB",
        user="postgres",
        password="sagun",
        port=5433
    )
    cursor = connection.cursor()

    #Create a table named 'users'-- columns -> id, name, dob, profession
    cursor.execute(" CREATE TABLE IF NOT EXISTS users(id INT PRIMARY KEY,name VARCHAR(100),dob DATE, profession  VARCHAR(100))")

    #Create table names `address`-- Columns -> id, user_id (FK -> users), permanent_address, temporary_address
    cursor.execute(" CREATE TABLE IF NOT EXISTS address(id INT PRIMARY KEY,user_id int, permanentaddress VARCHAR(100), temporaryaddress VARCHAR(100), CONSTRAINT fk_user_id FOREIGN KEY(user_id) REFERENCES users(id))")

    #Insert dummy data in the tables using psycopg connection
    cursor.execute("INSERT INTO users(id,name,dob,profession) VALUES(1,'Sagun Rupakheti','2000-02-04','Intern')")
    cursor.execute("INSERT INTO users(id,name,dob,profession) VALUES(2,'Manjila Khanal','1999-07-20','HR')")
    cursor.execute("INSERT INTO users(id,name,dob,profession) VALUES(3,'Biswani Khanal','2000-04-29','Student')")

    address_dict = ((1, 1, 'Kathmandu', 'Dhading'), (2, 2, 'Jhapa', 'Kathmandu'), (3, 3, 'Sarlahi', 'Bhaktapur'))
    address_query= "INSERT INTO address(id,user_id,permanentaddress,temporaryaddress) VALUES(%s,%s,%s,%s)"
    cursor.executemany(address_query, address_dict)


    # Fetch data from the joined users and address table -- given user_id
    cursor.execute("SELECT * FROM users WHERE id=2")
    print(cursor.fetchall())

    #given profession and permanent_address
    cursor.execute("SELECT u.name ,u.profession, a.permanentaddress FROM address a JOIN users u ON u.id=a.user_id WHERE profession!='Student' OR permanentaddress='Kathmandu'")
    get_info = cursor.fetchall()
    #print all columns
    for i in get_info:
        print('\n')
        print('Name:'+ i[0]);
        print('Profession:' + i[1]);
        print('Permanent Address:' + i[2]);

    #Update table users and add column gender
    cursor.execute("ALTER TABLE users ADD COLUMN gender CHAR(1)")

    #Delete records from user whose age is less than 20 yrs
    cursor.execute("DELETE FROM users WHERE date_part('year',age(dob))<20")

    connection.commit()
    cursor.close()
    connection.close()
except Exception as e:
    print(e)

