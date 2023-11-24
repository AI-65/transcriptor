from graphviz import Digraph

def create_conversation_flowchart():
    # Create a Digraph object
    f = Digraph('Conversation Flowchart', filename='conversation_flowchart.gv')
    f.attr(rankdir='TB', size='8,5')

    # Add nodes
    f.attr('node', shape='rectangle')
    f.node('A', 'Initial Call from Service Provider\n(Gabor from Coban Bauservice GmbH)')
    f.node('B', "Client's Confusion\n(Mention of previous call)")
    f.node('C', "Client's Lack of Equipment\n(No need for internet or related technology)")
    f.node('D', 'Clarification Attempt by Gabor\n(Question about contract with Deutsche Glasfaser)')
    f.node('E', "Client's Concerns\n(Uncertainty about equipment installation)")
    f.node('F', "Service Provider's Response\n(Explanation of installation process)")
    f.node('G', "Client's Dismissal\n(Service deemed unnecessary)")
    f.node('H', 'Conclusion of the Call\n(Gabor acknowledges decision)')

    # Add edges
    f.edges(['AB', 'BC', 'CD', 'DE', 'EF', 'FG', 'GH'])

    # Render the graph to a file
    f.render('/mnt/data/conversation_flowchart')

    return f

# Create and render the flowchart
flowchart = create_conversation_flowchart()
flowchart

