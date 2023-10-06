import requests


def send_post_data(
    *,
    data: str,
    host: str,
    port: int,
    method: str,
) -> None:
    """
    Send post request with message data to another service

    Parameters
    ----------
    data : str
        The string for delivery.
    host : str 
        The host address for connect 
    port: str 
        The port of server for connect
    method: str
        The server method
        
    Returns
    -------
    None

    Examples
    --------
    >>> send_post_data(data="DCJcPSyftN", host="127.0.0.1", port="5000", method="keep_data")
    """
    url = f"http://{host}:{port}/{method}"
    response = requests.post(url, data=data)

    # Check the response status code
    if response.status_code == 200:
        print("Data sent successfully.")
    else:
        print("Failed to send data. Status code:", response.status_code)