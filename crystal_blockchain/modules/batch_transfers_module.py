from .base_module import Module
from ..utils import check_type


class BatchTransfers(Module):
    _GET_TXS = '/monitor/batch/txs'
    _GET_TXS_BOUNDS = '/monitor/batch/tx-bounds'
    _EDIT_TXS = '/monitor/batch/txs/execute'

    _WITH_TOTALS = (1, 0)
    _ORDERS = ('amount', 'fiat', 'time', 'created_at', 'updated_at', 'riskscore')
    _DIRECTIONS = ('asc', 'desc')
    _ACTIONS = ('schedule', 'archive', 'unarchive', 'flag', 'unflag')

    def get_txs(
            self,
            with_total=None,
            offset=None,
            limit=None,
            order=None,
            direction=None,
            filter_dict=None,
    ) -> dict:
        """
        Get list of transfers with applied filters

        :param with_total: number, default=0, (1, 0)
        :param offset: number, default=0
        :param limit: number, default=10, example=10
        :param order: string, default='updated_at, ('amount', 'fiat', 'time', 'created_at', 'updated_at', 'riskscore')
        :param direction: string, ('asc', 'desc')
        :param filter_dict: filter dict (see API docs)
        :return:
        {
          "data": [
            {
              "address": "1AxCHtZA1mxNLg2o6KPRCyDRueifLPXED",
              "amount": 420060000,
              "archived": true,
              "created_at": 1571653914,
              "customer": {
                "name": "C#1456",
                "token": "bn3KXb66HkncoJPv"
              },
              "direction": "deposit",
              "fiat_code_effective": "eur",
              "flagged": false,
              "flag_reason": [...],
              "reason": null,
              "id": 1010,
              "riskscore": 0,
              "riskscore_profile": {
                "id": 10,
                "name": "KYC profile",
                "history_id": 322
              },
              "risky_volume": 12345.667,
              "risky_volume_fiat": 112,
              "signals": { ... },
              "status": "ready",
              "time": 1571652931,
              "token_id": 0,
              "tx": "f00ddb52671bcdddfb1bb654c091320f624e443edba392ea27e178817048b776",
              "updated_at": 1571653914,
              "fiat": 3449426
            }
          ],
          "meta": {...}
        }
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
            params['filter'] = self._filter_to_str(filter_dict)

        response = self._crystal.session().post(
            url=self._to_endpoint(self._GET_TXS),
            params=params
        )

        self._raise_for_error(response)

        return response.json()

    def get_txs_bounds(self) -> dict:
        """
        Get minimum and maximum filtering parameters for all customers

        :return:
        {
          "data": {
            "created_min": 1361107720,
            "created_max": 1561107720,
            "updated_min": 1361108012,
            "updated_max": 15361108012,
            "time_min": 1361107421,
            "time_max": 1561107421,
            "amount": 20790475596,
            "fiat": 202748821
          },
          "meta": {
            "calls_left": 0,
            "calls_used": 0,
            "error_code": 0,
            "error_message": "string",
            "fiat_code": "usd",
            "riskscore_profile": {
              "id": 150,
              "name": "default"
            },
            "server_time": 0,
            "validation_errors": {}
          }
        }
        """
        response = self._crystal.session().get(
            url=self._to_endpoint(self._GET_TXS_BOUNDS.format()),
        )

        self._raise_for_error(response)

        return response.json()

    def edit_txs(self, action=None, filter_dict=None):
        """

        :param action: Here you can specify the action ('schedule', 'archive', 'unarchive', 'flag', 'unflag')
        :param filter_dict: filter dict (see API docs)
        :return:
        {
          "data": {
            "scheduled": 1,
            "archived": 1,
            "unarchived": 1
          },
          "meta": {
            "calls_left": 0,
            "calls_used": 0,
            "error_code": 0,
            "error_message": "string",
            "fiat_code": "usd",
            "riskscore_profile": {
              "id": 150,
              "name": "default"
            },
            "server_time": 0,
            "validation_errors": {}
          }
        }
        """
        params = {}
        if action:
            if action not in self._ACTIONS:
                raise ValueError('Check "action" value')
            params['action'] = action
        if filter_dict:
            check_type(filter_dict, dict)
            params['filter'] = self._filter_to_str(filter_dict)
        response = self._crystal.session().post(
            url=self._to_endpoint(self._EDIT_TXS.format()),
            params=params
        )

        self._raise_for_error(response)

        return response.json()