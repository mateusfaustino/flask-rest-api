import os


class Config:
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{os.getenv('MYSQL_USER', 'user')}:" \
        f"{os.getenv('MYSQL_PASSWORD', 'password')}@" \
        f"{os.getenv('MYSQL_HOST', 'db')}:{os.getenv('MYSQL_PORT', '3306')}/" \
        f"{os.getenv('MYSQL_DATABASE', 'app_db')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
