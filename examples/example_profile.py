from pprint import pprint

from crystal_blockchain import CrystalBTC, CrystalLTC, CrystalBCH, CrystalUSDT, CrystalETH
from examples.config import API_KEY


crystal_btc = CrystalBTC(API_KEY)

# pprint(crystal_btc.profile.get_profiles())

# pprint(crystal_btc.profile.get_profile_details(110))

# pprint(crystal_btc.profile.edit_profile(110, 'alex', 'testDesc'))

# pprint(crystal_btc.profile.delete_profile(110))

# pprint(crystal_btc.profile.enable_profile(111))

# pprint(crystal_btc.profile.edit_entity_type(
#     profile_id=111,
#     signal='ATM',
#     risk_score=0.50,
#     recv='mid',
#     sent='mid'
# ))

# pprint(crystal_btc.profile.reset_settings(111))
