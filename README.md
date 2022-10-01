# Cisco Commands

In other projects I have worked on I used Python [static methods](https://docs.python.org/3/library/functions.html#staticmethod) to run commands on Cisco network devices simply to eliminate the need to type out the command every time I needed to use it.  It worked very well at first.  Then I found I needed to work with various modifications of those commands to change the output, to add or remove certain elements of it, etc.

It became clear that the static methods had served me well starting out but that to do more I was going to have to get a little more involved.  I still wanted to keep things organized in such a way that I could just drop them into any project and just work without a great deal of configuration or setup. Using [Netmiko](https://pypi.org/project/netmiko/) and [dotenv](https://pypi.org/project/python-dotenv/) help make that possible.

Most of the commands provide the result you would expect of them but some of them take it a little further.  Mostly just piping the command to filter the results in some way whereas others may perform extra manipulation of the result.  The `routes.py` file is an example of this.

This is still very much in development as work continues to add other commands and to organize commands and results so that they can easily be integrated into other projects with little to no effort.