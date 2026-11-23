"""src/nlp/config_d3_hennelly.py - Module Configuration.

(MODIFY YOUR VERSION OF THIS FILE)

Author: Kevin Hennelly
Date: 2026-11

Stores configuration values for the web document EVTL pipeline.
Source: arXiv abstract page for "Agents of Chaos" (2602.20021)

Purpose

  Store configuration values.

Analytical Questions

- What web page URL should be used as the data source?
- Where should raw and processed data be stored?

Edit your Python file to change:
- PAGE_URL (source of the HTML web page document),
- customize your output file name.
"""

from pathlib import Path

# ============================================================
# API CONFIGURATION
# ============================================================

# ATC article
PAGE_URL: str = "https://arxiv.org/abs/2205.09539"

# Let them know who we are (and that we're doing educational web mining).
HTTP_REQUEST_HEADERS: dict = {
    "User-Agent": "Mozilla/5.0 (educational-use; web-mining-course)"
}

# ============================================================
# PATH CONFIGURATION
# ============================================================

ROOT_PATH: Path = Path.cwd()
DATA_PATH: Path = ROOT_PATH / "data"
RAW_PATH: Path = DATA_PATH / "raw"
PROCESSED_PATH: Path = DATA_PATH / "processed"

# Output files from ATC article.
RAW_HTML_PATH: Path = RAW_PATH / "d3_hennelly_raw.html"
PROCESSED_CSV_PATH: Path = PROCESSED_PATH / "d3_hennelly_processed.csv"
