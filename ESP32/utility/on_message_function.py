def on_message(topic, msg, pump):
    """
    Control the pump status based on the MQTT message.

    Args:
        topic (bytes): The topic that the message was published to.
        msg (bytes): The actual message payload.
        pump (object): A pump class to interface with the water pump.

    Returns:
        No return.
    """
    # Echo the topic and the msg data
    print((topic, msg))
    # Check the message and change the pump status
    if msg == b'open_valve':
        pump.open()
    elif msg == b'close_valve':
        pump.close()
