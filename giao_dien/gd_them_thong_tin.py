# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from thu_vien.c_sinh_vien import *
from thu_vien.xl_chung import *
###########################################################################
## Class MyPanel3
###########################################################################

class PanelThemSinhVien ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 600,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):

        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"THÊM SINH VIÊN", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)

        self.m_staticText2.SetFont(
            wx.Font(15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        bSizer3.Add(self.m_staticText2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gbSizer1 = wx.GridBagSizer(0, 0)
        gbSizer1.SetFlexibleDirection(wx.BOTH)
        gbSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"Họ và tên", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)

        gbSizer1.Add(self.m_staticText5, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.txtHoTen = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.txtHoTen.SetMinSize(wx.Size(250, -1))

        gbSizer1.Add(self.txtHoTen, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u"Mã số sinh viên", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)

        gbSizer1.Add(self.m_staticText6, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.txtMSSV = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.txtMSSV.SetMinSize(wx.Size(250, -1))

        gbSizer1.Add(self.txtMSSV, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"Nơi sinh", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)

        gbSizer1.Add(self.m_staticText7, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.txtNoiSinh = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.txtNoiSinh.SetMinSize(wx.Size(250, -1))

        gbSizer1.Add(self.txtNoiSinh, wx.GBPosition(2, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, u"Ngày sinh", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)

        gbSizer1.Add(self.m_staticText8, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.txtNgaySinh = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.txtNgaySinh.SetMinSize(wx.Size(120, -1))

        gbSizer1.Add(self.txtNgaySinh, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText10 = wx.StaticText(self, wx.ID_ANY, u"Mã lớp", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)

        gbSizer1.Add(self.m_staticText10, wx.GBPosition(1, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        choiceMaLopChoices = []
        self.choiceMaLop = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceMaLopChoices, 0)
        self.choiceMaLop.SetSelection(0)
        self.choiceMaLop.SetMinSize(wx.Size(120, -1))

        gbSizer1.Add(self.choiceMaLop, wx.GBPosition(1, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.btnThemSInhVien = wx.Button(self, wx.ID_ANY, u"Thêm", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.btnThemSInhVien, wx.GBPosition(3, 0), wx.GBSpan(1, 4), wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer3.Add(gbSizer1, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer3)
        self.Layout()


    # Connect Events
        self.choiceMaLop.Bind( wx.EVT_CHOICE, self.choiceMaLop_clicked )
        self.btnThemSInhVien.Bind( wx.EVT_BUTTON, self.btnThemSinhVien_clicked )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def choiceMaLop_clicked( self, event ):
        ma_lop = self.choiceMaLop.GetStringSelection()
        return ma_lop


    def btnThemSinhVien_clicked( self, event ):
        # Ket noi voi csdl va tao list cac dictionary
        xl_sinh_vien = SinhVien(duong_dan_sinh_vien)

        # Lay thong tin user da dien
        ho_ten = self.txtHoTen.GetValue().strip()
        mssv = self.txtMSSV.GetValue().strip()
        ngay_sinh = self.txtNgaySinh.GetValue().strip()
        noi_sinh = self.txtNoiSinh.GetValue().strip()
        ma_lop = self.choiceMaLop_clicked(self)

        # Check xem thông tin đã được điền đầy đủ chưa tránh tình trạng để trống
        flag = 1
        if ho_ten == "" or mssv  == "" or ngay_sinh == "" or noi_sinh == "":
            flag = 0
            wx.MessageBox("Bạn chưa điền đầy đủ thông tin","Thông báo", wx.OK|wx.ICON_WARNING)

        if flag == 1:
            kq = xl_sinh_vien.them_sinh_vien(ho_ten,mssv,ma_lop,ngay_sinh,noi_sinh)
            if kq:
                wx.MessageBox("Thêm thông tin thành công","Thông báo", wx.OK|wx.ICON_INFORMATION)
            else:
                wx.MessageBox("Thêm thông tin thất bại, vui lòng kiểm tra lại MSSV", "Thông báo", wx.OK|wx.ICON_ERROR)






