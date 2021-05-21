from Game_Shop.library.xl_model import *
from sqlalchemy.orm import sessionmaker
from Game_Shop.library.xl_chung import *

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session_sqlalchemy = DBSession()

def doc_danh_sach_khach_hang():
	danh_sach_khach_hang = []
	obj_ds_khach_hang = session_sqlalchemy.query(Customer).all()
	for item in obj_ds_khach_hang:
		customer = {
			'Customer_ID': item.Customer_ID,
			'Fullname': item.Fullname,
			'Username': item.Username,
			'Password': item.Password,
			'Email': item.Email
		}
		danh_sach_khach_hang.append(customer)
	return danh_sach_khach_hang

def khach_hang_dang_nhap(danh_sach_khach_hang, username, password):
	danh_sach = list(filter(lambda khach_hang: khach_hang['Username']== username and khach_hang['Password']== password, danh_sach_khach_hang))
	kq = danh_sach[0] if len(danh_sach) > 0 else None
	return kq 

def chuoi_thong_tin_khach_hang(username):
	chuoi_html = ''' 
	<li><a href="#"><i class="fa fa-user"></i>'''+ username +'''</a></li>
	'''
	return Markup(chuoi_html)