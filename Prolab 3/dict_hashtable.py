
from twitteruser import TwitterUser 
import json 

class HashTable:
  def __init__(self):
      self.table = {}

  def insert(self, key, value):
      self.table[key] = value

  def get(self, key):
      if key in self.table:
          return self.table[key]
      else:
          return None

  def remove(self, key):
      if key in self.table:
          del self.table[key]
      else:
          print("Key not found")
#tqdm
def create_twitter_user_objects(json_file):
  with open('ela_furkan_data20.json', 'r', encoding='utf-8') as f:
      data = json.load(f)

  users = []
  for user_data in data:
      user = TwitterUser(user_data['user_name'], user_data['full_name'], user_data['followers_count'], user_data['following_count'], user_data['language'], user_data['region'], user_data['tweets'], user_data['followers'], user_data['following'])
      users.append(user)

  return users

users = create_twitter_user_objects('ela_furkan_data20.json')

users_hash_table = HashTable()

for user in users:
 users_hash_table.insert(user.user_name, user)
 
 class Graph:
   def __init__(self):
       self.nodes = {}

   def add_node(self, node):
       if node not in self.nodes:
           self.nodes[node] = []

   def add_edge(self, node1, node2):
       self.nodes[node1].append(node2)

   def remove_node(self, node):
       if node in self.nodes:
           del self.nodes[node]

   def remove_edge(self, node1, node2):
       if node1 in self.nodes and node2 in self.nodes[node1]:
           self.nodes[node1].remove(node2)

graph = Graph()

for user in users:
   graph.add_node(user.user_name)
   for followed_user in user.following:
       graph.add_edge(user.user_name, followed_user)
       
       
