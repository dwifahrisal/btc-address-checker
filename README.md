# btc-address-checker

Query the balance and transaction count of any Bitcoin address using the free Blockstream API.

## Usage

```bash
python3 check.py bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh
```

```
address : bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh
balance : 0.00500000 BTC
tx count: 12
```

## Notes

- Public API, no key required.
- Supports legacy (1), P2SH (3) and bech32 (bc1) addresses.
