"""
See 'Transfers' at https://expert.crystalblockchain.com/docs/api
"""

from pprint import pprint

from crystal_blockchain import CrystalBTC, CrystalLTC, CrystalBCH, CrystalUSDT, CrystalETH
from examples.config import API_KEY


crystal_btc = CrystalBTC(API_KEY)

# pprint(crystal_btc.transfers.add_tx_to_customer(
#     tx='e066aacb7e05e9aef1b4215ad798c038dc62a2c32b2fed9c36dea0e6e2f6b3a4',
#     direction='deposit',
#     address='334H1BX1yajKx7Lmq2cSWA4e3aqa7PFF7r',
#     name='alex'
# ))

# pprint(crystal_btc.transfers.edit_tx('899107', archived=None, flagged=None))

# pprint(crystal_btc.transfers.update_tx('899107'))

# pprint(crystal_btc.transfers.get_customer_txs(
#     token='Jo7EITvrnO7sZVIy',
#     with_total=None,  # not required params
#     offset=None,
#     limit=None,
#     order=None,
#     direction=None,
#     filter_dict=None
# ))

# pprint(crystal_btc.transfers.get_tx_bounds('Jo7EITvrnO7sZVIy'))

# pprint(crystal_btc.transfers.edit_customer_txs('Jo7EITvrnO7sZVIy', action=None, filter_dict=None))
