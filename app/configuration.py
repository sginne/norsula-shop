class Configuration():
    user=''
    password=''
    btc_master_key = ''

    database_url = './db/main'
    wtf_csrf = True
    salt = 'salt'
    btc_rate_url = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=EUR'
    shop_name="Laffkashop"
    shop_url="laffka6wwduoexvb.onion"
    btc_net = "Main"  # Test for testnet, otherwise MainNet
    debugging = True
    port=5678 #Port to serve for debugging or no. if not set, 5000 applied
    update_rate_sec = 60  # checking btc rate every ... seconds
    update_tx_sec = 300  # checking TX's every ... seconds.
    check_cutoff=60*60*24*30 #30 days in seconds
    secret_key='supersecretkey'


    #dont modify below
    import binascii, os, hashlib
    user=hashlib.sha224(user.encode('utf-8')).hexdigest()
    password=hashlib.sha224(password.encode('utf-8')).hexdigest()
    #secret_key = binascii.hexlify(os.urandom(24))
    header=shop_name+" - "+shop_url
    if btc_net=="Test":
        tx_url="https://testnet.blockchain.info/q/addressbalance/"
    else:
        tx_url="https://blockchain.info/q/addressbalance/"
