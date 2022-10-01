
import json
from client import SSHClient

def show_route(host: str, platform_id: str, credential_id: str):
    """
    show_route summary
        Logs into a network device and runs the command "show ip route".  The results are parsed using TextFSM
        templates and then further processed to give each route it is own number.  The intention being that
        when referencing the output between others, a common reference can be made

    Args:
        host (str): The ip address or hostname of the device to connect to and run the command
        platform_id (str): The platform identifier for Netmiko.  Can be "cisco_ios", "cisco_nxos", etc.
        credential_id (str): The prefix identifier for the credentials to be uses in the user provided .env file.

    Returns:
        json: The result of the show ip route command in JSON format
    """

    temp = {}

    ssh_client = SSHClient(hostname=host, credential_id=credential_id, platform_id=platform_id)

    ssh_client.ssh_host_login()
    device_name = ssh_client.device_hostname
    result = ssh_client.session.send_command("show ip route", strip_command=True, strip_prompt=True, use_textfsm=True)

    temp["device"] = device_name
    temp["total routes"] = len(result)
    temp["routing table"] = {}

    for num, route in enumerate(result):
        temp["routing table"].update({
            f"{num + 1:03d}": {k:v for k, v in route.items()}
        })

    return json.dumps(temp)

def show_route_minified(host: str, platform_id: str, credential_id: str):
    """
    show_route_minified summary
        Logs into a network device and runs the command "show ip route".  For NXOS based devices it will remove
        some values that are commonly empty to reduce the clutter.  As well, for NXOS and IOS platforms, the 
        uptime value is removed.  Each of the routes is processed after parsing to give each a number for ease of
        reference when reviewing or sharing the output.

        If any of the removed values are needed, use the "show_route" function.

    Args:
        host (str): The ip address or hostname of the device to connect to and run the command
        platform_id (str): The platform identifier for Netmiko.  Can be "cisco_ios", "cisco_nxos", etc.
        credential_id (str): The prefix identifier for the credentials to be uses in the user provided .env file.

    Returns:
        json: The result of the show ip route command in JSON format
    """

    temp = {}

    ssh_client = SSHClient(hostname=host, credential_id=credential_id, platform_id=platform_id)

    ssh_client.ssh_host_login()
    device_name = ssh_client.device_hostname
    result = ssh_client.session.send_command("show ip route", strip_command=True, strip_prompt=True, use_textfsm=True)

    if platform_id == "cisco_nxos":

        for route in result:
            del route["encap"]
            del route["tunnelid"]
            del route["segid"]
            del route["tag"]
            del route["uptime"]

    if platform_id == "cisco_ios":
        for route in result:
            del route["uptime"]

    temp["device"] = device_name
    temp["total routes"] = len(result)
    temp["routing table"] = {}

    for num, route in enumerate(result):
        temp["routing table"].update({
            f"{num + 1:03d}": {k:v for k, v in route.items()}
        })

    return json.dumps(temp)