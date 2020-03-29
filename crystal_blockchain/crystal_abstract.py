import requests

from abc import ABC

from .modules import Profile, Customer, Transfers


class Crystal(ABC):
    ENDPOINT = ''

    TOKEN_ID = None

    __MODULES = {
        'profile': Profile,
        'customer': Customer,
        'transfers': Transfers
    }

    profile: Profile
    customer: Customer
    transfers: Transfers

    def __init__(self, api_key):
        self.__api_key = api_key
        self.__session = None
        self.__headers = {
            'X-Auth-Apikey': self.__api_key,
        }

        Crystal.__attach_modules(self, self.__MODULES)

    def session(self):
        if not self.__session:
            self.__session = requests.Session()
            self.__session.headers.update(self.__headers)
        return self.__session

    @staticmethod
    def __attach_modules(parent_module, module_definitions):
        for module_name, module_class in module_definitions.items():
            module_class._attach(parent_module, module_name)
