import pytest


from src.masks import get_mask_card_number


def test_get_mask_card_number(card_number):
    assert get_mask_card_number(card_number) == "7000 79** **** 6361"

def test_get_mask_card_number_type():
    with pytest.raises(TypeError):
        get_mask_card_number("7000792289606361")

def test_get_mask_card_number_len(card_number):
    with pytest.raises(ValueError):
        get_mask_card_number(70007922896)
        get_mask_card_number(700079228960636156879546)

