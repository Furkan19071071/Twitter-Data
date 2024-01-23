from dict_hashtable import users
import networkx as nx
import matplotlib.pyplot as plt

from tqdm import tqdm
from bfs import bfs
from dfs import dfs
from userinfo import analiz

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = []

    def add_edge(self, node1, node2):
        if node1 not in self.nodes:
            self.add_node(node1)
        if node2 not in self.nodes:
            self.add_node(node2)
        self.nodes[node1].append(node2)
        self.nodes[node2].append(node1)

    def is_connected(self, node1, node2):
        if node1 not in self.nodes or node2 not in self.nodes:
            return False
        return node2 in self.nodes[node1]

    def neighbors(self, node):
        if node not in self.nodes:
            return []
        return self.nodes[node]

graph = Graph()
user1 = input("Birinci kullanıcıyı giriniz: ")
user2 = input("İkinci kullanıcıyı giriniz: ")

print("Yapmak İstediğiniz işlemi seçiniz")
print("1- Ortak Takipçileri Bul")
print("2- Ortak Takipçileri Göster")
print("3- Ortak Takipçileri Dosyaya Yaz")
print("4- Ortak Takipçileri Görselleştir")
print("5-Bir kullancının analizini yapma")
print("6-Ortak İlgi alanlarını Bulma ")
print("7- Çıkış")


while True:
    choice = input("Seçiminiz: ")

    if choice == "1":
        for user in tqdm(users):
            if user.user_name == user1 or user.user_name == user2:
                graph.add_node(user.user_name)
                for followed_user in user.following:
                    if followed_user == user1 or followed_user == user2:
                        graph.add_edge(user.user_name, followed_user)

        common_followers_bfs = bfs(graph, user1) & bfs(graph, user2)
        common_followers_dfs = dfs(graph, user1) & dfs(graph, user2)

        print("Ortak takipçiler (BFS):", list(common_followers_bfs))
        print("Ortak takipçiler (DFS):", list(common_followers_dfs))

    elif choice == "2":
        if nx.common_neighbors(graph, user1, user2):
            print("Ortak takipçiler:", list(nx.common_neighbors(graph, user1, user2)))
        else:
            print("Ortak takipçi yok.")

    elif choice == "3":
        if nx.common_neighbors(graph, user1, user2):
            with open("ortak_takipciler.txt", "w", encoding="utf-8") as f:
                f.write("Ortak takipçiler:\n")
                for takipci in nx.common_neighbors(graph, user1, user2):
                    f.write(f"{takipci}\n")
            print("Ortak takipçiler ortak_takipciler.txt dosyasına yazıldı.")
        else:
            print("Ortak takipçi yok.")

    elif choice == "4":
        G = nx.Graph()

        for node in graph.nodes:
            G.add_node(node)

        for node, edges in graph.nodes.items():
            for edge in edges:
                G.add_edge(node, edge)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True)

        if nx.common_neighbors(G, user1, user2):
            nx.draw_networkx_edges(G, pos, edgelist=list(nx.common_neighbors(G, user1, user2)), width=2)
        plt.show()
           
    elif choice == "5":
        user_name = input("Kullanıcı adı: ")
        result = analiz(user_name)
        print(result)


    elif choice == "7":
        print("Çıkılıyor...")
        break

    else:
        print("Geçersiz seçim. Lütfen 1-6 arasında bir seçim yapın.")