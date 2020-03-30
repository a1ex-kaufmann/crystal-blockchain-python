# joys-crystal-blockchain

Crystal-blockchain python wrap

### Examples of using

0. go to `/examples`
1. `cp ./config.example.py ./config.py`
2. edit API_KEY in config.py
3. uncomment methods & run examples

### Info

- API DOCS https://expert.crystalblockchain.com/docs/api
- RISK SCORE GUIDE https://expert.crystalblockchain.com/docs/riskscore-guide
- RISK SCORE PROFILES https://expert.crystalblockchain.com/user/profile (for creating new profiles)
- Each currency has its own unique endpoint (ex. BTC -> `https://apibtc.crystalblockchain.com`)
- See methods docstrings

## Using

```
from <some_config> import API_KEY
crystal_btc = CrystalBTC(API_KEY)
```

### Profile
```
crystal_btc.profile.get_profiles()           | GET /settings/riskscore/list
crystal_btc.profile.get_profile_details(...) | GET /settings/riskscore/one/{profile_id}
crystal_btc.profile.edit_profile(...)        | POST /settings/riskscore/one/{profile_id}
crystal_btc.profile.delete_profile(...)      | DELETE /settings/riskscore/one/{profile_id}
crystal_btc.profile.enable_profile(...)      | POST /settings/riskscore/one/{profile_id}/enable
crystal_btc.profile.edit_entity_type(...)    | POST /settings/riskscore/one/{profile_id}/{signal}
crystal_btc.profile.reset_settings(...)      | POST /settings/riskscore/one/{profile_id}/reset

``` 

### Customer
```
crystal_btc.customer.create_customer(...)        | POST /monitor/one
crystal_btc.customer.get_customer_details(...)   | GET /monitor/one/{token}
crystal_btc.customer.edit_customer(...)          | POST /monitor/one/{token}
crystal_btc.customer.get_customers()             | POST /monitor/list
crystal_btc.customer.get_customer_addresses(...) | GET /monitor/one/{token}/addresses
``` 

### Transfers
```
crystal_btc.transfers.add_tx_to_customer(...)    | POST /monitor/tx/add
crystal_btc.transfers.edit_tx(...)               | POST /monitor/tx/{id}/edit
crystal_btc.transfers.update_tx(...)             | POST /monitor/tx/{id}/update
crystal_btc.transfers.get_customer_txs(...)      | POST /monitor/one/{token}/txs
crystal_btc.transfers.get_tx_bounds(...)         | GET /monitor/one/{token}/tx-bounds
crystal_btc.transfers.edit_customer_txs(...)     | POST /monitor/one/{token}/txs/execute
``` 

### Batch Transfers
```
crystal_btc.batch_transfers.get_txs(...)        | POST /monitor/batch/txs
crystal_btc.batch_transfers.get_txs_bounds()    | GET /monitor/batch/tx-bounds
crystal_btc.batch_transfers.edit_txs(...)       | POST /monitor/batch/txs/execute
``` 

### Author
alexey.zhdanov for Joys Digital
