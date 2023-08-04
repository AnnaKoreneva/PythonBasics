import pytest
import re

from playwright.sync_api import Page, expect

@pytest.mark.ui
@pytest.mark.portal
def test_adcorner_login(page: Page):

    # Arrange
    page.goto('url')

    # Act
    page.locator('xpath=/html/body/app-root/app-welcome/div[1]/app-ui-card/mat-card/div/div[1]/app-ui-button/div/button').click()
    page.locator('id=username').fill('userName')
    page.locator('id=password').fill('Pass')
    page.locator('xpath=/html/body/div/main/section/div/div/div/form/div[3]/button').click()

    # React
    expect(page.get_by_text('Admin Portal')).to_be_visible()

def test_adcorner_create_account(page: Page):
    # Arrange
    page.goto('url/welcome')

    # Act
    page.locator(
        'xpath=/html/body/app-root/app-welcome/div[1]/app-ui-card/mat-card/div/div[1]/app-ui-button/div/button').click()
    page.locator('id=username').fill('username')
    page.locator('id=password').fill('pass')
    page.locator('xpath=/html/body/div/main/section/div/div/div/form/div[3]/button').click()
    page.locator(
        'xpath=/html/body/app-root/app-simple-layout/main/div/section/app-admin-portal/div[1]/app-ui-button/div/button').click()
    page.locator('xpath=//*[@id="mat-dialog-0"]/app-account-dialog/div/div[1]/div[2]/ul/li[2]/span').click()

