import pylast

# You have to have your own unique two values for API_KEY and API_SECRET
# Obtain yours from https://www.last.fm/api/account/create for Last.fm
API_KEY = "6b86e8a864f4072b7918fd93ac96809b"  # this is a sample key
API_SECRET = "84b4c08ff9acbb0ebcba744c08023b72"

# In order to perform a write operation you need to authenticate yourself
username = "wd7512"
password_hash = pylast.md5("Password")

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash)
