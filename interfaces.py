import json
from client import SSHClient

def show_ifaces_all(host: str, platform_id: str, credential_id: str, get_state: str = ""):
    """
    show_ifaces_all summary
        Logs into a network device and runs the command "show ip interface brief".  The command
        result is parsed using TextFSM, the device name found at the command prompt is added to
        the result and returned

    Args:
        host (str): The ip address or hostname of the device to connect to and run the command

        platform_id (str): The platform identifier for Netmiko.  Can be "cisco_ios", "cisco_nxos", etc.

        credential_id (str): The prefix identifier for the credentials to be uses in the user provided .env file.

        get_state (str, optional): get_state is a command modifier that will filter the command output
        to show only those interfaces in either an up or down state. Defaults to "". If no modification
        is provided, will run the default command "show ip interface brief"

    Returns:
        json: The result of the command in JSON format
    """

    if get_state == "up":
        cmd = "show ip interface brief | include up"
    elif get_state == "down":
        cmd = "show ip interface brief | include down"
    else:
        cmd = "show ip interface brief"

    # create a temporary, empty dictionary to be able to manipulate the data and results as needed
    temp = {}

    # create the SSH client.  This creates the dictionary that is needed for Netmiko to log into the device
    ssh_client = SSHClient(hostname=host, credential_id=credential_id, platform_id=platform_id)

    ssh_client.ssh_host_login()

    # add to the dictionary the hostname of the device
    temp["device name"] = ssh_client.device_hostname

    # add to the dictionary the result of the "show ip interface brief" command
    temp["interfaces"] = ssh_client.session.send_command(cmd, strip_command=True, strip_prompt=True, use_textfsm=True)

    return json.dumps(temp)


def show_iface_description(host: str, platform_id: str, credential_id: str, get_state: str = ""):
    """
    show_iface_description summary
        Logs into a network device and runs the command "show interface description".  The command
        result is parsed using TextFSM, the device name found at the command prompt is added to
        the result and returned

    Args:
        host (str): The ip address or hostname of the device to connect to and run the command

        platform_id (str): The platform identifier for Netmiko.  Can be "cisco_ios", "cisco_nxos", etc.

        credential_id (str): The prefix identifier for the credentials to be uses in the user provided .env file.

        get_state (str, optional): get_state is a command modifier that will filter the command output
        to show only those interfaces in either an up or down state. Defaults to "". If no modification
        is provided, will run the default command "show interface description"

    Returns:
        json: The result of the command in JSON format
    """

    if get_state == "up":
        cmd = "show interfaces description | include up"
    elif get_state == "down":
        cmd = "show interfaces description | include down"
    else:
        cmd = "show interfaces description"

    # create a temporary, empty dictionary to be able to manipulate the data and results as needed
    temp = {}

    # create the SSH client.  This creates the dictionary that is needed for Netmiko to log into the device
    ssh_client = SSHClient(hostname=host, credential_id=credential_id, platform_id=platform_id)

    ssh_client.ssh_host_login()

    # add to the dictionary the hostname of the device
    temp["device name"] = ssh_client.device_hostname

    # add to the dictionary the result of the "show interfaces description" command
    temp["interfaces"] = ssh_client.session.send_command(cmd, strip_command=True, strip_prompt=True, use_textfsm=True)

    return json.dumps(temp)