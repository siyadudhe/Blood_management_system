# Vital Ledger Blood Bank System

A Flask-based blood bank management system built from the provided Stitch/Figma UI export while preserving the existing design.

## Features
- Authentication, roles, and dashboards
- Donor management
- Inventory tracking and low-stock visibility
- Blood requests and status updates
- Hospital management
- Reports export to PDF and Excel
- Profile updates and password changes

## Setup
1. Create a virtual environment.
2. Install requirements: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and update settings.
4. Run: `python run.py`

## Notes
- SQLite is used by default.
- The app seeds sample data on first run.
