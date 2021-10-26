import os

# Database initialization
if os.environ.get('DATABASE_URL') is None:
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    # id de l'app TEST
    FB_APP_ID = 2097060923780902
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL'].replace('postgres://', 'postgresql://')
    FB_APP_ID = 869310400439313

SECRET_KEY = "fbjgleoqq6g^z3=+(7x4&by=xl&nuf)z=y-aujb)#81h16vodooq++jgfb"
