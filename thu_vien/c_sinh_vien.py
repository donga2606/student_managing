from thu_vien.c_Database import *

class SinhVien(Database):

    def __init__(self, path_db):
        Database.__init__(self, path_db)

    def doc_danh_sach_sinh_vien(self):
        """
        Đọc danh sách từ file database chuyển thành list các dictionary. Có thể dùng class thì khi gọi sẽ tiện hơn.
        """
        chuoi_sql = "select * from ThongTinSinhVien"
        noi_dung = Database.get_all(self, chuoi_sql)
        ds_sinh_vien = []
        for dong in noi_dung:
            ds_sinh_vien.append({"Ho_ten":dong[0],"Ma_so_sinh_vien":dong[1],
                                 "Ma_lop":dong[2],"Ngay_sinh":dong[3],"Noi_sinh":dong[4]})
        return ds_sinh_vien

    def them_sinh_vien(self, ho_ten, mssv, ma_lop, ngay_sinh, noi_sinh):
        chuoi_sql = "insert into ThongTinSinhVien values (?,?,?,?,?)"
        kq = Database.execute(self, chuoi_sql, (ho_ten, mssv, ma_lop, ngay_sinh, noi_sinh))
        return kq

    def cap_nhat_sinh_vien(self, ho_ten, ma_lop, ngay_sinh, noi_sinh, mssv):
        chuoi_sql = "update ThongTinSinhVien set Ho_ten = ?, Ma_lop = ?, Ngay_sinh = ?," \
                    "Noi_sinh = ? where  Ma_so_sinh_vien = ?"
        kq = Database.execute(self, chuoi_sql, (ho_ten, ma_lop, ngay_sinh, noi_sinh, mssv))
        return kq

    def xoa_sinh_vien(self, mssv):
        chuoi_sql = "delete from ThongTinSinhVien where Ma_so_sinh_vien = ?"
        kq = Database.execute(self, chuoi_sql, (mssv,))
        return kq

    def lay_thong_tin_sinh_vien_theo_mssv(self, mssv_input):
        chuoi_sql = "select * from ThongTinSinhVien where Ma_so_sinh_vien = ?"
        sv = Database.get_one(self, chuoi_sql, (mssv_input,))
        sv_tim_thay = {"Ho_ten": sv[0], "Ma_so_sinh_vien": sv[1], "Ma_lop": sv[2], "Ngay_sinh": sv[3], "Noi_sinh": sv[4]}
        return sv_tim_thay

    def tim_kiem_sinh_vien(self, ten_tim_kiem):
        chuoi_sql = "select * from ThongTinSinhVien where Ho_ten like ?"
        pattern = "%"+ten_tim_kiem+"%"
        sv_tim_thay = Database.get_all(self, chuoi_sql, (pattern,))
        ds_sv_tim_thay = []
        for dong in sv_tim_thay:
            ds_sv_tim_thay.append({"Ho_ten":dong[0],"Ma_so_sinh_vien":dong[1],
                                 "Ma_lop":dong[2],"Ngay_sinh":dong[3],"Noi_sinh":dong[4]})
        return ds_sv_tim_thay

    def __del__(self):
        pass



# Test function
# xl_sinh_vien = SinhVien("D:\\project-nang_cao\\appBaiThi\\du_lieu\\quan_ly_sinh_vien.db")
# a = xl_sinh_vien.tim_kiem_sinh_vien("A")
# print(a)

# kq = xl_sinh_vien.them_sinh_vien("a","K490001","a","a","a")
# print(kq)



