'''
import json
import os 
 
thu_muc_game = 'Game_Shop/data/game/'

def doc_file_json(duong_dan):
	f = open(duong_dan, encoding='utf-8')
	du_lieu = json.load(f)
	f.close()
	return du_lieu

def ghi_file_json(duong_dan, noi_dung):
	f = open(duong_dan, 'w',encoding='utf-8')
	json.dump(noi_dung, f, indent=4, ensure_ascii=False)
	f.close()
	return True

def doc_danh_sach_game():
	danh_sach_game = []
	for san_pham in os.listdir(thu_muc_game):
		duong_dan = thu_muc_game + san_pham
		san_pham = doc_file_json(duong_dan)
		danh_sach_game.append(san_pham)
	return danh_sach_game

# Cập nhật phần tử Image cho các file json

for tap_tin in os.listdir(thu_muc_game):
	duong_dan = thu_muc_game + tap_tin
	san_pham = doc_file_json(duong_dan)
	duong_dan_hinh_anh = san_pham['Name'].replace(' ', '')
	san_pham['Images'] = duong_dan_hinh_anh + '.jpg'
	kq = ghi_file_json(duong_dan, san_pham)
	if kq:
		confirm = 'OK'
	else:
		confirm = 'No'

'''