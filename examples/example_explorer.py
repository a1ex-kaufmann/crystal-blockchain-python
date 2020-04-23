"""
See 'Explorer' at UserAPI.json
"""

from pprint import pprint

from crystal_blockchain import CrystalBTC, CrystalLTC, CrystalBCH, CrystalETH
from examples.config import API_KEY


# crystal_btc = CrystalBTC(API_KEY)
#
# pprint(crystal_btc.explorer.get_address_summary('17A16QmavnUfCW11DAApiJxp7ARnxN5pGX'))
#
# pprint(crystal_btc.explorer.get_tx_summary('2099c246f65668226597c606ce937b510ddfc4c5ebe0aedef6a66f6c9f7d9473'))

# crystal_ltc = CrystalLTC(API_KEY)
# pprint(crystal_ltc.explorer.get_address_summary('MSccR1YCQTydEXBnmTZ55XfZaHtFy6aoT9'))
# pprint(crystal_ltc.explorer.get_tx_summary('32b19b7d6f57f21a4fd0ca409c54c2e176561ee5c95dba29e908bd242c7bc1f7'))

# crystal_ltc = CrystalBCH(API_KEY)
# pprint(crystal_ltc.explorer.get_address_summary('qryh28y68dt3y6r9qnln773y2z7azyunrux3xmpu7g'))
# pprint(crystal_ltc.explorer.get_tx_summary('03f8e500dc008fe1719d0be987302479bf71a880282fae217b9c77baf3bf6d40'))

# crystal_ltc = CrystalETH(API_KEY)
# pprint(crystal_ltc.explorer.get_address_summary('0x63DFeB971713e262a1A79a055EC6f8CFE90D8FDF'))
# pprint(crystal_ltc.explorer.get_tx_summary('0xd1545e9c762f772a2b81cfbb4c839a80bb083b08422d59384ea9ea027e134e1e'))
