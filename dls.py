# %%
#Depth-Limited Search(DLS)
import matplotlib.pyplot as plt
import networkx as nx 
import collections
from IPython.display import clear_output, display
import time
#Node position(based on X & Y axis,Y dec , X right to left)
node_pos={
    #L-1
    'A':(4,4),
    #L-2
    'B': (3,3),
    'C': (5,3),
    #L-3
    'D': (1,2),
    'E': (3,2),
    'F': (5,2),
    'G': (7,2),
    #L-4
    'H': (0.5,1),
    'I': (1.5,1),
    'J': (2.5,1),
    'K': (3.5,1) ,
    'L': (4.5,1),
    'M': (5.5,1),
    'N': (6.5,1),
    'O': (7.5,1)
}

#Tree Layers
adj_node={
    #L-0
    'A':['B','C'],
    #L-2
    'B':['A','D','E'],
    'C':['A','F','G'],
    #L-3
    'D':['B','H','I'],
    'E':['B','J','K'] ,
    'F':['C','L','M'],
    'G':['C','N','O'],
    #L-4
    'H':['D'] ,
    'I':['D'] ,
    'J':['E'],
    'K':['E'],
    'L':['F'],
    'M':['F'],
    'N':['G'],
    'O':['G']
}


def create_dls_tree(data,s_node,limit,g_node):
    G = nx.Graph()
    for node, neighbors in data.items():
        for neighbor in neighbors:
            G.add_edge(node,neighbor)
    #if already visited
    visited={s_node}
    #contain visited node
    visit_order = []
    #LIFO
    stack=collections.deque([(s_node,0)])
    goal_found = False

    while stack:
        curr,curr_depth=stack.pop()
        visit_order.append(curr)
        if curr==g_node:
            goal_found = True
        nd_color=[]
        waiting_node=[item[0] for item in stack] 
        for node in G.nodes():
            if node == g_node and node in visit_order: nd_color.append("#EF0A0A")
            elif node==curr:
                nd_color.append("#CE624F")
            elif node in visited:
                nd_color.append("#84C1AB")
            elif node in waiting_node:
                nd_color.append("#D5C368")
            else:
                nd_color.append("#7FDF12")

        #clear screen
        clear_output(wait=True)

        #visualization
        fig, axis=plt.subplots(figsize=(8,3))
        axis.set_title(f"DLS Step: Node '{curr}' (Depth: {curr_depth} | Limit: {limit})", fontweight='bold')

        if goal_found:
            axis.set_title(f"DLS Step: GOAL NODE '{g_node}' FOUND at Depth {curr_depth}!", fontweight='bold', color="red")
        else:
            axis.set_title(f"DLS Step: Node '{curr}' (Depth: {curr_depth} | Limit: {limit})", fontweight='bold', color="#4A4A4A")
        #visualize tree
        nx.draw(
            G,
            pos=node_pos,
            node_color=nd_color,
            node_size=400,
            with_labels=True,
            font_weight="bold",
            edge_color="black",
            ax=axis
        )
        axis.text(
            0.5,
            -0.12,
            "Visited: " + " -> ".join(visit_order),
            transform=axis.transAxes,
            ha="center",
            fontsize=10
        )

        display(fig)
        plt.close(fig)
        time.sleep(1.4)
        if goal_found:
            break
        if curr_depth<limit:
            for neighbor in reversed(data[curr]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append((neighbor,curr_depth+1))

create_dls_tree(adj_node, s_node='A',limit=3, g_node='E')

# %%
