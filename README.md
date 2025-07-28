# MediMatch – A Community Health Resource & Appointment Platform

MediMatch is a database-driven platform designed to improve access to basic healthcare in underserved communities such as students, refugees, and uninsured individuals. While nonprofit clinics and community organizations offer vital health services, their impact is often limited by poor coordination, inefficient scheduling, and lack of visibility.

MediMatch bridges this gap by:

Connecting individuals to free or low-cost medical services

Streamlining clinic and event organization

Supporting appointment management, volunteer coordination, and feedback collection

This project includes a full-stack implementation with:

A Flask web interface for patients and organizers

A CLI tool for quick data interaction and testing

A normalized relational database schema with synthetic data generated for testing realistic scenarios

MediMatch serves as a digital infrastructure for improving health equity and operational efficiency in community healthcare outreach.
# create_db.py
Initializes the MediMatch SQLite3 database.

Defines tables: Patient, Clinic, Service, Appointment, MedicalEvent, Doctor, Volunteer, Feedback

Enforces schema structure and relationships based on the ER diagram

Run this script first to create the database file and schema.

# generate_data.py
Populates the database with synthetic data using the Faker library.

Generates realistic test data: names, contact info, dates, etc.

Inserts bulk data into tables (e.g., 1500+ patients, 3000+ appointments)

Helps simulate real-world usage for development and testing.

# cli.py
Implements a Command-Line Interface to interact with the database.

Built using Python’s argparse module

Supports operations like:

Registering patients or volunteers

Viewing upcoming events

Booking or canceling appointments

Submitting and viewing feedback

Useful for testing and debugging without the web UI.

# app.py
Flask-based Web Application for MediMatch.

Provides user-friendly forms and pages to:

Register users and volunteers

Search clinics and medical events

Book appointments

Submit and view feedback

Uses HTML templates (assumed in a templates/ directory)

Can be run locally for demo or development purposes.
