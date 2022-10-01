import json
from client import SSHClient

def show_vlans(host: str, platform_id: str, credential_id: str):
    """
    show_vlans summary
        Logs into a network device and runs the command "show vlan".  The command
        result is parsed using TextFSM, the device name found at the command prompt is added to
        the result and returned

    Args:
        host (str): The ip address or hostname of the device to connect to and run the command

        platform_id (str): The platform identifier for Netmiko.  Can be "cisco_ios", "cisco_nxos", etc.

        credential_id (str): The prefix identifier for the credentials to be uses in the user provided .env file.

    Returns:
        json: The result of the command in JSON format
    """

    # create a temporary, empty dictionary to be able to manipulate the data and results as needed
    temp = {}

    # create the SSH client.  This creates the dictionary that is needed for Netmiko to log into the device
    ssh_client = SSHClient(hostname=host, credential_id=credential_id, platform_id=platform_id)

    ssh_client.ssh_host_login()

    # add to the dictionary the hostname of the device
    temp["device name"] = ssh_client.device_hostname

    # add to the dictionary the result of the "show vlan" command
    temp["vlans"] = ssh_client.session.send_command("show vlan", strip_command=True, strip_prompt=True, use_textfsm=True)

    return json.dumps(temp)