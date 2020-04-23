from .base_module import Module
from ..utils import check_type


class Profile(Module):
    _GET_PROFILES = '/settings/riskscore/list'
    _GET_PROFILE_DETAILS = '/settings/riskscore/one/{profile_id}'
    _EDIT_PROFILE = '/settings/riskscore/one/{profile_id}'
    _DELETE_PROFILE = '/settings/riskscore/one/{profile_id}'
    _ENABLE_PROFILE = '/settings/riskscore/one/{profile_id}/enable'
    _EDIT_ENTITY_TYPE = '/settings/riskscore/one/{profile_id}/{signal}'
    _RESET_SETTINGS = '/settings/riskscore/one/{profile_id}/reset'

    _SIGNAL_LIST = (
        'atm', 'dark_market', 'dark_service', 'exchange', 'trusted_exchange', 'gambling', 'ransom',
        'marketplace', 'miner', 'mixer', 'payment', 'scam', 'wallet', 'stolen_coins', 'illegal_service'
    )
    _RECV_LIST = ('none', 'low', 'mid', 'high')
    _SENT_LIST = ('none', 'low', 'mid', 'high')

    def get_profiles(self) -> dict:
        """
        Method provides the list of Risk Score profiles

        :return:
        {'data': [{'author': 'Сергей Жданов',
                   'created_at': 1585262863,
                   'id': 110,
                   'is_enabled': True,
                   'name': 'testName',
                   'updated_at': 1585294925},
                  {'author': 'Crystal',
                   'created_at': None,
                   'id': 0,
                   'is_enabled': False,
                   'name': 'Default',
                   'updated_at': 1580467806}],
         'meta': {'calls_left': 19993,
                  'calls_used': 7,
                  'error_code': 0,
                  'error_message': '',
                  'riskscore_profile': {'id': 110, 'name': 'testName'},
                  'server_time': 1585294967}}
        """
        response = self._crystal.session().get(
            url=self._to_endpoint(self._GET_PROFILES)
        )

        self._raise_for_error(response)

        return response.json()

    def get_profile_details(self, profile_id: int) -> dict:
        """
        Method provides the Risk Score profile details

        :param profile_id: Profile ID
        :return:
        {'data': {'author': 'Сергей Жданов',
                  'created_at': 1585262863,
                  'description': 'testDesc Chech',
                  'id': 110,
                  'is_enabled': True,
                  'name': 'testName',
                  'signals': [...],
                  'updated_at': 1585294925},
         'meta': {'calls_left': 19993,
                  'calls_used': 7,
                  'error_code': 0,
                  'error_message': '',
                  'riskscore_profile': {'id': 110, 'name': 'testName'},
                  'server_time': 1585295226}}
        """
        check_type(profile_id, int)

        response = self._crystal.session().get(
            url=self._to_endpoint(self._GET_PROFILE_DETAILS.format(profile_id=profile_id)),
        )

        self._raise_for_error(response)

        return response.json()

    def edit_profile(self, profile_id: int, name: str, description: str) -> dict:
        """
        Method edits the profile name and description

        :param profile_id: Profile ID
        :param name: Profile name
        :param description: Profile description
        :return:
        {'meta': {'calls_left': 19993,
                  'calls_used': 7,
                  'error_code': 0,
                  'error_message': '',
                  'riskscore_profile': {'id': 110, 'name': 'alex'},
                  'server_time': 1585297854}}
        """
        check_type(profile_id, int)
        check_type(name, str)
        check_type(description, str)

        response = self._crystal.session().post(
            url=self._to_endpoint(self._EDIT_PROFILE.format(profile_id=profile_id)),
            params={
                'name': name,
                'description': description
            }
        )

        self._raise_for_error(response)

        return response.json()

    def delete_profile(self, profile_id: int) -> dict:
        """
        Method deletes the Risk Score profile
        !!! Profile must be disabled (is_enabled: False), use enable_profile(...)

        :param profile_id: Profile ID
        :return:
        {'meta': {'calls_left': 19993,
                  'calls_used': 7,
                  'error_code': 0,
                  'error_message': '',
                  'riskscore_profile': {'id': 0, 'name': 'Default'},
                  'server_time': 1585297926}}
        """
        check_type(profile_id, int)

        response = self._crystal.session().delete(
            url=self._to_endpoint(self._DELETE_PROFILE.format(profile_id=profile_id)),
        )

        self._raise_for_error(response)

        return response.json()

    def enable_profile(self, profile_id: int) -> dict:
        """
        Method enables Risk Score profile
        Sets the profile 'is_enabled' value to 'true' and for other profiles to 'false'

        :param profile_id: Profile ID
        :return:
        {'meta': {'calls_left': 19993,
                  'calls_used': 7,
                  'error_code': 0,
                  'error_message': '',
                  'riskscore_profile': {'id': 111, 'name': 'test'},
                  'server_time': 1585298143}}
        """
        check_type(profile_id, int)

        response = self._crystal.session().post(
            url=self._to_endpoint(self._ENABLE_PROFILE.format(profile_id=profile_id)),
        )

        self._raise_for_error(response)

        return response.json()

    def edit_entity_type(self, profile_id: int, signal: str, risk_score=None, recv=None, sent=None) -> dict:
        """
        Method edits Risk Score profile settings for the specified entity type

        :param profile_id: Profile ID
        :param signal: Signal type (see _SIGNAL_LIST)
        :param risk_score: Optional, is a metric that helps estimate the chance that an entity,
        address or transaction is related to illegal activity
        :param recv: Optional, receiving direction
        :param sent: Optional, sending direction
        :return:
        {'meta': {'calls_left': 19993,
                  'calls_used': 7,
                  'error_code': 0,
                  'error_message': '',
                  'riskscore_profile': {'id': 111, 'name': 'test'},
                  'server_time': 1585298666}}
        """
        check_type(profile_id, int)

        # signal value validation
        signal = signal.lower()
        if signal and (signal not in self._SIGNAL_LIST):
            raise ValueError('Check "signal" value')

        # other params validation
        params = {}
        if risk_score:
            if not (0 <= risk_score <= 1):
                raise ValueError('Check "risk_score" value')
            params['riskscore'] = risk_score
        if recv:
            recv = recv.lower()
            if not (recv in self._RECV_LIST):
                raise ValueError('Check "recv" value')
            params['recv'] = recv
        if sent:
            sent = sent.lower()
            if not (sent in self._SENT_LIST):
                raise ValueError('Check "sent" value')
            params['sent'] = sent

        response = self._crystal.session().post(
            url=self._to_endpoint(self._EDIT_ENTITY_TYPE.format(profile_id=profile_id, signal=signal)),
            params=params
        )

        self._raise_for_error(response)

        return response.json()

    def reset_settings(self, profile_id: int) -> dict:
        """
        Method resets Risk Score profile settings to the default settings created by Crystal team

        :param profile_id: Profile ID
        :return:
        {'meta': {'calls_left': 19993,
                  'calls_used': 7,
                  'error_code': 0,
                  'error_message': '',
                  'riskscore_profile': {'id': 111, 'name': 'test'},
                  'server_time': 1585299020}}
        """
        check_type(profile_id, int)

        response = self._crystal.session().post(
            url=self._to_endpoint(self._RESET_SETTINGS.format(profile_id=profile_id)),
        )

        self._raise_for_error(response)

        return response.json()
