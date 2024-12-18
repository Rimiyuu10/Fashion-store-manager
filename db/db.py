from sqlite3 import connect

def create_db():
    conn = connect('shop.db')

    # Foreign key support
    conn.execute('PRAGMA foreign_keys = ON;')

    # Create tables
    conn.execute('''
        CREATE TABLE IF NOT EXISTS SanPham (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ten_sp TEXT NOT NULL,
            mo_ta TEXT NOT NULL,
            gia NUMERIC NOT NULL,
            so_luong_s INTEGER NOT NULL,
            so_luong_m INTEGER NOT NULL,
            so_luong_l INTEGER NOT NULL,
            so_luong_xl INTEGER NOT NULL,
            mau_sac TEXT NOT NULL,
            hinh_anh TEXT NOT NULL DEFAULT 'default.jpg',
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS NhanVien (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ten_nv TEXT NOT NULL,
            dia_chi TEXT NOT NULL,
            sdt TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            vai_tro TEXT NOT NULL,
            ten_dang_nhap TEXT NOT NULL UNIQUE,
            mat_khau TEXT NOT NULL,
            quyen_han INTEGER NOT NULL DEFAULT 1,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS DonHang (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nguoi_mua TEXT NOT NULL,
            sdt_nguoi_mua TEXT NOT NULL,
            dia_chi_giao_hang TEXT NOT NULL,
            trang_thai INTEGER NOT NULL DEFAULT 1,
            tong_tien NUMERIC NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS ChiTietDonHang (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_don_hang INTEGER NOT NULL,
            id_san_pham INTEGER NOT NULL,
            so_luong_s INTEGER NOT NULL,
            so_luong_m INTEGER NOT NULL,
            so_luong_l INTEGER NOT NULL,
            so_luong_xl INTEGER NOT NULL,
            don_gia NUMERIC NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            FOREIGN KEY (id_don_hang) REFERENCES DonHang(id),
            FOREIGN KEY (id_san_pham) REFERENCES SanPham(id)
        );
    ''')

    # Commit and close
    conn.commit()
    conn.close()


class DbConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            # Apply create_db() to create tables if not exists
            create_db()

            cls._instance = connect('shop.db')
            cls._instance.execute('PRAGMA foreign_keys = ON;')
        return cls._instance

    def __del__(self):
        self._instance.close()

    @classmethod
    def get_instance(cls):
        return cls._instance if cls._instance is not None else cls()

    @classmethod
    def insert(cls, self):
        tbl_name = self._table_name
        properties = self._properties
        values = [getattr(self, prop) for prop in properties]
        placeholders = ['?' for _ in properties]

        query = f'''
            INSERT INTO {tbl_name} ({', '.join(properties)})
            VALUES ({', '.join(placeholders)});
        '''
        cls.get_instance().execute(query, values)

    @classmethod
    def delete(cls, self):
        tbl_name = self._table_name
        query = f'''
            DELETE FROM {tbl_name}
            WHERE id = ?;
        '''
        cls.get_instance().execute(query, (self.id,))

    @classmethod
    def commit(cls):
        cls.get_instance().commit()

    @classmethod
    def update(cls, self):
        tbl_name = self._table_name
        properties = self._properties
        values = [getattr(self, prop) for prop in properties]

        query = f'''
            UPDATE {tbl_name}
            SET {', '.join([f"{prop} = ?" for prop in properties])}
            WHERE id = ?;
        '''
        cls.get_instance().execute(query, values + [self.id])

    @classmethod
    def fetch_all(cls, cls_type: type, where: dict = None, order_by: str = 'created_at', offset: int = None, limit: int = None, like: dict = None) -> list:
        tbl_name = cls_type._table_name
        properties = cls_type._properties

        query = f'''
            SELECT {', '.join(properties)}
            FROM {tbl_name}
        '''
        if where:
            query += ' WHERE ' + ' AND '.join([f"{key} = ?" for key in where.keys()])
        if like and not where:
            query += ' WHERE ' + ' AND '.join([f"{key} LIKE ?" for key in like.keys()])
        elif like:
            query += ' AND ' + ' AND '.join([f"{key} LIKE ?" for key in like.keys()])
        if order_by:
            query += f' ORDER BY {order_by}'
        if offset is not None and limit is not None:
            query += f' LIMIT {offset}, {limit}'

        cursor = cls.get_instance().execute(query, list(where.values() if where else []) + list(map(lambda x: f"%{x}%", list(like.values() if like else []))))
        res = cursor.fetchall()
        # Convert to list of objects (with same order as properties)
        for i in range(len(res)):
            obj = cls_type()
            for j, prop in enumerate(properties):
                setattr(obj, prop, res[i][j])
            res[i] = obj
        return res

    @classmethod
    def count(cls, cls_type: type, where: dict = None, like: dict = None) -> int:
        tbl_name = cls_type._table_name

        query = f'''
            SELECT COUNT(*)
            FROM {tbl_name}
        '''
        if where:
            query += ' WHERE ' + ' AND '.join([f"{key} = ?" for key in where.keys()])
        if like and not where:
            query += ' WHERE ' + ' AND '.join([f"{key} LIKE ?" for key in like.keys()])
        elif like:
            query += ' AND ' + ' AND '.join([f"{key} LIKE ?" for key in like.keys()])

        cursor = cls.get_instance().execute(query, list(where.values() if where else []) + list(map(lambda x: f"%{x}%", list(like.values() if like else []))))
        return cursor.fetchone()[0]

    @classmethod
    def last_insert_id(cls):
        return cls.get_instance().execute('SELECT last_insert_rowid();').fetchone()[0]

    @classmethod
    def sum(cls, cls1, param, where: dict = None):
        tbl_name = cls1._table_name
        query = f'''
            SELECT SUM({param})
            FROM {tbl_name}
        '''
        if where:
            query += ' WHERE ' + ' AND '.join([f"{key} = ?" for key in where.keys()])
        cursor = cls.get_instance().execute(query, list(where.values() if where else []))
        return cursor.fetchone()[0] or 0
