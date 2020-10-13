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
## Class MyPanel2
###########################################################################

class PanelTimKiemThongTin ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		gbSizer4 = wx.GridBagSizer( 0, 0 )
		gbSizer4.SetFlexibleDirection( wx.BOTH )
		gbSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Tìm theo tên", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		self.m_staticText9.Wrap( -1 )

		gbSizer4.Add( self.m_staticText9, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.txtTenTimKIem = wx.SearchCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtTenTimKIem.ShowSearchButton( True )
		self.txtTenTimKIem.ShowCancelButton( False )
		gbSizer4.Add( self.txtTenTimKIem, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 5 ), wx.ALL, 5 )


		bSizer2.Add( gbSizer4, 1, wx.ALL|wx.EXPAND, 5 )

		self.listCtrDSSV_tim_thay = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT)
		bSizer2.Add( self.listCtrDSSV_tim_thay, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		# Connect Events
		self.txtTenTimKIem.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.txtTenTimKiem_searched )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def txtTenTimKiem_searched( self, event ):
		# Lấy giá trị tìm kiếm người dùng nhập vào
		ten_tim_kiem = event.GetString()
		xl_sinh_vien = SinhVien(duong_dan_sinh_vien)

		ds_sv_tim_thay = xl_sinh_vien.tim_kiem_sinh_vien(ten_tim_kiem)
		self.listCtrDSSV_tim_thay.DeleteAllItems()
		for sv in ds_sv_tim_thay:
			index = self.listCtrDSSV_tim_thay.GetItemCount()
			self.listCtrDSSV_tim_thay.InsertItem(index, sv["Ho_ten"])
			self.listCtrDSSV_tim_thay.SetItem(index, 1, sv["Ma_so_sinh_vien"])
			self.listCtrDSSV_tim_thay.SetItem(index, 2, sv["Ma_lop"])
			self.listCtrDSSV_tim_thay.SetItem(index, 3, sv["Ngay_sinh"])
			self.listCtrDSSV_tim_thay.SetItem(index, 4, sv["Noi_sinh"])


