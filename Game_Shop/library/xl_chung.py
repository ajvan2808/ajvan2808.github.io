from flask import request, render_template, redirect, url_for, session, Markup
from Game_Shop import app
from mysql.connector import connect
from Game_Shop.library.xl_json import *
import pymysql

# Biến MySQL 
conn_mysql = pymysql.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'root',
	database = 'gameshop',
	port = 3306
)

# danh_sach_game = doc_danh_sach_game()
# cursor = conn_mysql.cursor()

# # Thêm Column vào table Products 
# query = 'ALTER TABLE Products ADD Images VARCHAR(100) AFTER Description'
# cursor.execute(query)
# conn_mysql.commit()
# print('OK')


# # lọc dict category ra ngoài, xử lý trùng key
# the_loai_game = {}
# for games in danh_sach_game:
# 	the_loai = games['Category']
# 	ma_so = the_loai['ID']
# 	ten_the_loai = the_loai['Type']
# 	the_loai_game[ma_so] = [ten_the_loai]

# for para1, para2 in the_loai_game.items():
# 	chuoi_mysql = 'INSERT INTO Category VALUES(%s, %s)'
# 	cursor.execute(chuoi_mysql, (para1, para2[0]))
# 	conn_mysql.commit()


# for game in danh_sach_game:
# 	chuoi_mysql = 'INSERT INTO Products VALUES(%s, %s, %s, %s, %s, %s)'
# 	cursor.execute(chuoi_mysql, (game['Game_ID'], game['Name'], game['Price'], 
# 									game['Description'],
# 									game['Images'],
# 									game['Category']['ID']))
# 	conn_mysql.commit()

# conn_mysql.close()