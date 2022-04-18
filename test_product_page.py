import pytest
from Pages.productpage import *


class TestBook:

    def test_guest_can_add_product_to_basket(self, browser):
        ProductPage.take_book(browser)
