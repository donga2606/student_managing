# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from giao_dien.gd_thong_tin_sinh_vien import *
from giao_dien.gd_them_thong_tin import *
from giao_dien.gd_cap_nhat_va_xoa_thong_tin import *
from giao_dien.gd_tim_kiem_thong_tin import *
from thu_vien.xl_chung import *
from thu_vien.c_sinh_vien import *


###########################################################################
## Class FrameChinh
###########################################################################

class FrameChinh(wx.MDIParentFrame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="Dữ liệu sinh viên", pos=wx.DefaultPosition,
                          size=wx.Size(1224, 655), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.m_menubar1 = wx.MenuBar(0)
        self.mnTaiKhoan = wx.Menu()
        self.mnItemDangNhap = wx.MenuItem(self.mnTaiKhoan, wx.ID_ANY, u"Đăng nhập", wx.EmptyString, wx.ITEM_NORMAL)
        self.mnTaiKhoan.Append(self.mnItemDangNhap)

        self.mnItemThoat = wx.MenuItem(self.mnTaiKhoan, wx.ID_ANY, u"Thoát", wx.EmptyString, wx.ITEM_NORMAL)
        self.mnTaiKhoan.Append(self.mnItemThoat)

        self.m_menubar1.Append(self.mnTaiKhoan, u"Tài khoản")

        self.m_menu2 = wx.Menu()
        self.mnItemTTSV = wx.MenuItem(self.m_menu2, wx.ID_ANY, u"Hiển thị thông tin sinh viên", wx.EmptyString,
                                      wx.ITEM_NORMAL)
        self.m_menu2.Append(self.mnItemTTSV)

        self.mnItemThemSV = wx.MenuItem(self.m_menu2, wx.ID_ANY, u"Thêm sinh viên", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu2.Append(self.mnItemThemSV)

        self.mnItemCapNhatXoaSV = wx.MenuItem(self.m_menu2, wx.ID_ANY, u"Cập nhật hoặc xóa thông tin sinh viên",
                                              wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu2.Append(self.mnItemCapNhatXoaSV)

        self.mnItemTimKiem = wx.MenuItem(self.m_menu2, wx.ID_ANY, u"Tìm kiếm sinh viên", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu2.Append(self.mnItemTimKiem)

        self.m_menubar1.Append(self.m_menu2, u"Chức năng")

        self.SetMenuBar(self.m_menubar1)

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_MENU, self.mnItemTTSV_clicked, id=self.mnItemTTSV.GetId())
        self.Bind(wx.EVT_MENU, self.mnItemThemSV_clicked, id=self.mnItemThemSV.GetId())
        self.Bind(wx.EVT_MENU, self.mnItemCapNhatXoa_clicked, id=self.mnItemCapNhatXoaSV.GetId())
        self.Bind(wx.EVT_MENU, self.mnItemTimKiem_clicked, id=self.mnItemTimKiem.GetId())

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def mnItemTTSV_clicked(self, event):

        # Moi khi user click lai thì sẽ tắt cái cũ di và load lai cái mới để cập nhật được thông tin mới nhất
        ds_Children = self.GetChildren()
        for children in ds_Children:
            if children.GetTitle() == 'Thông tin sinh viên':
                children.Close()

        # Tạo danh sách sinh viên
        xl_sinhvien = SinhVien(duong_dan_sinh_vien)
        ds_sinhvien = xl_sinhvien.doc_danh_sach_sinh_vien()

        app = wx.App()
        frame = wx.MDIChildFrame(self, title="Thông tin sinh viên", size=(720, 420))
        panel = PanelTTSV(frame)

        # Nhập tên cột vô Bảng thông tin
        panel.listCtrl_TTSV.InsertColumn(0, "Họ Tên")
        panel.listCtrl_TTSV.InsertColumn(1, "Mã Số Sinh Viên")
        panel.listCtrl_TTSV.InsertColumn(2, "Mã Lớp")
        panel.listCtrl_TTSV.InsertColumn(3, "Ngày Sinh")
        panel.listCtrl_TTSV.InsertColumn(4, "Nơi Sinh")

        # Nhập giá trị vô Bảng
        for sv in ds_sinhvien:
            index = panel.listCtrl_TTSV.GetItemCount()
            panel.listCtrl_TTSV.InsertItem(index, sv["Ho_ten"])
            panel.listCtrl_TTSV.SetItem(index, 1, sv["Ma_so_sinh_vien"])
            panel.listCtrl_TTSV.SetItem(index, 2, sv["Ma_lop"])
            panel.listCtrl_TTSV.SetItem(index, 3, sv["Ngay_sinh"])
            panel.listCtrl_TTSV.SetItem(index, 4, sv["Noi_sinh"])

        # panel.listCtrl_TTSV.Append((sv["Ho_ten"],Ơ sv["Ma_so_sinh_vien"], sv["Ma_lop"], sv["Ngay_sinh"], sv["Noi_sinh"]))
        frame.Show(True)
        app.MainLoop()

    def mnItemThemSV_clicked(self, event):
        # Khi bật lại chức năng thì nếu có sẵn rồi thì activate lại
        ds_Children = self.GetChildren()
        for children in ds_Children:
            if children.GetTitle() == "Thêm sinh viên":
                children.Activate()
                return

        app = wx.App()
        frame = wx.MDIChildFrame(self, title="Thêm sinh viên", size=(620, 320))
        panel = PanelThemSinhVien(frame)

        # ds_ma_lop ben xu_chung.
        panel.choiceMaLop.Append(ds_ma_lop)

        frame.Show(True)
        app.MainLoop()

    def mnItemCapNhatXoa_clicked(self, event):
        ds_Children = self.GetChildren()
        for children in ds_Children:
            if children.GetTitle() == 'Cập nhật hoặc xóa thông tin':
                children.Close()

        # Trích lấy ds ma so sinh viên để cho vào wxchoice cho user chọn
        xl_sinh_vien = SinhVien(duong_dan_sinh_vien)
        ds_sinhvien = xl_sinh_vien.doc_danh_sach_sinh_vien()
        ds_mssv = [i["Ma_so_sinh_vien"] for i in ds_sinhvien]

        app = wx.App()
        frame = wx.MDIChildFrame(self, title="Cập nhật hoặc xóa thông tin", size=(520, 320))

        # Cho vào wxchoice
        panel = PanelCapNhatXoa(frame)
        panel.choiceMSSVCapNhat.Append(ds_mssv)

        frame.Show(True)
        app.MainLoop()

    def mnItemTimKiem_clicked(self, event):
        # Nếu đã có app thì tắt app đi và khởi tạo app mới
        ds_Children = self.GetChildren()
        for children in ds_Children:
            if children.GetTitle() == 'Tìm kiếm thông tin sinh viên theo tên':
                children.Close()

        # Khỏi tạo app nhỏ, frame con
        app = wx.App()
        frame = wx.MDIChildFrame(self, title="Tìm kiếm thông tin sinh viên theo tên", size=(520,320))
        panel = PanelTimKiemThongTin(frame)

        # Thêm các cột vào list_ctrl
        panel.listCtrDSSV_tim_thay.InsertColumn(0, "Họ Tên")
        panel.listCtrDSSV_tim_thay.InsertColumn(1, "Mã Số Sinh Viên")
        panel.listCtrDSSV_tim_thay.InsertColumn(2, "Mã Lớp")
        panel.listCtrDSSV_tim_thay.InsertColumn(3, "Ngày Sinh")
        panel.listCtrDSSV_tim_thay.InsertColumn(4, "Nơi Sinh")

        frame.Show(True)
        app.MainLoop()