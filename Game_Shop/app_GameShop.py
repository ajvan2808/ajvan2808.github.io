from Game_Shop.library.xl_chung import *
from Game_Shop.library.xl_san_pham import *


@app.route('/game-shop', methods=['GET', 'POST'])
def game_shop():
	danh_sach_game = doc_danh_sach_game()
	danh_sach_game_gio_hang = []

	if request.form.get('MaGame'):
		if session.get('session_GioHang'):
			danh_sach_game_gio_hang = session['session_GioHang']['Gio_hang']

		ma_game = int(request.form.get('MaGame'))
		so_luong = 1
		san_pham_chon = lay_chi_tiet_game(danh_sach_game, ma_game)

		if lay_chi_tiet_game(danh_sach_game_gio_hang, ma_game) is not None:
			san_pham_chon_cu = lay_chi_tiet_game(danh_sach_game_gio_hang, ma_game)
			so_luong_cu = san_pham_chon_cu['So_luong']
			so_luong += so_luong_cu
			danh_sach_game_gio_hang.remove(san_pham_chon_cu)

		san_pham_chon['So_luong'] = so_luong
		danh_sach_game_gio_hang.append(san_pham_chon)
		session['session_GioHang'] = {'Gio_hang': danh_sach_game_gio_hang}

	tong_thanh_tien, tong_so_luong = thong_tin_gio_hang(danh_sach_game_gio_hang)
	if session.get('session_GioHang'):
		tong_thanh_tien, tong_so_luong = thong_tin_gio_hang(session['session_GioHang']['Gio_hang'])
		danh_sach_game_gio_hang = session['session_GioHang']['Gio_hang']

	return render_template('GameShop/game_shop.html', DanhSachGame=danh_sach_game, SESSION_SQLALCHEMY=session_sqlalchemy, PRODUCTS=Products,
								DanhSachGameGioHang=danh_sach_game_gio_hang,
								TongThanhTien=tong_thanh_tien,
								TongSoLuong=tong_so_luong)

	
