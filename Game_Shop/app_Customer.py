from Game_Shop.library.xl_chung import *
from Game_Shop.library.xl_san_pham import *
from Game_Shop.library.xl_khach_hang import *

@app.route('/log-in', methods=['GET', 'POST'])
def customer_log_in():
	danh_sach_game = doc_danh_sach_game()
	danh_sach_game_gio_hang = []

	if session.get('session_GioHang'):
		danh_sach_game_gio_hang = session['session_GioHang']['Gio_hang']
	
	chuoi_kq = ''
	danh_sach_khach_hang = doc_danh_sach_khach_hang()
	if request.form.get('UserName'):
		username = request.form.get('UserName')
		password = request.form.get('Passwrd')
		kq = khach_hang_dang_nhap(danh_sach_khach_hang, username, password)
		if kq is not None:
			session['session_customer'] = kq
			return redirect(url_for('index'))
		else:
			chuoi_kq = 'Failed to log-in. Please check Username and Password!'

	tong_thanh_tien, tong_so_luong = thong_tin_gio_hang(danh_sach_game_gio_hang)
	if session.get('session_GioHang'):
		tong_thanh_tien, tong_so_luong = thong_tin_gio_hang(session['session_GioHang']['Gio_hang'])
		danh_sach_game_gio_hang = session['session_GioHang']['Gio_hang']

	return render_template('Customer/log_in.html', DanhSachGame=danh_sach_game, SESSION_SQLALCHEMY=session_sqlalchemy, PRODUCTS=Products,
								DanhSachGameGioHang=danh_sach_game_gio_hang,
								TongThanhTien=tong_thanh_tien,
								TongSoLuong=tong_so_luong, ChuoiKQ=chuoi_kq)

@app.route('/log-out')
def customer_log_out():
    session.pop('session_customer', None)
    return redirect(url_for('customer_log_in'))