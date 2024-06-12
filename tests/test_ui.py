import logging
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        yield browser
        browser.close()

def test_example(browser):
    page = browser.new_page()
    page.goto("https://progress.com")
    assert 'Progress' in page.title()