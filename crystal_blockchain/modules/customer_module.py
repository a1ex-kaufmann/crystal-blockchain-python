from .base_module import Module
from ..utils import check_type


class Customer(Module):
    _CREATE_CUSTOMER = '/monitor/one'
    _GET_CUSTOMER_DETAILS = '/monitor/one/{token}'
    _EDIT_CUSTOMER = '/monitor/one/{token}'
    _GET_CUSTOMERS = '/monitor/list'
    _GET_CUSTOMER_ADDRESSES = '/monitor/one/{token}/addresses'

    _WITH_TOTALS = (0, 1)
    _ORDERS = ('last_added', 'n_txs', 'amount', 'fiat', 'risky_volume', 'risky_volume_fiat')
    _DIRECTIONS = ('asc', 'desc')

    def create_customer(self, name: str, note=None) -> dict:
        """
        Method for creating a new customer. In the response you will receive unique token corresponding to the customer

        :param name: Customer identifier. Please avoid using sensitive data.
        :param note: Comments for the customer
        :return:
        {'data': {'token': 'IaePi4f7T4cUCKik'},
         'meta': {'calls_left': 19976,
                  'calls_used': 24,
                  'error_code': 0,
                  'error_message': '',
                  'riskscore_profile': {'id': 111, 'name': 'test'},
                  'server_time': 1585305641}}
        """
        check_type(name, str)

        params = {
            'name': name,
        }
        if note:
            check_type(note, str)
            params['note'] = note

        response = self._crystal.session().post(
            url=self._to_endpoint(self._CREATE_CUSTOMER),
            params=params
        )

        self._raise_for_error(response)

        return response.json()

    def get_customer_details(self, token: str) -> dict:
        """
        Viewing customer details

        :param token: Token corresponding to the customer
        :return:
        {'data': {'amount_deposit': {'0': 0},
                  'amount_withdrawal': {'0': 0},
                  'archived': False,
                  'created_at': 1585307008,
                  'fiat_deposit': 0,
                  'fiat_withdrawal': 0,
                  'last_added': None,
                  'n_addresses': 0,
                  'n_archived': 0,
                  'n_flagged': 0,
                  'n_txs': 0,
                  'name': 'C#11224',
                  'note': '213',
                  'risky_volume': {'0': 0},
                  'risky_volume_fiat': 0,
                  'token': 'lhN7gPURdSQ5t3Aa',
                  'updated_at': 1585307008,
                  'updating': False},
         'meta': {'calls_left': 19945,
                  'calls_used': 55,
                  'error_code': 0,
                  'error_message': '',
                  'fiat_code': 'usd',
                  'riskscore_profile': {'id': 111, 'name': 'test'},
                  'server_time': 1585307211}}
        """
        check_type(token, str)

        response = self._crystal.session().get(
            url=self._to_endpoint(self._GET_CUSTOMER_DETAILS.format(token=token)),
        )

        self._raise_for_error(response)

        return response.json()

    def edit_customer(self, token: str, archived=None, name=None, note=None) -> dict:
        """
        Edit customer name or notes

        :param token: Token corresponding to the customer
        :param archived: Archive or unarchive transfer (True or False)
        :param name: Customer identified. Please avoid using sensitive data.
        :param note: Comments for the customer
        :return:
        {'data': {'amount_deposit': {'0': 0.0},
                  'amount_withdrawal': {'0': 0.0},
                  'archived': True,
                  'created_at': 1585307008,
                  'fiat_deposit': 0,
                  'fiat_withdrawal': 0,
                  'last_added': None,
                  'n_addresses': 0,
                  'n_archived': 0,
                  'n_flagged': 0,
                  'n_txs': 0,
                  'name': 'newName123',
                  'note': 'newNote111',
                  'risky_volume': {'0': 0.0},
                  'risky_volume_fiat': 0,
                  'token': 'lhN7gPURdSQ5t3Aa',
                  'updated_at': 1585308233,
                  'updating': False},
         'meta': {'calls_left': 19905,
                  'calls_used': 95,
                  'error_code': 0,
                  'error_message': '',
                  'fiat_code': 'usd',
                  'riskscore_profile': {'id': 111, 'name': 'test'},
                  'server_time': 1585308258}}
        """
        check_type(token, str)

        params = {}
        if archived:
            check_type(archived, bool)
            params['archived'] = None  # TODO разобраться, почему api не принимает параметр
        if name:
            check_type(name, str)
            params['name'] = name
        if note:
            check_type(note, str)
            params['note'] = note

        response = self._crystal.session().post(
            url=self._to_endpoint(self._EDIT_CUSTOMER.format(token=token)),
            params=params
        )

        self._raise_for_error(response)

        return response.json()

    def get_customers(
            self,
            with_total=None,
            offset=None,
            limit=None,
            order=None,
            direction=None,
            filter_dict=None
    ) -> dict:
        """
        Viewing customer details for all customers matching the specified parameters

        :param with_total: Default=0 [1, 0]
        :param offset: Default=0
        :param limit: The value ranges between 1 and 20000
        :param order: Default='last_added' ('last_added','n_txs','amount','fiat','risky_volume','risky_volume_fiat')
        :param direction: ('asc', 'desc' )
        :param filter_dict:
            {
                archived: boolean, example=false
                amount_deposit_from: number, example=431460000
                amount_deposit_to: number, example=431460000
                fiat_deposit_from: number, example=4314600
                fiat_deposit_to: number, example=4314600
                amount_withdrawal_from:	number, example=431460000
                amount_withdrawal_to: number, example=431460000
                fiat_withdrawal_from: number, example=4314600
                Minimum amount withdrawn by customer, in selected fiat
                fiat_withdrawal_to: number, example=4314600
                n_txs_from: integer, example=5
                n_txs_to: integer, example=10
                risky_volume_from: number, example=100000000
                risky_volume_to: number, example=200000000
                risky_volume_fiat_from: number, example=10000
                risky_volume_fiat_to: number, example=20000
                last_added_from: number, example=1561007720
                last_added_to: number, example=1561007720
                term: string, example=test customer
            }
        :return:
        {'data': [{'archived': True,
                   'created_at': 1585307008,
                   'fiat_deposit': 0,
                   'fiat_withdrawal': 0,
                   'last_added': None,
                   'n_addresses': 0,
                   'n_archived': 0,
                   'n_flagged': 0,
                   'n_txs': 0,
                   'name': 'newName123',
                   'note': 'newNote111',
                   'risky_volume_fiat': 0,
                   'token': 'lhN7gPURdSQ5t3Aa',
                   'updated_at': 1585308233}, ...],
         'meta': {'calls_left': 19904,
                  'calls_used': 96,
                  'error_code': 0,
                  'error_message': '',
                  'fiat_code': 'usd',
                  'riskscore_profile': {'id': 111, 'name': 'test'},
                  'server_time': 1585309373}}
        """
        params = {}

        if with_total:
            if with_total not in self._WITH_TOTALS:
                raise ValueError('Check "with_total" value')
            params['with_total'] = with_total
        if offset:
            params['offset'] = offset
        if limit:
            params['limit'] = limit
        if order:
            if order not in self._ORDERS:
                raise ValueError('Check "order" value')
            params['order'] = order
        if direction:
            if direction not in self._DIRECTIONS:
                raise ValueError('Check "direction" value')
            params['direction'] = direction
        if filter_dict:
            check_type(filter_dict, dict)
            params['filter'] = filter_dict

        response = self._crystal.session().post(
            url=self._to_endpoint(self._GET_CUSTOMERS),
            params=params
        )

        self._raise_for_error(response)

        return response.json()

    def get_customer_addresses(self, token: str) -> dict:
        """
        Viewing addresses associated with the customer

        :param token: Token corresponding to the customer
        :return:
        {'data': [...],
         'meta': {'calls_left': 19901,
                  'calls_used': 99,
                  'error_code': 0,
                  'error_message': '',
                  'riskscore_profile': {'id': 111, 'name': 'test'},
                  'server_time': 1585313641}}
        """
        check_type(token, str)

        response = self._crystal.session().get(
            url=self._to_endpoint(self._GET_CUSTOMER_ADDRESSES.format(token=token)),
        )

        self._raise_for_error(response)

        return response.json()
