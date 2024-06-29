""" HTTP client to send POST requests to the Flask server """
import urequests
import ujson


def send_data(url, data):
    """
        Send data to the flask Api.

        Args:
            url(string): Un end point of the falsk api.
            data(json): A json object store all the new data.

        Returns:
            response(object): Un urequests object handel server response.
    """
    # Set the reqeust header
    headers = {'Content-Type': 'application/json'}
    # Get the server response
    response = urequests.post(url, data=ujson.dumps(data), headers=headers)
    return (response)
