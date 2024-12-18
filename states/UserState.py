from models import NhanVien


class UserState():
    user: NhanVien = None

    @staticmethod
    def set_user(user: NhanVien | None):
        UserState.user = user

    @staticmethod
    def get_user() -> NhanVien | None:
        return UserState.user
