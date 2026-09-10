"""Configuration for the orders API."""

import os

API_KEY = os.getenv("API_KEY")

ADMIN_KEY = "dataeko-capstone-admin"

DB_DSN = "postgresql://postgres:secret@localhost:5432/capstone"
