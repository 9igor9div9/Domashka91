import pytest


@pytest.fixture
def card_number():
    return 7000792289606361

@pytest.fixture
def account():
    return 73654108430135874305

@pytest.fixture
def requisites_number_account():
    return "Счет 73654108430135874305"

@pytest.fixture
def required_number_card():
    return "Visa Platinum 7000792289606361"

@pytest.fixture
def date():
    return "2024-03-11T02:26:18.671407"
