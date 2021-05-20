from Game_Shop.library.xl_chung import *
from Game_Shop.library.xl_san_pham import *
from datetime import datetime

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
	danh_sach_game = doc_danh_sach_game()
	danh_sach_game_gio_hang = []

	if session.get('session_GioHang'):
		danh_sach_game_gio_hang = session['session_GioHang']['Gio_hang']
		
	chuoi_kq = ''
	chuoi_redirect = ''
	if request.form.get('DatHang'):
		if session.get('session_customer') is None:
			chuoi_kq = '<div class="alert alert-warning" role="alert" style="font-size: 16px;">You are not log in. <a href="/log-in">Log in now </a></div>'
		else:
			ma_khach_hang = session['session_customer']['Customer_ID']
			tong_thanh_tien = thong_tin_gio_hang(danh_sach_game_gio_hang)[0]
			don_hang = Order(CustomerID=ma_khach_hang, Order_date=datetime.now(),Total=tong_thanh_tien)
			session_sqlalchemy.add(don_hang)
			session_sqlalchemy.commit()

			for game in danh_sach_game_gio_hang:
				thanh_tien = game['So_luong'] * game['Price']
				chi_tiet_don_hang = Order_detail(OrderID=don_hang.Order_ID, GameID=game['Game_ID'],
													Quantity=game['So_luong'], Game_price=game['Price'], Order_total=thanh_tien)
				session_sqlalchemy.add(chi_tiet_don_hang)
				session_sqlalchemy.commit()

			session.pop('session_GioHang', None)
			danh_sach_game_gio_hang = []
			chuoi_kq = '<div class="alert alert-success" role="alert" style="font-size: 16px;">Order succeed. Thank you!</div>'
			chuoi_redirect = '<meta http-equiv = "refresh" content = "1; url = /" />'
	
	tong_thanh_tien, tong_so_luong = thong_tin_gio_hang(danh_sach_game_gio_hang)
	if session.get('session_GioHang'):
		tong_thanh_tien, tong_so_luong = thong_tin_gio_hang(session['session_GioHang']['Gio_hang'])
		danh_sach_game_gio_hang = session['session_GioHang']['Gio_hang']

	return render_template('Checkout/checkout.html', DanhSachGame=danh_sach_game, SESSION_SQLALCHEMY=session_sqlalchemy, PRODUCTS=Products,
								DanhSachGameGioHang=danh_sach_game_gio_hang,
								TongThanhTien=tong_thanh_tien,
								TongSoLuong=tong_so_luong, ChuoiKQ=Markup(chuoi_kq), ChuoiRedirect=Markup(chuoi_redirect))