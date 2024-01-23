import json
from faker import Faker
from tqdm import tqdm

fake_tr = Faker("tr_TR")  
fake_en = Faker("en_US")

def generate_fake_twitter_data(user_count=50000):
   
    twitter_data_list = []
    user_names = []

    for _ in tqdm(range(user_count)):
        user_name = fake_tr.user_name()
        user_names.append(user_name)
        full_name = fake_tr.name()
        followers_count = fake_tr.random_int(min=0, max=20)
        following_count = fake_tr.random_int(min=0, max=20)
        language = fake_tr.language_code()
        region = fake_tr.country()

        tweet_count = fake_tr.random_int(min=1, max=10)
        tweets = [fake_en.text(max_nb_chars=fake_tr.random_int(min=20, max=140)) for _ in range(tweet_count)]

        followers = generate_fake_followers(user_names, user_count=fake_tr.random_int(min=0, max=20))  # Her kullanıcının 0 ile 50 arasında takipçisi olsun
        following = generate_fake_following(user_names, user_count=fake_tr.random_int(min=0, max=20))  # Her kullanıcının 0 ile 50 arasında kişiyi takip etmesini sağlayalım

        for other_user in following:
            if user_name not in followers:
                followers.append(other_user)

        twitter_data = {
            "user_name": user_name,
            "full_name": full_name,
            "followers_count": followers_count,
            "following_count": following_count,
            "language": language,
            "region": region,
            "tweets": tweets,
            "followers": followers,
            "following": following
        }

        twitter_data_list.append(twitter_data)

    return twitter_data_list

def generate_fake_followers(user_names, user_count=1):
  
    followers_list = []
    for _ in range(user_count):
        follower_name = fake_tr.user_name()
        while follower_name in user_names:
            follower_name = fake_tr.user_name()
        followers_list.append(follower_name)
    return followers_list

def generate_fake_following(user_names, user_count=1):
    following_list = []
    for _ in range(user_count):
        following_name = fake_tr.user_name()
        while following_name in user_names:
            following_name = fake_tr.user_name()
        following_list.append(following_name)
    return following_list

def save_to_json(data, filename="ela_furkan_data20.json"):
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


fake_twitter_data = generate_fake_twitter_data(user_count=50000)
save_to_json(fake_twitter_data)