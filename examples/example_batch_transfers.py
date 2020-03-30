"""
See 'Batch Transfers' at https://expert.crystalblockchain.com/docs/api
"""

from pprint import pprint

from crystal_blockchain import CrystalBTC, CrystalLTC, CrystalBCH, CrystalUSDT, CrystalETH
from examples.config import API_KEY


crystal_btc = CrystalBTC(API_KEY)

# pprint(crystal_btc.batch_transfers.get_txs(
#     with_total=None,  # not required params
#     offset=None,
#     limit=None,
#     order=None,
#     direction=None,
#     filter_dict=None
# ))

# pprint(crystal_btc.batch_transfers.get_txs_bounds())

# pprint(crystal_btc.batch_transfers.edit_txs(
#     action=None,  # not required params
#     filter_dict=None
# ))
