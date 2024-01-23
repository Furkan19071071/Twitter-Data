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
        followers_count = 0
        following_count = 0
        language = fake_tr.language_code()
        region = fake_tr.country()

        tweet_count = fake_tr.random_int(min=1, max=10)
        tweets = [fake_en.text(max_nb_chars=fake_tr.random_int(min=20, max=140)) for _ in range(tweet_count)]

        followers = []
        following = []

        for other_user in user_names:
            if other_user != user_name and other_user not in followers and other_user not in following:
                if fake_tr.boolean(chance_of_getting_true=50):
                    followers.append(other_user)
                    followers_count += 1
                elif fake_tr.boolean(chance_of_getting_true=50):
                    following.append(other_user)
                    following_count += 1

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


def save_to_json(data, filename="ela_furkan_data21.json"):
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


fake_twitter_data = generate_fake_twitter_data(user_count=50000)
save_to_json(fake_twitter_data)