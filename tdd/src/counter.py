from flask import Flask

# we need to import the file that contains the status codes
from src import status

app = Flask(__name__)

COUNTERS = {}


# We will use the app decorator and create a route called slash counters.
# specify the variable in route <name>
# let Flask know that the only methods that is allowed to be called
# on this function is "POST".
@app.route('/counters/<name>', methods=['POST'])
def create_counter(name):
    """Create a counter"""
    app.logger.info(f"Request to create counter: {name}")
    global COUNTERS

    if name in COUNTERS:
        return {"Message": f"Counter {name} already exists"}, status.HTTP_409_CONFLICT

    COUNTERS[name] = 0
    return {name: COUNTERS[name]}, status.HTTP_201_CREATED


# create a route for method PUT on endpoint /counters/<name>
# create a function to implement that route
@app.route('/counters/<name>', methods=['PUT'])
def update_counter(name):
    """ Update the counter by incrementing it by 1"""
    # increment the counter by 1
    global COUNTERS

    if name in COUNTERS:
        # update counter and return the counter
        COUNTERS[name] += 1
        app.logger.info(f"Updating counter {name} by 1 to a value of {COUNTERS[name]}")

        app.logger.info(f"Returning counter {name} with a value of {COUNTERS[name]}")
        return {name: COUNTERS[name]}, status.HTTP_200_OK

    # if no counter found
    return {"Message": f"Counter {name} does not exist"}, status.HTTP_404_NOT_FOUND


# create a route for method GET on endpoint /counters/<name>
# create a function to implement that route
@app.route('/counters/<name>', methods=['GET'])
def read_counter(name):
    """ Read and return the value of the counter"""
    global COUNTERS

    if name in COUNTERS:
        # return the value of the counter
        app.logger.info(f"Returning counter {name} with a value of {COUNTERS[name]}")
        return {name: COUNTERS[name]}, status.HTTP_200_OK

    # if no counter found
    return {"Message": f"Counter {name} does not exist"}, status.HTTP_404_NOT_FOUND

# create a route for method DELETE on endpoint /counters/<name>
# create a function to implement that route
@app.route('/counters/<name>', methods=['DELETE'])
def delete_counter(name):
    """ Delete a counter"""
    global COUNTERS

    if name in COUNTERS:
        # delete the counter
        app.logger.info(f"Deleting counter {name}")
        del COUNTERS[name]
        return status.HTTP_204_NO_CONTENT

    # if no counter found
    return {"Message": f"Counter {name} does not exist"}, status.HTTP_404_NOT_FOUND

