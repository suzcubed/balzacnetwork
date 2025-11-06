import pandas as pd
import os
from collections import Counter
nodes_df = pd.read_csv('nodes_vs_export.csv')
nodes = [{'data': row.to_dict()} for _, row in nodes_df.iterrows()]
net_df = pd.read_csv('character_frequencies.csv')

# compile node mappings
scene_map = nodes_df.set_index(nodes_df['id'].str.strip().str.upper())['scene'].to_dict()
# sum frequencies
freq_count = (
    net_df.groupby("character")["frequency"].sum().to_dict()
    if "frequency" in net_df.columns else {}
)

def map_weights(freq): 
    if freq >= 500:
        return 5
    elif freq >= 100: 
        return 4
    elif freq >= 25:
        return 3
    elif freq >= 5:
        return 2
    elif freq > 0:
        return 1
    else:
        return 0
net_df['weight'] = net_df['frequency'].apply(map_weights)

edges = [
    {
        "data": {
            "source": str(row["character"]),
            "target": str(row["novel"]),
            "weight": row["weight"]  
        }
    }
    for _, row in net_df.iterrows()
]
from collections import Counter
novel_counts = Counter(net_df['novel'])

for node in nodes: 
    if node['data']['type'] == 'novel':
        node_id = node['data']['id']
        node['data']['shape'] = 'square'
        node['data']['scene'] = scene_map.get(node_id, "UNKNOWN")
        scene = node['data']['scene']
        degree = novel_counts.get(node_id, 0)
        
        # tiered sizing
        if degree <= 2:
            node['data']['size'] = 20
        elif degree <= 5:
            node['data']['size'] = 30
        elif degree <= 10:
            node['data']['size'] = 40
        elif degree <= 20:
            node['data']['size'] = 50
        else:
            node['data']['size'] = 60

        # set color by scenes 
        colors = {
            'SCENES DE LA VIE PRIVEE': 'blue',
            'SCENES DE LA VIE PARISIENNE': '#FF6F61',
            'SCENES DE LA VIE PROVINCE': 'sandybrown',
            'SCENES DE LA VIE POLITIQUE': 'goldenrod',
            'SCENES DE LA VIE DE CAMPAGNE': 'mediumseagreen',
            'SCENES DE LA VIE MILITAIRE': 'lightsteelblue',
            'ETUDES PHILOSOPHIQUES': 'plum',
        }    
        node['data']['color'] = colors.get(scene, 'gray')
        
    # character nodes
    elif node['data']['type'] == 'character':
        node_id = node['data']['id']
        node['data']['color'] = 'skyblue'
        node['data']['shape'] = 'dot'

        # dynamic sizing
        total_freq = freq_count.get(node_id, 0)
        
        # set size based on total frequency
        if total_freq <= 50:
            node['data']['size'] = 15
        elif total_freq <= 100:
            node['data']['size'] = 20
        elif total_freq <= 200:
            node['data']['size'] = 25
        elif total_freq <= 400:
            node['data']['size'] = 30
        elif total_freq <= 700:
            node['data']['size'] = 40
        elif total_freq <= 1000:
            node['data']['size'] = 50
        elif total_freq <= 1500:
            node['data']['size'] = 70
        elif total_freq <= 2000:
            node['data']['size'] = 85
        else:  # 2001+
            node['data']['size'] = 100

# GRAPH SET UP 
from pyvis.network import Network

net = Network(
    height='1050px', width='100%',
    notebook=False,            # don't embed in notebook
    select_menu=True,
    filter_menu=True,
    neighborhood_highlight=True,
    cdn_resources='remote'     
)


# create nodes based on mapping 
for node in nodes:
    net.add_node(
        node['data']['id'],
        label=node['data'].get('label', 'UNKNOWN'),
        color=node['data'].get('color', 'black'),
        shape=node['data'].get('shape', 'star'),
        size=node['data'].get('size', 10),
        **{k:v for k,v in node['data'].items() if k not in ['id','label','color', 'shape', 'size']}
    )

# create the edges as char, novel 
for e in edges:
    net.add_edge(e['data']['source'], e['data']['target'], value=e['data']['weight'])

options="""
{
  "nodes": {
    "font": {"size": 50, "face": "Arial", "align": "center"},
    "scaling": {"label": {"min": 30, "max": 80}}
  },
   "interaction": {
            "zoomView": true,
            "hover": true,
            "navigationButtons": true,
            "dragNodes": true,
            "dragView":true,
            "hideEdgesOnDrag": false
        },
  "physics": {
    "forceAtlas2Based": {
      "gravitationalConstant": -200,
      "centralGravity": 0.01,
      "springLength": 200,
      "springConstant": 0.04,
      "damping": 0.5
    },
     "minVelocity": 0.1,
    "solver": "forceAtlas2Based"
  }
}
"""

net.set_options(options)
save_path = os.path.join(os.getcwd(), "10.28.3interactive_network.html")
net.save_graph(save_path)
print("Saving to:", save_path)
