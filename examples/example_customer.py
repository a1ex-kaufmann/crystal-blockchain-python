"""
See 'Customer' at https://expert.crystalblockchain.com/docs/api
"""

from pprint import pprint

from crystal_blockchain import CrystalBTC, CrystalLTC, CrystalBCH, CrystalETH
from examples.config import API_KEY


crystal_btc = CrystalBTC(API_KEY)

# pprint(crystal_btc.customer.create_customer('name', 'comment'))

# pprint(crystal_btc.customer.get_customer_details('lhN7gPURdSQ5t3Aa'))

# pprint(crystal_btc.customer.edit_customer('lhN7gPURdSQ5t3Aa', True, 'testNewName', note=None))

# pprint(crystal_btc.customer.get_customers(
#     with_total=None,  # not required params
#     offset=None,
#     limit=None,
#     order=None,
#     direction=None,
#     filter_dict=None
# ))

# pprint(crystal_btc.customer.get_customer_addresses('Jo7EITvrnO7sZVIy'))
