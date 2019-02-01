# Norsula
>Sell everything, your keys are your properties, your freedom is .onion land.
>Py3 opensource application specialized for hidden onion. service providing.
>Application implements bitcoin checkouts and simple private key sweeping

[Readme wiki](../../wiki)


1. [ What If? ](#whatif)
2. [ How to? ](#howto)

<a name="whatif"></a>
## What if I could tell you...

<a name="#howdoi"></a>
## How do I...

Requirements - [**python3**](https://www.python.org/download/releases/3.0/), might work on Windows machine uses cron in the same way, never checked, why bother.

From own experience can say, that installing on **Centos 7.4** provided by [Evolution Host] (https://evolution-host.com/) takes under 15 minutes.

1. ```yum -y install git``` we require git to clone Laffka on filesystem.
2. ```yum -y install https://centos7.iuscommunity.org/ius-release.rpm``` we need to install IUS for **Python3**
3. ```yum -y install python36u``` we need. or at least I have used **3.6** Python
4. ```yum -y install python36u-pip``` and finally we need **pip** for aquired python.
5. ```git clone https://github.com/eruina/laffka.git``` we need clone **Laffka** in order to use it, of course.
6. ```cd laffka```
7. ```pip3.6 install -r requirements.txt``` for Laffka, we need next python packages: [requests](http://docs.python-requests.org/en/master/),[Flask](http://flask.pocoo.org/),[Flask-APScheduler](https://github.com/viniciuschiele/flask-apscheduler), [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/), [bitmerchant](https://github.com/sbuss/bitmerchant),[Flask-Login](https://flask-login.readthedocs.io/en/latest/), [Flask-Session](https://pythonhosted.org/Flask-Session/), [waitress](https://docs.pylonsproject.org/projects/waitress/en/latest/)
