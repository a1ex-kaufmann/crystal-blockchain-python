from .base_module import Module
from ..utils import check_type


class Entity(Module):
    _GET_ENTITY_LIST = '/entity/list'
    _GET_ENTITY_SUMMARY = '/entity/one/{slug}'

    def get_entity_list(self) -> dict:
        """
        This method provides the list of entities

        :return:
        {'data': [{'id': '390910438',
                   'name': 'Hotbit',
                   'slug': 'Hotbit',
                   'subtype': None,
                   'type': 'exchange'},
                  {'id': '87306325',
                   'name': 'IndependentReserve',
                   'slug': 'IndependentReserve',
                   'subtype': None,
                   'type': 'exchange'},
                   ...
                  {'id': '233083216',
                   'name': 'LocalCoin',
                   'slug': 'LocalCoin',
                   'subtype': None,
                   'type': 'atm'}],
         'meta': {'calls_left': 19727,
                  'calls_used': 273,
                  'error_code': 0,
                  'error_message': '',
                  'riskscore_profile': {'id': 111, 'name': 'test'},
                  'server_time': 1587669630}}

        """
        response = self._crystal.session().get(
            url=self._to_endpoint(self._GET_ENTITY_LIST)
        )

        self._raise_for_error(response)

        return response.json()

    def get_entity_summary(self, slug: str):
        """
        This method provides details about entity

        :param slug: Entity identifier (URL valid entity name or entity ID)
        :return:
        {'data': {'balance': 1985662589.0,
                  'country': 'ca',
                  'fiat': True,
                  'first_activity': 1488998438,
                  'has_token': [0],
                  'id': '233083216',
                  'last_activity': 1587669356,
                  'n_mentions': 1,
                  'name': 'LocalCoin',
                  'riskscore': {'signals': {'atm': 1.0,
                                            'dark_market': 0.0,
                                            'dark_service': 0.0,
                                            'exchange': 0.0,
                                            'gambling': 0.0,
                                            'illegal_service': 0.0,
                                            'marketplace': 0.0,
                                            'miner': 0.0,
                                            'mixer': 0.0,
                                            'payment': 0.0,
                                            'ransom': 0.0,
                                            'risky_exchange': 0.0,
                                            'scam': 0.0,
                                            'stolen_coins': 0.0,
                                            'trusted_exchange': 0.0,
                                            'wallet': 0.0},
                                'updated': [{'time': 1587162768, 'type': 'global'},
                                            {'time': 1587669356, 'type': 'fast'}],
                                'value': 0.5},
                  'size': 8,
                  'slug': 'LocalCoin',
                  'status': 'active',
                  'subtype': None,
                  'type': 'atm',
                  'website': 'https://localcoin.ca/'},
         'meta': {'calls_left': 19725,
                  'calls_used': 275,
                  'error_code': 0,
                  'error_message': '',
                  'riskscore_profile': {'id': 111, 'name': 'test'},
                  'server_time': 1587669951}}
        """
        check_type(slug, str)

        response = self._crystal.session().get(
            url=self._to_endpoint(self._GET_ENTITY_SUMMARY.format(slug=slug))
        )

        self._raise_for_error(response)

        return response.json()
