from faker import Faker
import sqlite3
import random

fake = Faker()
conn = sqlite3.connect('medimatch.db')
cursor = conn.cursor()

# Create sample clinics (120)
for _ in range(120):
    cursor.execute('INSERT INTO Clinic (Name, Address) VALUES (?, ?)', 
                   (fake.company(), fake.address()))

# Create sample services (90)
services = [(f"{fake.word().capitalize()} Service {i+1}", fake.sentence(nb_words=5)) for i in range(90)]
for s in services:
    cursor.execute('INSERT INTO Service (Name, Description) VALUES (?, ?)', s)

# Create sample patients (1500) with UNIQUE email check in DB
for i in range(1500):
    while True:
        unique_email = f"user{i}_{random.randint(1000, 9999)}@example.com"
        cursor.execute("SELECT 1 FROM Patient WHERE Email = ?", (unique_email,))
        if cursor.fetchone() is None:
            break
    cursor.execute('''
        INSERT INTO Patient (Name, DOB, Phone, Email, City)
        VALUES (?, ?, ?, ?, ?)''',
        (
            fake.name(),
            fake.date_of_birth(minimum_age=18, maximum_age=90).isoformat(),
            fake.phone_number(),
            unique_email,
            fake.city()
        ))

# Create sample doctors (150)
license_nos = set()
for _ in range(150):
    while True:
        license_no = fake.bothify(text='????-#####')
        if license_no not in license_nos:
            license_nos.add(license_no)
            break
    cursor.execute('INSERT INTO Doctor (Name, Speciality, License_No) VALUES (?, ?, ?)',
                   (
                       fake.name(),
                       random.choice(['Dentist', 'Ophthalmologist', 'Cardiologist', 'Therapist', 'General Practitioner']),
                       license_no
                   ))

# Create sample volunteers (150)
for _ in range(150):
    cursor.execute('INSERT INTO Volunteer (Name, Role) VALUES (?, ?)',
                   (
                       fake.name(),
                       random.choice(['Reception', 'Assistance', 'Logistics', 'Scheduling', 'Outreach'])
                   ))

# Get existing counts
cursor.execute("SELECT COUNT(*) FROM Clinic")
clinic_count = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM Patient")
patient_count = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM Service")
service_count = cursor.fetchone()[0]

# Create sample medical events (150)
for _ in range(150):
    clinic_id = random.randint(1, clinic_count)
    cursor.execute('INSERT INTO Medical_Event (Date, Location, Clinic_ID) VALUES (?, ?, ?)',
                   (
                       fake.date_between(start_date='-60d', end_date='+60d').isoformat(),
                       fake.city(),
                       clinic_id
                   ))

cursor.execute("SELECT COUNT(*) FROM Medical_Event")
event_count = cursor.fetchone()[0]

# Create sample appointments (3000)
for _ in range(3000):
    cursor.execute('''
        INSERT INTO Appointment (Date, Status, Patient_ID, Clinic_ID, Service_ID)
        VALUES (?, ?, ?, ?, ?)''',
        (
            fake.date_between(start_date='-30d', end_date='+30d').isoformat(),
            random.choice(['confirmed', 'cancelled']),
            random.randint(1, patient_count),
            random.randint(1, clinic_count),
            random.randint(1, service_count)
        ))

# Create sample feedback (600)
for _ in range(600):
    cursor.execute('''
        INSERT INTO Feedback (Rating, Comments, Patient_ID, Event_ID)
        VALUES (?, ?, ?, ?)''',
        (
            random.randint(1, 5),
            fake.sentence(nb_words=10),
            random.randint(1, patient_count),
            random.randint(1, event_count)
        ))

conn.commit()
conn.close()
print("Large sample data generated successfully.")
