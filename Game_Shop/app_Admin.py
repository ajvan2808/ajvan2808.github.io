from Game_Shop.library.xl_chung import *
from Game_Shop.library.xl_san_pham import *
from Game_Shop.library.xl_model import *
from flask_admin import Admin, BaseView, expose, form
from sqlalchemy import exc
from flask_login import UserMixin, LoginManager, current_user, login_user, logout_user
from flask_admin.contrib.sqla import ModelView
from wtforms import fields, widgets
import os
import os.path as op
import PIL

app.config['STATIC_FOLDER'] = app.static_folder

file_path = op.join(op.dirname(__file__), 'static')
try:
	os.mkdir(file_path)
except OSError:
	pass

app.config['SQLALCHEMY_DATABASE_URI'] = connect_var
admin = Admin(app, name='X Game Admin', template_mode='bootstrap4')

configure_mappers()
Base.metadata.bind=engine
DBSession = sessionmaker(bind=engine)
session_sqlalchemy = DBSession()

login = LoginManager(app)

@login.user_loader
def load_user(id):
	shop_admin = session_sqlalchemy.query(ShopAdmin).filter(ShopAdmin.id==id).first()
	return shop_admin

def render_image(self, context, model, name):
	if not model.Images:
		return ''
	return Markup('<img src="%s" width="100" alt="%s" />' %(url_for('static', filename='img/' + model.Images), model.Images))

class MyModelView(ModelView):
	def is_accessible(self):
		return current_user.is_authenticated 

class MyModelView_1(BaseView):
	def is_accessible(self):
		return current_user.is_authenticated


class CKTextAreaWidget(widgets.TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += ' ckeditor'
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)

class CKTextAreaField(fields.TextAreaField):
    widget = CKTextAreaWidget()


class Category_View(MyModelView):
	column_display_pk = False
	can_create=True
	can_delete = True
	can_export=True
	column_list = ('Type', 'ID')
	form_columns = ('Type',)
	column_labels = {'ID': 'Category ID', 'Type': 'Type of category'}

class Products_View(MyModelView):
	olumn_display_pk = False
	can_create=True
	can_delete = True
	can_export=True
	column_list = ('Images', 'Name', 'Price', 'category')
	form_columns = ('Name', 'Price', 'Description', 'Images', 'category')
	column_labels = {
		'Game_ID': 'Game ID',
		'Name': 'Title',
		'Price': 'Price',
		'Description': 'Description',
		'Images': 'Image',
		'Type_ID': 'Category ID',
		'category': 'Category'
	}

	column_formatters = {
		'Images': render_image
	}

	form_extra_fields = {
		'Images': form.ImageUploadField('Image', base_path=file_path)
	}

	form_overrides = {
		'Description': CKTextAreaField
	}

	page_size = 10
	create_template = 'Admin/addnew.html'
	edit_template = 'Admin/update.html'

class MyView(MyModelView_1):
	@expose('/')
	def index(self):
		danh_sach_game_myview = doc_danh_sach_game()

		return self.render('Admin/myview.html', DanhSachGameMyView=danh_sach_game_myview)

class Logout(MyModelView_1):
	@expose('/')
	def index(self):
		logout_user()
		return redirect(url_for('admin_login'))

admin.add_view(Category_View(Category, session_sqlalchemy, 'Category'))
admin.add_view(Products_View(Products, session_sqlalchemy, 'Game products'))
admin.add_view(MyView('My View'))
admin.add_view(Logout('Log out'))


@app.route('/admin/log-in', methods=['GET', 'POST'])
def admin_login():
    chuoi_kq = ''
    if request.form.get('Ad_UserName'):
        # gán biến
        ten_dang_nhap = request.form.get('Ad_UserName')
        mat_khau = request.form.get('Ad_Passwrd')

        # Truy xuất dữ liệu
        shopadmin = session_sqlalchemy.query(ShopAdmin).filter(ShopAdmin.Username_Ad == ten_dang_nhap and ShopAdmin.Password_Ad == mat_khau).first()
        if shopadmin:
            login_user(shopadmin)
            return redirect(url_for('admin.index'))
        else:
            chuoi_kq = 'Log in failed'

    return render_template('Admin/log_in.html', ChuoiKQ=chuoi_kq)

# @app.route('/admin/myview', methods=['GET', 'POST'])
# def admin_myview():
# 	danh_sach_game_myview = doc_danh_sach_game()

# 	return render_template('Admin/myview.html', DanhSachGameMyView=danh_sach_game_myview)
