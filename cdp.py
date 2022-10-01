
import json
from client import SSHClient

def show_cdp_neighbors(host: str, platform_id: str, credential_id: str, get_details: bool = False):
    """
    show_neighbors summary
        Logs into a network device and runs the command "show cdp neighbors".  If the "get_details" argument
        is set to True, then the command "show cdp neighbors detail" is run.  The results are parsed using
        TextFSM templates and further processed for easier readability and organization by giving each 
        neighbor a number for ease of reference to the output between others.

    Args:
        host (str): The ip address or hostname of the device to connect to and run the command
        platform_id (str): The platform identifier for Netmiko.  Can be "cisco_ios", "cisco_nxos", etc.
        credential_id (str): The prefix identifier for the credentials to be uses in the user provided .env file.
        get_details (bool, optional): Whether or not to run "show cdp neighbor details". Defaults to False.

    Returns:
        json: The result of the show cdp neighbor command in JSON format
    """

    # If "get_details" is set to True then run the neighbors detail command otherwise just show cdp neighbors
    if get_details:
        cmd = "show cdp neighbors detail"
    else:
        cmd = "show cdp neighbors"

    # create a temporary, empty dictionary to be able to manipulate the data and results as needed
    temp = {}

    # create the SSH client.  This creates the dictionary that is needed for Netmiko to log into the device
    ssh_client = SSHClient(hostname=host, credential_id=credential_id, platform_id=platform_id)

    ssh_client.ssh_host_login()

    # Get the device name as it is displayed from the command line
    device_name = ssh_client.device_hostname

    # run the command and format it with the appropriate TextFSM template
    result = ssh_client.session.send_command(cmd, strip_command=True, strip_prompt=True, use_textfsm=True)

    # start forming the dictionary to hold some extra information captured from the device and command result
    temp["device"] = device_name
    temp["total neighbors"] = len(result)
    temp["cdp neighbors"] = {}

    # loop over the result of the command output and add a number to the entry to help better identify
    # each neighbor.  Not strictly necessary but it makes the output a python dictionary rather than a list
    # of dictionaries and satisfies the unique key requirment
    for num, neighbors in enumerate(result):
        temp["cdp neighbors"].update({
            f"{num + 1:03d}": {k:v for k, v in neighbors.items()}
        })

    # convert the dictionary to a JSON object and return that back to the caller
    return json.dumps(temp)