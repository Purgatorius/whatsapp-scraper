# EvidenceScraper_WhatsApp

Terminal-only WhatsApp Web scraper written in Python and Playwright.

The goal is to professionally and cleanly extract message evidence with full logging, headless operation, and forensic robustness.

## Features (planned)
- [x] CLI only, Vim friendly
- [ ] Clean OOP codebase
- [ ] Logging and reporting
- [ ] Evidence export (JSON, CSV, PDF)


## Project Structure

```
EvidenceScraper_WhatsApp/
├── evidence_scraper/ # app main code
│ ├── init.py
│ ├── cli.py # CLI logic
│ ├── scraper.py # app main class
│ ├── playwright_runner.py # wrapper for Playwright
│ ├── exporter.py # export data
│ └── utils.py # additional functions
├── tests/ # unit tests
│ ├── init.py
│ ├── test_scraper.py
│ ├── test_exporter.py
│ └── ...
├── data/ # temp data (added in .gitignore)
├── logs/ # logs (added in .gitignore)
├── README.md
├── .gitignore
├── requirements.txt # Python dependencies
└── main.py # app entry point
```
