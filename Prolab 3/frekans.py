
from dict_hashtable import users

def count_words_in_tweet(tweet):
    words = ''.join(tweet).split()
    word_counts = {}
    for word in words:
        if word not in word_counts:
            word_counts[word] = 0
        word_counts[word] += 1
    return word_counts

def get_user_interest(user_name):
    for user in users:
        if user.user_name == user_name:
            word_counts = count_words_in_tweet(user.tweets)
            user.interest = max(word_counts, key=word_counts.get)
            return user.interest

def create_interests_hash_tables():
    interests_hash_tables = {}
    for user in users:
        if user.interest not in interests_hash_tables:
            interests_hash_tables[user.interest] = []
        interests_hash_tables[user.interest].append(user.user_name)
    return interests_hash_tables

def get_common_interests(user1, user2):
    user1_interest = get_user_interest(user1)
    user2_interest = get_user_interest(user2)
    common_interests = []
    if user1_interest == user2_interest:
        common_interests.append(user1_interest)
    return common_interests


def print_common_interests(user1, user2):
    common_interests = get_common_interests(user1, user2)
    if common_interests:
        print(f"{user1} ve {user2} ortak ilgi alanları:")
        for interest in common_interests:
            print(f"#{interest}")
    else:
        print(f"{user1} ve {user2} ortak ilgi alanına sahip değil.")

interests_hash_tables = create_interests_hash_tables()

user1 = input("Birinci kullanıcıyı giriniz: ")
user2 = input("İkinci kullanıcıyı giriniz: ")

print_common_interests(user1, user2)