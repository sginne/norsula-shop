class Configuration():
    database_url = '/home/sginne/src/laffka.py/db/main'
    wtf_csrf = True
    salt = 'salt'
    btc_rate = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=EUR'
    btc_master_key = 'belt arrange uphold soul dinosaur meat pave version heavy used spatial skin'
    btc_net = "Test"  # Test for testnet
    header = '⛁ Laffkashop - laffka6wwduoexvb.onion'
    update_rate_sec = 60  # checking btc rate every ... seconds
    update_tx_sec = 300  # checking TX's every ... seconds.

    import binascii, os
    secret_key = binascii.hexlify(os.urandom(24))
