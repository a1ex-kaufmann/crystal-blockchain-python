from abc import ABC
from urllib import parse

from ..exceptions import CrystalException


class Module(ABC):
    def __init__(self, crystal):
        self._crystal = crystal

    @classmethod
    def _attach(cls, target, module_name=None):
        if not module_name:
            module_name = cls.__name__.lower()
        if hasattr(target, module_name):
            raise AttributeError(
                f"""
                Cannot set {target} module named '{module_name}'. 
                The crystal object already has an attribute with that name
                """
            )
        setattr(target, module_name, cls(target))

    @staticmethod
    def _raise_for_error(response):
        if not response.ok:
            msg = None
            try:
                msg = response.json()['meta']
            except:
                msg = response.text

            raise CrystalException(f'code: {response.status_code}, msg={msg}')

    def _to_endpoint(self, route: str):
        return parse.urljoin(self._crystal.ENDPOINT, route)

    @staticmethod
    def _filter_to_str(filter_dict: dict) -> str:
        """
        wtf, this api requires a string instead of a json object (python dict) in filters
        """
        res_str = str(filter_dict).replace('{', '').replace('}', '').replace(' ', '').replace("'", "")
        return res_str
