import sys

# Initialisation d'une classe Graph pour le réseau
class Graph:
    def __init__(self, vertices):
        self.V = vertices   # Nombre de noeuds
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]  # Matrice d'adjacence

    # Fonction pour trouver le sommet avec la distance minimale qui n'a pas été encore traité
    def min_distance(self, dist, spt_set):
        min_val = sys.maxsize
        min_index = -1
        for v in range(self.V):
            if dist[v] < min_val and not spt_set[v]:
                min_val = dist[v]
                min_index = v
        return min_index

    # Fonction pour afficher le résultat du plus court chemin
    def print_solution(self, dist):
        print("Sommet \tDistance depuis l'origine")
        for node in range(self.V):
            print(f"{node} \t {dist[node]}")

    # Implémentation de l'algorithme de Dijkstra
    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V  # Initialisation de la distance des noeuds à l'infini
        dist[src] = 0  # La distance du noeud source est 0
        spt_set = [False] * self.V  # Définir le tableau de sommets traités (shortest path tree)

        for _ in range(self.V):
            # Sélectionner le sommet de distance minimale non encore traité
            u = self.min_distance(dist, spt_set)
            spt_set[u] = True  # Marquer le sommet u comme traité

            # Mettre à jour la valeur de dist des sommets adjacents du sommet sélectionné
            for v in range(self.V):
                if self.graph[u][v] > 0 and not spt_set[v] and dist[u] + self.graph[u][v] < dist[v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.print_solution(dist)

# Exemple d'utilisation du graphe avec 5 sommets
g = Graph(5)

# Matrice d'adjacence du graphe (réseau)
g.graph = [
    [0, 10, 0, 30, 100],
    [10, 0, 50, 0, 0],
    [0, 50, 0, 20, 10],
    [30, 0, 20, 0, 60],
    [100, 0, 10, 60, 0],
]

# Appliquer l'algorithme à partir du noeud source (0)
g.dijkstra(0)
