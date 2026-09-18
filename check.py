#!/usr/bin/env python3
"""Look up the on-chain balance and tx count of a Bitcoin address."""

import json
import sys
import urllib.request

API_TEMPLATE = "https://blockstream.info/api/address/{}"


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: python3 check.py <btc-address>", file=sys.stderr)
        return 1

    address = sys.argv[1]
    if not address.startswith(("1", "3", "bc1")):
        print("invalid bitcoin address format", file=sys.stderr)
        return 1

    try:
        with urllib.request.urlopen(API_TEMPLATE.format(address), timeout=15) as resp:
            data = json.load(resp)
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    stats = data["chain_stats"]
    balance = (stats["funded_txo_sum"] - stats["spent_txo_sum"]) / 1e8
    print(f"address : {address}")
    print(f"balance : {balance:.8f} BTC")
    print(f"tx count: {stats['tx_count']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
