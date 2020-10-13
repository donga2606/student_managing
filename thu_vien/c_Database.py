import sqlite3


class Database(object):
    # Khởi tạo kết nối đến DB
    def __init__(self, path_db):
        self.conn = sqlite3.connect(path_db)

    # TRUY XUẤT
    # Truy xuất lấy danh sách các item
    def get_all(self, chuoi_sql, bieu_thuc_dieu_kien=()):
        noi_dung = self.conn.execute(chuoi_sql, bieu_thuc_dieu_kien)
        danh_sach = noi_dung.fetchall()
        return danh_sach

    # Truy xuất lấy 1 item
    def get_one(self, chuoi_sql, bieu_thuc_dieu_kien=()):
        noi_dung = self.conn.execute(chuoi_sql, bieu_thuc_dieu_kien)
        doi_tuong = noi_dung.fetchone()
        return doi_tuong

    # THỰC THI: INSERT, UPDATE, DELETE
    def execute(self, chuoi_sql, bieu_thuc_dieu_kien=()):
        try:
            noi_dung = self.conn.execute(chuoi_sql, bieu_thuc_dieu_kien)
            self.conn.commit()
            return noi_dung.rowcount
        except:
            return None
    # Ngắt kết nối với DB
    def disconnect(self):
        self.conn.close()



