class Configuration():
    adminkey1='123456'
    adminkey2='234567'
    database_url = './db/main'
    wtf_csrf = True
    salt = 'salt'
    btc_rate_url = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=EUR'
    btc_master_key = 'belt arrange uphold soul dinosaur meat pave version heavy used spatial skin'
    shop_name="⛁ Laffkashop"
    shop_url="laffka6wwduoexvb.onion"
    btc_net = "Test"  # Test for testnet, otherwise MainNet
    update_rate_sec = 60  # checking btc rate every ... seconds
    update_tx_sec = 300  # checking TX's every ... seconds.
    check_cutoff=60*60*24*30 #30 days in seconds


    #dont modify below
    import binascii, os
    secret_key = binascii.hexlify(os.urandom(24))
    header=shop_name+" - "+shop_url
    if btc_net=="Test":
        tx_url="https://testnet.blockchain.info/q/addressbalance/"
    else:
        tx_url="https://blockchain.info/q/addressbalance/"