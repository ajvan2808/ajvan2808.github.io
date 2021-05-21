from flask import Flask

app = Flask(__name__)
app.secret_key = '12345'

import Game_Shop.app_Index
import Game_Shop.app_Cart
import Game_Shop.app_Checkout
import Game_Shop.app_GameShop
import Game_Shop.app_Customer
import Game_Shop.app_Admin