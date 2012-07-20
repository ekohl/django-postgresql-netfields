from __future__ import absolute_import

from ipaddr import (IPAddress, IPv4Address, IPv6Address, IPNetwork,
        IPv4Network, IPv6Network)

from . import PythonType

__all__ = ('AddressType', 'NetworkType')


class AddressType(PythonType):
    python_type = staticmethod(IPAddress)
    python_instances = (IPv4Address, IPv6Address)


class NetworkType(PythonType):
    python_type = staticmethod(IPNetwork)
    python_instances = (IPv4Network, IPv6Network)
