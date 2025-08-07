from graphviz import Digraph

def generate_mind_map(topic, subtopics_dict):
    dot = Digraph(comment='Mind Map')
    dot.node('root', topic)

    def add_nodes(parent, children):
        for child, subchildren in children.items():
            dot.node(child, child)
            dot.edge(parent, child)
            if isinstance(subchildren, dict):
                add_nodes(child, subchildren)

    add_nodes('root', subtopics_dict)
    return dot

if __name__ == "__main__":
    # Example mind map data structure: nested dictionary
    mind_map_data = {
        "Python": {
            "Syntax": {},
            "Libraries": {
                "NumPy": {},
                "Pandas": {},
                "Matplotlib": {}
            },
            "Applications": {
                "Web": {},
                "Data Science": {},
                "Automation": {}
            }
        }
    }

    topic = "Programming Languages"
    dot = generate_mind_map(topic, mind_map_data)

    # Render and save to file
    dot.render('mind_map_output', view=True, format='png')

