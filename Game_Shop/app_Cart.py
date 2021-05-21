from Game_Shop.library.xl_chung import *
from Game_Shop.library.xl_san_pham import *

@app.route('/cart', methods=['GET', 'POST'])
def cart():
	danh_sach_game = doc_danh_sach_game()
	danh_sach_game_gio_hang = []
	khach_hang_dang_nhap = []

	chuoi_html= ''
	chuoi_khach_hang = ''
	if session.get('session_customer'):
		khach_hang_dang_nhap = session['session_customer']
		chuoi_html = '<a href="/log-out">Logout</a>'
		chuoi_khach_hang = '<li><a href="/cart"><i class="fa fa-user"></i>'+ khach_hang_dang_nhap['Fullname'] +'</a></li>'
	else:
		chuoi_html = '<a href="/log-in">Login</a>'

	if session.get('session_GioHang'):
		danh_sach_game_gio_hang = session['session_GioHang']['Gio_hang']

	if request.form.get('GioHang'):
		danh_sach_game_gio_hang_moi = []
		for game in danh_sach_game_gio_hang:
			so_luong = int(request.form.get('SoLuongGH' + str(game['Game_ID'])))
			game['So_luong'] = so_luong
			danh_sach_game_gio_hang_moi.append(game)
		
		session['session_GioHang'] = {'Gio_hang': danh_sach_game_gio_hang_moi}
	
	if request.form.get('XoaSPGioHang'):
		ma_game = int(request.form.get('XoaSPGioHang'))
		game_xoa = lay_chi_tiet_game(danh_sach_game_gio_hang, ma_game)
		danh_sach_game_gio_hang.remove(game_xoa)

		session['session_GioHang'] = {'Gio_hang': danh_sach_game_gio_hang}

	tong_thanh_tien, tong_so_luong = thong_tin_gio_hang(danh_sach_game_gio_hang)
	if session.get('session_GioHang'):
		tong_thanh_tien, tong_so_luong = thong_tin_gio_hang(session['session_GioHang']['Gio_hang'])
		danh_sach_game_gio_hang = session['session_GioHang']['Gio_hang']

	return render_template('Cart/cart.html', DanhSachGame=danh_sach_game, SESSION_SQLALCHEMY=session_sqlalchemy, PRODUCTS=Products,
								DanhSachGameGioHang=danh_sach_game_gio_hang,
								TongThanhTien=tong_thanh_tien,
								TongSoLuong=tong_so_luong, ChuoiHTML=Markup(chuoi_html), ChuoiKhachHang=Markup(chuoi_khach_hang))