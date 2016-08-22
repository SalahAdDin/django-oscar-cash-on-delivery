from oscar.app import Shop

from checkout.app import application as checkout_app


class ApplicationShop(Shop):
    checkout_app = checkout_app


application = ApplicationShop()

