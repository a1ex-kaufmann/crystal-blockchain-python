from pprint import pprint

from crystal_blockchain import CrystalBTC
from examples.config import API_KEY


crystal_btc = CrystalBTC(API_KEY)

# pprint(crystal_btc.customer.create_customer('name', 'comment'))

# pprint(crystal_btc.customer.get_customer_details('lhN7gPURdSQ5t3Aa'))

# pprint(crystal_btc.customer.edit_customer('lhN7gPURdSQ5t3Aa', True, 'newName123'))

# pprint(crystal_btc.customer.get_customers())

# pprint(crystal_btc.customer.get_customer_addresses('lhN7gPURdSQ5t3Aa'))