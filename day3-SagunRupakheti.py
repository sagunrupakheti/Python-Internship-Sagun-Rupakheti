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
    # DOCTOR_SPECIALIZATION
    #cursor.execute(" CREATE TABLE IF NOT EXISTS doctor_specialization(id INT PRIMARY KEY,specialization_type VARCHAR(100))")
    # cursor.execute("INSERT INTO doctor_specialization(id,specialization_type) VALUES(2,'Surgeon')")
    # cursor.execute("INSERT INTO doctor_specialization(id,specialization_type) VALUES(3,'Psychiatrist')")
    # cursor.execute("INSERT INTO doctor_specialization(id,specialization_type)VALUES(1,'Anaesthesiologist')")

    #PATIENT
    #cursor.execute(" CREATE TABLE IF NOT EXISTS patient(id INT PRIMARY KEY,name VARCHAR(100), date_of_birth DATE, gender CHAR(1))")
    patient_dict = ((1, 'Jane Henderson', '1989-09-19', 'F'), (2, 'Alice Sprigg', '1991-11-12', 'F'),
                    (3, 'Dave Carr', '1995-03-28', 'M'), (4, 'Morris Beckman', '2001-07-07', 'M'))
    patient_query = ('INSERT INTO patient(id,name,date_of_birth,gender)VALUES(%s,%s,%s,%s)')
    # cursor.executemany(patient_query,patient_dict)

    #DOCTOR
    #cursor.execute(" CREATE TABLE IF NOT EXISTS doctor(id INT PRIMARY KEY,name VARCHAR(100),specialization int,phone_no int,CONSTRAINT doctor_specialization_id FOREIGN KEY(specialization) REFERENCES doctor_specialization(id))")
    doctor_dict = ((1,'Lionel Smart',1,281123),(2,'Michelle Sanders',2,18999),(3,'Pretti Patel',3,79801),(4,'Sadiq Khan',1,7983),(5 ,'Chaz Smith',2,2039))
    doctor_query = "INSERT INTO doctor(id,name,specialization,phone_no) VALUES (%s, %s, %s, %s)"
    #cursor.executemany(doctor_query,doctor_dict)

    #APPOINTMENT
    #cursor.execute(" CREATE TABLE IF NOT EXISTS appointment(id INT PRIMARY KEY,doctor_id int, patient_id int, diagnosis VARCHAR(100),"
                   #"CONSTRAINT fk_doctor_id FOREIGN KEY(doctor_id) REFERENCES doctor(id), CONSTRAINT fk_patient_id FOREIGN KEY(patient_id) REFERENCES patient(id))")
    appointment_dict = ((1, 1, 2, 1000, ''), (2, 1, 4, 1000, 'Headache'),
                        (3, 4, 3, 2000, ''), (4, 2, 1, 1500, 'Back Pain'))
    appointment_query = ('INSERT INTO appointment(id,doctor_id,patient_id,fee,diagnosis)VALUES(%s,%s,%s,%s,%s)')
    # cursor.executemany(appointment_query,appointment_dict)

    #GET the count of patients born after 1990.

    #cursor.execute('SELECT COUNT(*) FROM patient WHERE EXTRACT (YEAR FROM date_of_birth) >1990')
    print(cursor.fetchall())

    #GET the appointments made with “Surgeon” specialized doctors.
    #cursor.execute("SELECT a.id AS appointment_num FROM appointment a JOIN doctor d ON a.doctor_id = d.id JOIN doctor_specialization c ON c.id = d.specialization WHERE c.specialization_type = 'Surgeon'")
    print(cursor.fetchall())

    #UPDATE fees of appointments and reduce them by 25%
    #cursor.execute("UPDATE appointment SET fee = appointment.fee - (appointment.fee * 0.25);")

    #UPDATE phone_number of Chaz Smith to 1231292310.
    #cursor.execute("UPDATE doctor SET phone_no = 123129 WHERE name = 'Chaz Smith'")


    #DELETE all doctors who are specialized as “Psychiatrist”.
    #cursor.execute("DELETE FROM doctor USING doctor_specialization WHERE doctor.specialization = doctor_specialization.id AND "
                   #"doctor_specialization.specialization_type='Psychiatrist';")
    connection.commit()
    cursor.close()
    connection.close()
except Exception as e:
    print(e)

