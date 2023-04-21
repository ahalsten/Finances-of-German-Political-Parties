#################################
# SI507: Final Project
# Winter 2023
# Anna Halstenbach
# uniqname: ahalsten
# The Program
#################################


from flask import Flask, render_template, send_file, request
from flask_caching import Cache
import networkx as nx
from io import BytesIO
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from read_json_ahalsten import G 

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple', 'CACHE_DEFAULT_TIMEOUT': 3600}) # Cache the image data for 1 hour

def generate_graph_image():
    """ Load the graph data from read_json_ahalsten module. Draws a
    plot and saves the graph as a PNG image in memory. Returns the image
    data as bytes.

    Parameters:
        None

    Returns:
        bytes: the image data as bytes
     """
    nx.draw_networkx(G, with_labels = True, font_size=4)
    buf = BytesIO()
    plt.savefig(buf, format='png', dpi=199)
    buf.seek(0)
    return buf.getvalue() 

@app.route('/')
def index():
    """ For index, we just welcome the user of the program.
    <h1> tag to make the font larger

    Parameters:
        None

    Returns:
        str: Welcome to the networks of German political parties and sponsors! 
     """
    return "<h1>Welcome to the networks of German political parties and sponsors!</h1>"

@app.route('/graph.png')
@cache.cached() # Cache the image data returned by this route for the configured time period
def graph():
    image_data = generate_graph_image() # Generate the image data
    # Serve the image data using Flask's send_file function
    return send_file(BytesIO(image_data), mimetype='image/png')

@app.route('/commonsponsors')
def print_common_sponsors():
    """ Get the precedessors of the SPD node and the predecessors of the Greens node.
    Then Finds the intersection of the two sets to get the nodes that have edges with 
    both nodes. Prints them in alphabetical order.

    Parameters:
        None

    Returns:
        the webpage (html)
     """
    predecessors_spd = set(G.predecessors('SPD'))
    predecessors_greens = set(G.predecessors('Greens'))
    connected_nodes = sorted(list(predecessors_spd.intersection(predecessors_greens)))
    return render_template('commonsponsors.html', connected_nodes=connected_nodes)

@app.route('/total')
def print_total_amount():
    """ Display the total amount of sponsorship (weight of all edges)
    from 2019 through 2022.

    Parameters:
        None

    Returns:
        the webpage (html)
     """
    total_weight = sum([G[u][v][key]['weight'] for u, v, key in G.edges(keys=True)])
    return render_template('total.html', total_weight=total_weight)

# This one is a potential fifth presentation, but it is a bit boring.
# @app.route('/topsponsors/')
# def print_top_sponsors():
#     """ Display the sponsors with the highest out degree, i.e.
#     the sponsors that consistently sponsored both parties (max 8
#     because 4 years x 2 parties). 

#     Parameters:
#         None

#     Returns:
#         the webpage (html)
#      """
#     out_degrees = [(node, G.out_degree(node)) for node in G.nodes()]

#     # find the node(s) with the highest out degree
#     max_out_degree = max(out_degrees, key=lambda x: x[1])[1]
#     highest_out_degree_nodes = [node for node, out_degree in out_degrees if out_degree == max_out_degree]
#     return render_template('topsponsors.html', highest_out_degree_nodes=highest_out_degree_nodes)

@app.route('/topsponsors', methods=['GET', 'POST'])
def top_nodes():
    if request.method == 'POST':
        # Get the number inputted by the user
        num_nodes = int(request.form['num_nodes'])
        
        # Find the top nodes with the highest out-degree
        nodes = sorted(G.nodes(), key=lambda x: G.out_degree(x), reverse=True)[:num_nodes]
        
        # Return the top nodes as a string
        return "The top {} sponsors with the most consistent sponsorship behavior to both parties throughout the observed years (the highest out-degree) are: {}".format(num_nodes, nodes)
    else:
        # Render the form for the user to input a number
        return '''
            <form method="post">
                <label for="num_nodes">In the following, a list of sponsors that most consistently sponsored party events of the SPD and the Greens will appear (no matter the amount they gave). From the top of this list, how many of the top consistent sponsors would you like to see? Enter a number :</label>
                <input type="number" id="num_nodes" name="num_nodes" min="1" max="100">
                <input type="submit" value="Submit">
            </form>
        '''

# Runs the application on a local development server. Returns None.
# Launch the Flask dev server.
# Once the Flask server is running, use browser to navigate to the following URL:
# http://localhost:5000/

app.run(host='localhost')