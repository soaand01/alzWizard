"""Playwright screenshot script for ALZ Wizard pages.

Saves screenshots under screenshots/ with names like:
  screenshots/desktop_phase1_tools.png
  screenshots/mobile_phase1_tools.png

Requires: playwright package and browsers installed via `playwright install`.
Run: /home/andlopes/labs/alzWizard/.venv/bin/python tools/playwright_screenshots.py
"""
import os
from playwright.sync_api import sync_playwright

BASE_URL = 'http://localhost:5000'
PAGES = [
    ('phase1_tools', '/phase1/tools'),
    ('phase1_subscriptions', '/phase1/subscriptions'),
    ('phase1_vcs', '/phase1/vcs'),
    ('phase2', '/phase2'),
    ('phase3', '/phase3'),
]

OUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'screenshots')
os.makedirs(OUT_DIR, exist_ok=True)

VIEWPORTS = {
    'desktop': {'width': 1280, 'height': 900},
    'mobile': {'width': 412, 'height': 915},
}

with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context()
    for vp_name, vp in VIEWPORTS.items():
        context = browser.new_context(viewport=vp)
        page = context.new_page()
        for name, path in PAGES:
            url = BASE_URL + path
            print(f'Capturing {vp_name} {url}')
            try:
                page.goto(url, wait_until='networkidle')
                # small delay to allow client-side scripts to run
                page.wait_for_timeout(600)
                out_path = os.path.join(OUT_DIR, f'{vp_name}_{name}.png')
                page.screenshot(path=out_path, full_page=True)
                print('Saved', out_path)
            except Exception as e:
                print('ERROR capturing', url, e)
        context.close()
    browser.close()
