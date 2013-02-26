import json
from netifaces import ifaddresses
from sh import grep, netstat

# [bknittel] added function tok_replace

import uuid
import socket

def tok_replace(uri):
    result = ''
    while 1:
        left = uri.find('<')
        if left < 0: break
        right = uri.find('>')
        if right < left: break
        tok = uri[left+1:right]

	try:
	    if tok == 'hostname':
		tok = socket.gethostname()
	    elif tok == 'macaddr':
		tok = get_node_mac()
	    elif tok == 'ipaddr':
		tok = get_node_ip()
	    elif tok == 'lt':
		tok = '<'
	except:
	    tok = uri[left+1:right]

        result = result + uri[:left] + tok
        uri = uri[right+1:]

    return result+uri

def get_node_mac():
    try:
	return ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0,8*6,8)][::-1])
    except:
	pass

    return None

def get_node_ip():
    """Returns the node's IP, for the interface
    that is being used as the default gateway.
    This shuld work on both MacOS X and Linux."""

    try:
        default_interface = grep(netstat('-nr'), '-e', '^default', '-e' '^0.0.0.0').split()[-1]
        my_ip = ifaddresses(default_interface)[2][0]['addr']
        return my_ip
    except:
        pass

    return None


def handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        raise TypeError('Object of type %s with value of %s is not JSON serializable' % (type(obj), repr(obj)))


def json_dump(obj):
    return json.dumps(obj, default=handler)
