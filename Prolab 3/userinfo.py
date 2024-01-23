from matplotlib import pyplot as plt
from twitteruser import TwitterUser
import json 

def analiz(user_name):
    with open("ela_furkan_data20.json", "r", encoding="utf-8") as json_file:
        twitter_data_list = json.load(json_file)

    twitter_users = [TwitterUser(**twitter_data) for twitter_data in twitter_data_list]

    twitter_users_dict = {user.user_name: user for user in twitter_users}
    user = twitter_users_dict.get(user_name)

    if user is None:
        return "Kullanıcı bulunamadı."

    print(f"İsmi: {user.full_name}")
    print(f"Kullanıcının tweetleri: {user.tweets}")
    print(f"kullancının takip ettikleri:{user.following}")
    print(f"kullancının takipçileri:{user.followers}")
    print(f"kullanıcının bölgesi:{user.region}")

    follower_counts = [user.followers_count]
    following_counts = [user.following_count]

    plt.bar(range(len(user.tweets)), user.tweets, align='center')
    plt.xlabel("Tweet Sırası")
    plt.ylabel("Tweet Metni")
    plt.title(f"{user.user_name} Kullanıcısının Tweetleri")
    plt.show()

    plt.subplot(1, 2, 1)
    plt.hist(follower_counts, bins=10)
    plt.xlabel("Takipçi Sayısı")
    plt.ylabel("Kullanıcı Sayısı")
    plt.title("Kullanıcıların Takipçi Sayısı Dağılımı")

    plt.subplot(1, 2, 2)
    plt.hist(following_counts, bins=10)
    plt.xlabel("Takip Edilen Kullanıcı Sayısı")
    plt.ylabel("Kullanıcı Sayısı")
    plt.title("Kullanıcıların Takip Edilen Kullanıcı Sayısı Dağılımı")

    plt.show()

    return "Kullanıcı verileri başarıyla görüntülendi."