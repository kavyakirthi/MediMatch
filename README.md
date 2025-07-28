create_db.py
Initializes the MediMatch SQLite3 database.

Defines tables: Patient, Clinic, Service, Appointment, MedicalEvent, Doctor, Volunteer, Feedback

Enforces schema structure and relationships based on the ER diagram

Run this script first to create the database file and schema.

generate_data.py
Populates the database with synthetic data using the Faker library.

Generates realistic test data: names, contact info, dates, etc.

Inserts bulk data into tables (e.g., 1500+ patients, 3000+ appointments)

Helps simulate real-world usage for development and testing.

cli.py
Implements a Command-Line Interface to interact with the database.

Built using Python’s argparse module

Supports operations like:

Registering patients or volunteers

Viewing upcoming events

Booking or canceling appointments

Submitting and viewing feedback

Useful for testing and debugging without the web UI.

app.py
Flask-based Web Application for MediMatch.

Provides user-friendly forms and pages to:

Register users and volunteers

Search clinics and medical events

Book appointments

Submit and view feedback

Uses HTML templates (assumed in a templates/ directory)

Can be run locally for demo or development purposes.
