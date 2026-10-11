# %%
#Uniform-Cost Search(UCS)

import matplotlib.pyplot as plt
import networkx as nx 
import heapq
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
    #l-0
    'A': [('B',2),('C',3)],
    #l-1
    'B': [('A',2),('D',5),('E',1)],
    'C': [('A',3),('F',7),('G',6)],
    #l-2
    'D': [('B',5),('H',4),('I',5)],
    'E': [('B',1),('J',2),('K',3)], 
    'F': [('C',7),('L',1),('M',2)],
    'G': [('C',6),('N',3), ('O',2)],
    #l-3
    'H': [('D',4)], 
    'I': [('D',5)], 
    'J': [('E',2)],
    'K': [('E',3)] ,
    'L': [('F',1)],
    'M': [('F',2)],
    'N': [('G',3)],
    'O': [('G',2)]
}


def create_ucs_tree(data,s_node,g_node):
    G=nx.Graph()
    for node, neighbors in data.items():
        for neighbor,cost in neighbors:
            G.add_edge(node,neighbor,weight=cost)
    prt_queue=[] #val with cost
    heapq.heappush(prt_queue,(0,s_node,[s_node]))

    visited={}
    traversal_order=[]
    goal_found=False
    final_cost=0

    while prt_queue:
        curr_cost,curr_node,path=heapq.heappop(prt_queue)
        if curr_node in visited and visited[curr_node] <= curr_cost:
            continue
            
        visited[curr_node]=curr_cost
        traversal_order.append(f"{curr_node}({curr_cost})")
        if curr_node==g_node:
            goal_found=True
            final_cost=curr_cost
        waiting_node=[item[1] for item in prt_queue] 
        nd_color=[]
        #node color
        for node in G.nodes():
            if node==g_node and node in visited:
                nd_color.append("#EF0A0A")
            elif node==curr_node:
                nd_color.append("#CE624F")
            elif node in visited:
                nd_color.append("#84C1AB")
            elif node in waiting_node:
                nd_color.append("#99A88A")
            else:
                nd_color.append("#9AD655")

        #clear screen
        clear_output(wait=True)

        #visualization
        fig, axis=plt.subplots(figsize=(8,3))
        if goal_found:
            axis.set_title(f"GOAL '{g_node}' FOUND!! Total Min Cost: {final_cost}", fontweight='bold', color="#1D4C1C", fontsize=10)
        else:
            axis.set_title(f"Processing: '{curr_node}' (Current Path Cost: {curr_cost})", fontweight='bold', color="#2E2E2E")

        nx.draw(
            G,
            pos=node_pos,
            node_color=nd_color,
            node_size=400,
            with_labels=True,
            font_size=9,
            font_weight="bold",
            edge_color="black",
            ax=axis
        )
        edge_labels = nx.get_edge_attributes(G, 'weight')
        #visualize tree
        nx.draw_networkx_edge_labels(G, pos=node_pos, edge_labels=edge_labels, font_size=8, font_color='purple')

        axis=axis.gca() if hasattr(axis,'gca') else axis
        #Traversal path
        axis.text(
            0.5,
            -0.15,
            "Traversal Order: " + " -> ".join(traversal_order), 
            transform=axis.transAxes,
            ha="center",
            fontsize=10,
            fontweight='bold'
        )

        display(fig)
        plt.close(fig)
        time.sleep(1.4)

        if goal_found:
            return True
        for neighbor,cost in reversed(data[curr_node]):
            total_cost=curr_cost+cost
            if neighbor not in visited or total_cost<visited[neighbor]:
                heapq.heappush(prt_queue,(total_cost,neighbor,path+[neighbor]))
               
    return False
create_ucs_tree(adj_node,s_node='A',g_node='G')
# %%
