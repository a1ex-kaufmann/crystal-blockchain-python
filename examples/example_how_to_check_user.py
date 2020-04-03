from crystal_blockchain import CrystalETH
from examples.config import API_KEY

from pprint import pprint

crystal_eth = CrystalETH(API_KEY)

# user_id = 'uuid'
# some_data = 'some data or maybe timestamp'
# user_token = crystal_eth.customer.create_customer(
#     name=user_id,
#     note=some_data
# )['data']['token']
#
# # blockchain parsing and search transactions for the address whose we need
#
# # ...
# # ...
# # ...
#
# # add transfer 1
# new_transfer = crystal_eth.transfers.add_tx_to_customer(
#     tx='0xf7679f92ddd49236c257a178ae6dc52ba60aab7ad031956defcadffa7350137e',
#     direction='deposit',
#     address='0xbdb6f9bd274ba69fbbbdb23f67db81b410300d3a',
#     name=user_id
# )
# pprint(new_transfer)
#
# # add transfer N
# # ...
#
#
# get dangerous transfers. If list is blank -> user is safe
# dangerous_transfers = crystal_eth.transfers.get_customer_txs(
#     token='7DWgbyU6Rf7E5FH4',
#     filter_dict={'riskscore_from': 0.4}
# )
# pprint(dangerous_transfers)
