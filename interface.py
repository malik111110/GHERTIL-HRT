from tkinter import Tk, Frame, Label, Entry, Button, Canvas, Scale, HORIZONTAL
from graph_generator import GraphGenerator
from ghertil import GhertilHRT


class Application(Tk):
    def __init__(self):
        super().__init__()
        self.title("Graphe et Algorithme Ghertil")
        self.geometry("1000x700")


        self.graph = GraphGenerator(num_nodes=10, min_edges=2, max_edges=4).generate()
        self.ghertil = GhertilHRT(self.graph)  # Passer le graphe généré
        self.init_ui()

    def init_ui(self):

        control_frame = Frame(self, width=200, bg="lightgrey", relief="ridge", borderwidth=2)
        control_frame.pack(side="left", fill="y")

        Label(control_frame, text="Noeud de départ:").pack(pady=5)
        self.start_node_entry = Entry(control_frame)
        self.start_node_entry.pack(pady=5)

        Label(control_frame, text="Noeud cible:").pack(pady=5)
        self.target_node_entry = Entry(control_frame)
        self.target_node_entry.pack(pady=5)

        Label(control_frame, text="Vitesse de l'animation:").pack(pady=5)
        self.speed_control = Scale(control_frame, from_=1, to=10, orient=HORIZONTAL)
        self.speed_control.set(5)
        self.speed_control.pack(pady=5)

        Button(control_frame, text="Générer Graphe", command=self.generate_graph).pack(pady=10)
        Button(control_frame, text="Trouver Chemin", command=self.find_path).pack(pady=10)

        # Canvas pour dessiner le graphe
        self.canvas = Canvas(self, bg="white")
        self.canvas.pack(side="right", fill="both", expand=True)

        self.draw_graph()

    def generate_graph(self):

        self.graph = GraphGenerator(num_nodes=10, min_edges=2, max_edges=4).generate()
        self.ghertil = GhertilHRT(self.graph)  # Mettre à jour Ghertil avec le nouveau graphe
        self.draw_graph()

    def find_path(self):

        start_node = self.start_node_entry.get()
        target_node = self.target_node_entry.get()

        if start_node.isdigit() and target_node.isdigit():
            start_node, target_node = int(start_node), int(target_node)
            path, cost = self.ghertil.find_path(start_node, target_node)
            if path:
                self.animate_path(path, cost)
            else:
                print("Aucun chemin trouvé.")
        else:
            print("Veuillez entrer des nombres valides.")

    def draw_graph(self):

        self.canvas.delete("all")
        self.update_idletasks()
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        if width <= 100 or height <= 100:
            print("Dimensions insuffisantes pour dessiner le graphe.")
            return

        self.node_positions = {}
        for node in self.graph:
            x, y = self.random_position(width, height, self.node_positions)
            self.node_positions[node] = (x, y)
            self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="blue")
            self.canvas.create_text(x, y, text=str(node), fill="white")

        for node, neighbors in self.graph.items():
            x1, y1 = self.node_positions[node]
            for neighbor, cost in neighbors.items():
                x2, y2 = self.node_positions[neighbor]
                self.canvas.create_line(x1, y1, x2, y2, fill="black")
                mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
                self.canvas.create_text(mid_x, mid_y, text=str(cost), fill='green')


    def random_position(self, width, height, positions):
        import random
        while True:
            x = random.randint(50, width - 50)
            y = random.randint(50, height - 50)
            # Vérifier qu'il n'y a pas de collision avec d'autres nœuds
            if all((x - px) ** 2 + (y - py) ** 2 > 50 ** 2 for px, py in positions.values()):
                return x, y

    def animate_path(self, path, cost):
        for i in range(len(path) - 1):
            start, end = path[i], path[i + 1]
            start_x, start_y = self.node_positions[start]
            end_x, end_y = self.node_positions[end]
            self.canvas.create_line(
                start_x, start_y, end_x, end_y, fill="red", width=3
            )
            self.update()
            self.after(int(500 / self.speed_control.get()))
        print(f"Coût total du chemin: {cost}")


if __name__ == "__main__":
    app = Application()
    app.mainloop()
