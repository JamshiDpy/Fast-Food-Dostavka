from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili
ChannelInside = env.int("CHANNEL_INSIDE")
ChannelOutside = env.int("CHANNEL_OUTSIDE")
CAFE_LOCATION = env.str("CAFE_LOCATION")
SMS_TOKEN = env.str("SMS_TOKEN")
