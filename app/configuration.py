class Configuration():
    user='faceless'
    password='1234qwerasdfzxcv'

    database_url = './db/hydro.db'
    wtf_csrf = True
    salt = 'salt'
    btc_rate_url = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=EUR'
    btc_master_key = 'culture bright tiger bone tonight multiply connect engage useless festival despair load'
    shop_name="Hydrafinil"
    shop_url="http://hydrai4gff7sohjw.onion/"
    btc_net = "Main"  # Test for testnet, otherwise MainNet
    update_rate_sec = 60  # checking btc rate every ... seconds
    update_tx_sec = 300  # checking TX's every ... seconds.
    check_cutoff=60*60*24*30 #30 days in seconds
    secret_key='doddiofoddioe'


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