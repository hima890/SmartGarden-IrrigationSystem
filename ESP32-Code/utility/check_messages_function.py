"""Function to check for control messages"""
def check_messages(client):
    """
    Check for control messages from the MQTT client.

    Args:
        client: The MQTT client instance used to check for messages.

    Returns:
        None

    Example:
        # Assuming `client` is a properly configured MQTT client instance
        check_messages(client)

    Raises:
        Exception: If there is an error while checking for messages.
    """
    try:
        client.check_msg()
    except Exception as e:
        print(f"Failed to check messages: {e}")
