# name: Stephen Wang
# date: November 16, 2020
# purpose: Loading data from dartmouth_graph.txt into vertices.txt

from vertex import Vertex

def load_graph(filename):
    vertex_dict = {}

    # First pass over data file (no adj lists)
    file = open(filename, "r")

    for l in file:
        section_split = l.split(";")

        vertex_name = section_split[0]
        coordinates = section_split[2].strip().split(", ")
        x_coor = int(coordinates[0])
        y_coor = int(coordinates[1])
        
        # create a graph vertex here and add it to the dictionary
        vertex_dict[vertex_name] = Vertex(vertex_name, x_coor, y_coor, [])

    file.close()

    # Second pass over data file (adding in adj lists)
    file = open(filename, "r")

    for l in file:
        section_split = l.split(";")
        vertex_name = section_split[0]
        adj_vertices = section_split[1].strip().split(", ")
        for vert in adj_vertices:
            vertex_dict[vertex_name].adj.append(vertex_dict[vert])

    file.close()

    return vertex_dict

vertex_dict = load_graph("dartmouth_graph.txt")

# write into vertices.txt
out_file = open("vertices.txt", "w")
for vertex in vertex_dict:
    out_file.write(str(vertex_dict[vertex]) + "\n")
out_file.close()