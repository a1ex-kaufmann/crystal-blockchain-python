from .base_module import Module
from ..utils import check_type


class Explorer(Module):
    _GET_ADDRESS_SUMMARY = '/explorer/address/{address_hash}'
    _GET_TX_SUMMARY = '/explorer/tx/{tx_hash}'

    _RISK_SCORES = ('none', 'simple', 'extended')

    def get_address_summary(self, address: str) -> dict:
        """
        This method provides address details

        :param address: wallet address
        :return:
        {'data': {'address': '17A16QmavnUfCW11DAApiJxp7ARnxN5pGX',
                  'balance': 349120500103,
                  'first_activity': 1481541858,
                  'has_token': [0],
                  'last_activity': 1587639149,
                  'n_mentions': 53,
                  'n_tx': 361045,
                  'owner': {'first_activity': 1310318258,
                            'grade': 0,
                            'id': '26456753',
                            'last_activity': 1587638446,
                            'name': 'Poloniex',
                            'size': 990670,
                            'slug': 'Poloniex',
                            'status': 'active',
                            'subtype': None,
                            'type': 'exchange'},
                  'received': 333167851580073,
                  'riskscore': {'signals': {'atm': 0.0,
                                            'dark_market': 0.0,
                                            'dark_service': 0.0,
                                            'exchange': 1.0,
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
                                            {'time': 1587638446, 'type': 'fast'}],
                                'value': 0.5},
                  'shared_balance': 0,
                  'shared_recv': 0,
                  'status': 'active',
                  'topTxs': [{'block_time': 1517079726,
                              'hash': '8526fa5d044e9ec6711a6ea413aa3110ac7663f7e6eb64ad84be28a08b579bb6',
                              'situational': {'delta': 1165772241179}},
                             {'block_time': 1491174439,
                              'hash': '08734a2d652f57ad43164af485b8e2a3deee0b2adaf7f96e3f3f9941fcfb13fc',
                              'situational': {'delta': 850181899209}},
                             {'block_time': 1501551425,
                              'hash': 'b0b8d071cc27541e2795b3e379daccc43a7cd2c6669369d6ec46b367db24e0dd',
                              'situational': {'delta': 747476976573}},
                             {'block_time': 1521083347,
                              'hash': '76132dbead41764f368cfc938b6c29056bcb3be34fb1621abff130295e42b435',
                              'situational': {'delta': 737581676597}},
                             {'block_time': 1523538334,
                              'hash': '047652349cad2686753b695113509c90e1e6f658262e88a0515679ba2e65b4b3',
                              'situational': {'delta': 735595160558}}]},
         'meta': {'calls_left': 19738,
                  'calls_used': 262,
                  'error_code': 0,
                  'error_message': '',
                  'riskscore_profile': {'id': 111, 'name': 'test'},
                  'server_time': 1587639191}}
        """
        check_type(address, str)

        response = self._crystal.session().get(
            url=self._to_endpoint(self._GET_ADDRESS_SUMMARY.format(address_hash=address))
        )

        self._raise_for_error(response)

        return response.json()

    def get_tx_summary(self, tx_hash: str, untangle=None, risk_score=None) -> dict:
        """
        This endpoint provides transaction details

        :param tx_hash: transaction hash
        :param untangle: enter 1 if you need untangled transaction
        :param risk_score: enter "extended" if you need maximum and average value for inputs and outputs of transaction
            Available values : none, simple, extended
        :return:
        {'data': {'additional': {},
                  'block': {'hash': '0000000000000000000e19280a3918a4e3d8d5f29bd4a0d8d3af6761132eea57',
                            'height': 627310},
                  'block_time': 1587654070,
                  'confirmations': 1,
                  'count_in': 5,
                  'count_out': 2,
                  'fiat_rate': 7555.7,
                  'hash': '2099c246f65668226597c606ce937b510ddfc4c5ebe0aedef6a66f6c9f7d9473',
                  'inputs': [{'address': '367f4YWz1VCFaqBqwbTrzwi2b1h2U3w1AF',
                              'amount': 116548542,
                              'owner': {'id': '356179483',
                                        'name': 'GOPAX',
                                        'slug': 'GOPAX',
                                        'subtype': None,
                                        'type': 'exchange'},
                              'pos': 0,
                              'prev': 'f2daf5aa76754c821ef206a422f77eee241827bfd4dfe5c085886fce8ed1f729',
                              'riskscore': 0.5},
                                ...
                             {'address': '1C5idoNRyGj6eg5pkMGQgsyN8aGLdDssnu',
                              'amount': 452964,
                              'owner': {'id': '356179483',
                                        'name': 'GOPAX',
                                        'slug': 'GOPAX',
                                        'subtype': None,
                                        'type': 'exchange'},
                              'pos': 1,
                              'prev': '9d7010f9e646df0ce4787112003687c08bcbd004c8168c2c4c12a4b8f197de9c',
                              'riskscore': 0.5}],
                  'outputs': [{'address': '367f4YWz1VCFaqBqwbTrzwi2b1h2U3w1AF',
                               'amount': 8199850,
                               'owner': {'id': '356179483',
                                         'name': 'GOPAX',
                                         'slug': 'GOPAX',
                                         'subtype': None,
                                         'type': 'exchange'},
                               'riskscore': 0.5},
                              {'address': '1FUWYzFRxCAi34UUxJ8MMjLcyCQgCWePtx',
                               'amount': 109315048,
                               'owner': {'id': '455688048',
                                         'name': 'Bybit',
                                         'slug': 'Bybit',
                                         'subtype': None,
                                         'type': 'exchange'},
                               'riskscore': 0.5}],
                  'pool_time': 1587654036,
                  'riskscore': {'signals': {'atm': 0.0,
                                            'dark_market': 0.0,
                                            'dark_service': 0.0,
                                            'exchange': 1.0,
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
                                'value': 0.5},
                  'size': 1001,
                  'total_in': 117700698,
                  'total_out': 117514898,
                  'weight': 3228},
         'meta': {'calls_left': 19735,
                  'calls_used': 265,
                  'error_code': 0,
                  'error_message': '',
                  'fiat_code': 'usd',
                  'riskscore_profile': {'id': 111, 'name': 'test'},
                  'server_time': 1587655174}}
        """
        check_type(tx_hash, str)
        params = {}

        if untangle:
            if untangle not in (0, 1):
                raise ValueError('Check "untangle" value')
            params['untangle'] = untangle
        if risk_score:
            if risk_score not in Explorer._RISK_SCORES:
                raise ValueError('Check "riskscore" value')
            params['riskscore'] = risk_score

        response = self._crystal.session().get(
            url=self._to_endpoint(self._GET_TX_SUMMARY.format(tx_hash=tx_hash)),
            params=params
        )

        self._raise_for_error(response)

        return response.json()
