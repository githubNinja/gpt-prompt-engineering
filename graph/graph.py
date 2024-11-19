import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

# Sample data structure
data = pd.DataFrame({
    'CustomerID': ['C1', 'C1', 'C2', 'C2', 'C3'],
    'ChatID': ['CH1', None, 'CH2', 'CH3', None],
    'CallID': ['CL1', 'CL2', 'CL3', 'CL4', 'CL5'],
    'SurveyID': [None, 'S1', 'S2', None, 'S3'],
    'CallDuration': [5, 3, 7, 2, 6],
    'StartTime': ['2024-11-01 09:00', '2024-11-01 10:30', '2024-11-01 11:00', '2024-11-01 14:00', '2024-11-01 16:00'],
    'EndTime': ['2024-11-01 09:05', '2024-11-01 10:33', '2024-11-01 11:07', '2024-11-01 14:02', '2024-11-01 16:06']
})

# Initialize graph
G = nx.Graph()

# Add nodes and edges to the graph
for _, row in data.iterrows():
    customer_id = row['CustomerID']
    G.add_node(customer_id, type='customer')

    if pd.notna(row['ChatID']):
        G.add_node(row['ChatID'], type='chat')
        G.add_edge(customer_id, row['ChatID'], interaction_type='chat')

    if pd.notna(row['CallID']):
        G.add_node(row['CallID'], type='call', duration=row['CallDuration'],
                   start=row['StartTime'], end=row['EndTime'])
        G.add_edge(customer_id, row['CallID'], interaction_type='call')

    if pd.notna(row['SurveyID']):
        G.add_node(row['SurveyID'], type='survey')
        G.add_edge(customer_id, row['SurveyID'], interaction_type='survey')

# Choose a specific customer for visualization
selected_customer = 'C1'
subgraph = G.subgraph(nx.node_connected_component(G, selected_customer))

# Visualize the graph
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(subgraph)
nx.draw(subgraph, pos, with_labels=True, node_size=3000, font_size=10, node_color='lightblue')
nx.draw_networkx_edge_labels(subgraph, pos, edge_labels=nx.get_edge_attributes(subgraph, 'interaction_type'))
plt.title(f"Graph View for Customer {selected_customer}")
plt.show()
