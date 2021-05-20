from Game_Shop.library.xl_model import *
from sqlalchemy.orm import sessionmaker

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session_sqlalchemy = DBSession()

def doc_danh_sach_game():
	danh_sach = []
	obj_danh_sach_game = session_sqlalchemy.query(Products).all()
	for item in obj_danh_sach_game:
		game = {
			"Game_ID": item.Game_ID,
			"Name": item.Name,
			"Price": item.Price,
			"Description": item.Description,
			"Images": item.Images,
			"Type_ID": item.Type_ID
		}
		danh_sach.append(game)
	return danh_sach

def lay_chi_tiet_game(danh_sach_game, game_id):
	danh_sach_game = list(filter(lambda sp: sp['Game_ID'] == game_id, danh_sach_game))
	sp_game = danh_sach_game[0] if len(danh_sach_game) == 1 else None
	return sp_game

def thong_tin_gio_hang(danh_sach_game_gio_hang):
	tong_thanh_tien = 0
	tong_so_luong = 0
	for game_trong_gio_hang in danh_sach_game_gio_hang:
		thanh_tien = game_trong_gio_hang['So_luong'] * game_trong_gio_hang['Price']
		tong_thanh_tien += thanh_tien
		tong_so_luong += game_trong_gio_hang['So_luong']
	return tong_thanh_tien, tong_so_luong
