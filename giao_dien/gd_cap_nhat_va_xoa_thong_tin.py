# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from thu_vien.xl_chung import *
from thu_vien.c_sinh_vien import *
###########################################################################
## Class PanelCapNhatXoa
###########################################################################

class PanelCapNhatXoa ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Cập nhật hoặc xóa thông tin sinh viên", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer4.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"MSSV", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText8.Wrap( -1 )

		gbSizer2.Add( self.m_staticText8, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		choiceMSSVCapNhatChoices = []
		self.choiceMSSVCapNhat = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,-1 ), choiceMSSVCapNhatChoices, 0 )
		self.choiceMSSVCapNhat.SetSelection( 0 )
		gbSizer2.Add( self.choiceMSSVCapNhat, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 5 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( gbSizer2, 1, wx.EXPAND, 5 )

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Thay đổi" ), wx.VERTICAL )

		gbSizer6 = wx.GridBagSizer( 0, 0 )
		gbSizer6.SetFlexibleDirection( wx.BOTH )
		gbSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText13 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Họ tên", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		gbSizer6.Add( self.m_staticText13, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtHoTenCapNhat = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer6.Add( self.txtHoTenCapNhat, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Mã số sinh viên", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText14.Wrap( -1 )

		gbSizer6.Add( self.m_staticText14, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtMSSVCapNhat_readonly = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		gbSizer6.Add( self.txtMSSVCapNhat_readonly, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText15 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Mã lớp", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		gbSizer6.Add( self.m_staticText15, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtMaLopCapNhat = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer6.Add( self.txtMaLopCapNhat, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText16 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Ngày sinh", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		gbSizer6.Add( self.m_staticText16, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtNgaySinhCapNhat = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer6.Add( self.txtNgaySinhCapNhat, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText18 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Nơi sinh", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		gbSizer6.Add( self.m_staticText18, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtNoiSinhCapNhat = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer6.Add( self.txtNoiSinhCapNhat, wx.GBPosition( 2, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		sbSizer3.Add( gbSizer6, 1, wx.EXPAND, 5 )

		gbSizer7 = wx.GridBagSizer( 0, 0 )
		gbSizer7.SetFlexibleDirection( wx.BOTH )
		gbSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.btnXoa = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Xóa", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer7.Add( self.btnXoa, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		self.btnXoa.Enable(False)

		self.btnCapNhat = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Cập nhật", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer7.Add( self.btnCapNhat, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		self.btnCapNhat.Enable(False)

		sbSizer3.Add( gbSizer7, 1, wx.EXPAND, 5 )


		bSizer4.Add( sbSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		# Connect Events
		self.choiceMSSVCapNhat.Bind( wx.EVT_CHOICE, self.choiceMSSVCapNhat_clicked )
		self.btnXoa.Bind( wx.EVT_BUTTON, self.btnXoa_clicked )
		self.btnCapNhat.Bind( wx.EVT_BUTTON, self.btnCapNhat_clicked )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def choiceMSSVCapNhat_clicked( self, event ):
		xl_sinhvien = SinhVien(duong_dan_sinh_vien)
		mssv_cap_nhat = self.choiceMSSVCapNhat.GetStringSelection()

		sv_tim_thay = xl_sinhvien.lay_thong_tin_sinh_vien_theo_mssv(mssv_cap_nhat)

		self.txtMSSVCapNhat_readonly.SetValue(sv_tim_thay["Ma_so_sinh_vien"])
		self.txtHoTenCapNhat.SetValue(sv_tim_thay["Ho_ten"])
		self.txtMaLopCapNhat.SetValue(sv_tim_thay["Ma_lop"])
		self.txtNgaySinhCapNhat.SetValue(sv_tim_thay["Ngay_sinh"])
		self.txtNoiSinhCapNhat.SetValue(sv_tim_thay["Noi_sinh"])

		# Kích hoạt tính năng xóa và sửa sau khi user đã chọn sinh viên thích hợp
		self.btnXoa.Enable(True)
		self.btnCapNhat.Enable(True)

	def btnXoa_clicked( self, event ):

		xl_sinh_vien = SinhVien(duong_dan_sinh_vien)
		mssv_can_xoa = self.txtMSSVCapNhat_readonly.GetValue()

		kq = xl_sinh_vien.xoa_sinh_vien(mssv_can_xoa)

		if kq:
			wx.MessageBox("Xóa thành công mssv: " + mssv_can_xoa, "Thông Báo", wx.OK|wx.ICON_INFORMATION)
		else:
			wx.MessageBox("Không xóa thành công", "Thông báo", wx.OK|wx.ICON_ERROR)


	def btnCapNhat_clicked( self, event ):
		# Kết nối với database
		xl_sinh_vien = SinhVien(duong_dan_sinh_vien)

		# Lấy thông tin từ user
		mssv_can_cap_nhat = self.txtMSSVCapNhat_readonly.GetValue()
		ho_ten = self.txtHoTenCapNhat.GetValue()
		ma_lop = self.txtMaLopCapNhat.GetValue()
		ngay_sinh = self.txtNgaySinhCapNhat.GetValue()
		noi_sinh = self.txtNoiSinhCapNhat.GetValue()

		kq = xl_sinh_vien.cap_nhat_sinh_vien(ho_ten, ma_lop, ngay_sinh, noi_sinh, mssv_can_cap_nhat)

		if kq:
			wx.MessageBox("Cập nhật thành công mssv: " + mssv_can_cap_nhat, "Thông Báo", wx.OK | wx.ICON_INFORMATION)
		else:
			wx.MessageBox("Không cập nhật thành công", "Thông báo", wx.OK | wx.ICON_ERROR)


