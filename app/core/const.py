DB_HOST = "192.168.0.10"
DB_USER = "postgres"
DB_PASSWORD = "password"
DB_NAME = "help_desk"
DB_PORT= 5432
DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

JWT_EXPIRED_MSG = "Your JWT token is expired! Renew the JWT token!"
JWT_INVALID_MSG = "Invalid JWT token!"
SECRET_KEY = "5a3bd8c4b9a77ff3f2173ad74a87f70e1fef428279a097e1d9d207f87f0d3c3d"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30