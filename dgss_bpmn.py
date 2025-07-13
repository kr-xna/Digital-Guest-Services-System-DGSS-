from graphviz import Digraph
from IPython.display import Image

# Initialize the BPMN diagram
dot = Digraph(comment='Digital Guest Services System (DGSS)', format='png')

# Guest pool
with dot.subgraph(name='cluster_guest') as guest:
    guest.attr(label='Guest')
    guest.node('Start', 'Guest Initiates Service Request', shape='circle')
    guest.node('A', 'Select Service (In-room Dining or Laundry)')
    guest.node('Gateway', 'Decision: Select In-room Dining or Laundry', shape='diamond')
    guest.node('B', 'Place Order')
    guest.node('C', 'Track Request Status')
    guest.node('D', 'Provide Feedback')
    guest.node('End', 'Service Completed', shape='circle')

# Kitchen staff pool
with dot.subgraph(name='cluster_kitchen') as kitchen:
    kitchen.attr(label='Kitchen Staff')
    kitchen.node('E', 'Receive Order')
    kitchen.node('F', 'Prepare Food')
    kitchen.node('G', 'Send Status Update')

# Housekeeping staff pool
with dot.subgraph(name='cluster_housekeeping') as housekeeping:
    housekeeping.attr(label='Housekeeping Staff')
    housekeeping.node('H', 'Receive Laundry Request')
    housekeeping.node('I', 'Collect Laundry')
    housekeeping.node('J', 'Send Status Update')

# Green Points System pool
with dot.subgraph(name='cluster_green') as green:
    green.attr(label='Green Points System')
    green.node('K', 'Track Eco-Friendly Choices')
    green.node('L', 'Update Points Balance')

# Sequential flows
dot.edges([('Start', 'A'), ('A', 'Gateway'), ('Gateway', 'B'), ('B', 'C'),
           ('C', 'D'), ('D', 'End')])

dot.edges([('B', 'E'), ('E', 'F'), ('F', 'G'), ('G', 'C')])
dot.edges([('Gateway', 'H'), ('H', 'I'), ('I', 'J'), ('J', 'C')])
dot.edges([('D', 'K'), ('K', 'L')])

# Message flows
dot.edge('B', 'E', style='dashed', label='Message: Order Sent to Kitchen')
dot.edge('Gateway', 'H', style='dashed', label='Message: Laundry Request Sent to Housekeeping')
dot.edge('D', 'K', style='dashed', label='Message: Feedback Sent to Green Points')

# Render and display
output_path = 'dgss_bpmn_diagram'
dot.render(output_path, cleanup=True)

# Optional: display in Jupyter
Image(output_path + '.png')
