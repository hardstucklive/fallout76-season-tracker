name: Update season info

on:
  schedule:
    - cron: '0 8 * * *'  # Every day at 8am UTC
  workflow_dispatch:

jobs:
  update:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: pip install beautifulsoup4 requests

      - name: Run scraper
        run: python scrape.py

      - name: Commit & Push
        run: |
          git config user.name "github-actions"
          git config user.email "github-actions@github.com"
          git add season.txt
          git commit -m "Auto-update season end date" || echo "No changes"
          git push
