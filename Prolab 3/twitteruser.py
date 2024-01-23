class TwitterUser:
    def __init__(self, user_name, full_name, followers_count, following_count, language, region, tweets, followers, following):
        self.user_name = user_name
        self.full_name = full_name
        self.followers_count = followers_count
        self.following_count = following_count
        self.language = language
        self.region = region
        self.tweets = tweets
        self.followers = followers
        self.following = following
      
    def __repr__(self):
        return f"TwitterUser(user_name={self.user_name}, full_name={self.full_name}, followers_count={self.followers_count}, following_count={self.following_count}, language={self.language}, region={self.region}, tweets={self.tweets}, followers={self.followers}, following={self.following})"
