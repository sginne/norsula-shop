# Laffka
## Introduction
>Opensource torshop application written in Python 3, and powered by Flask.

Application was developed with hidden service in mind after realisation, that customers cant withdraw money from [Valhalla market](valhallaxmn3fydu.onion), only vendors can.

I think this is very unfriendly, and I deem hiddenservice market places as a dumb idea at all. Centralized drug selling place, honeypot for LEOs. And exitscams.

Many would do perfectly fine with own small shop hidden somewhere in __onion land.__

Well, here it is, my solution - **Laffka**. Most important Laffkas feature is that one doesnt need daemons or blockchain to receive payments.

Payments go to the publcic bitcoin addresses, while private keys are stored in sqlite database, and can be later sweeped from any selfrespectable bitcoin wallet there are.

Bitcoin public and private addresses are generated from mnemonics in __/app/config.py__ (Remember, you HAVE to edit this file in order to run Laffka)

## Installation
