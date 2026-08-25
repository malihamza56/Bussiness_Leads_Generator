"""
Business Lead Generator
Configuration Module

Centralizes application configuration such as:
- Directory URL
- Pagination limit
- Request timeout
- Output paths
- Environment variables
"""

import os
from pathlib import Path

from dotenv import load_dotenv


# ============================================================
#! BASE PROJECT DIRECTORY
# ============================================================

BASE_DIR = Path(
    __file__
).resolve().parents[2]


# ============================================================
#! ENVIRONMENT VARIABLES
# ============================================================

ENV_PATH = BASE_DIR / ".env"

load_dotenv(
    ENV_PATH
)


# ============================================================
#! DIRECTORY WEBSITE
# ============================================================

DIRECTORY_BASE_URL = (
    "https://www.lookup.pk"
)


# ============================================================
#! SCRAPING SETTINGS
# ============================================================

MAX_PAGES = 25

REQUEST_TIMEOUT = 30_000

HEADLESS = False


# ============================================================
#! DATA DIRECTORIES
# ============================================================

DATA_DIR = (
    BASE_DIR / "data"
)

RAW_DATA_DIR = (
    DATA_DIR / "raw"
)

PROCESSED_DATA_DIR = (
    DATA_DIR / "processed"
)


# ============================================================
#! OUTPUT FILES
# ============================================================

RAW_JSON_PATH = (
    RAW_DATA_DIR /
    "businesses_raw.json"
)

PROCESSED_JSON_PATH = (
    PROCESSED_DATA_DIR /
    "businesses_processed.json"
)

CSV_PATH = (
    PROCESSED_DATA_DIR /
    "business_leads.csv"
)

EXCEL_PATH = (
    PROCESSED_DATA_DIR /
    "business_leads.xlsx"
)


# ============================================================
#! LOGGING
# ============================================================

LOG_DIR = (
    BASE_DIR / "logs"
)

LOG_FILE = (
    LOG_DIR / "scraper.logs"
)


# ============================================================
#! OPTIONAL EMAIL CONFIGURATION
# ============================================================

SMTP_HOST = os.getenv(
    "SMTP_HOST"
)

SMTP_PORT = int(
    os.getenv(
        "SMTP_PORT",
        "587"
    )
)

EMAIL_USER = os.getenv(
    "EMAIL_USER"
)

EMAIL_PASSWORD = os.getenv(
    "EMAIL_PASSWORD"
)


# ============================================================
#! CREATE DIRECTORIES
# ============================================================

RAW_DATA_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

PROCESSED_DATA_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

LOG_DIR.mkdir(
    parents=True,
    exist_ok=True,
)