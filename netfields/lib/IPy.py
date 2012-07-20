from __future__ import absolute_import

from IPy import IP

from . import PythonType

__all__ = ('AddressType', 'NetworkType')


class AddressType(PythonType):
    python_type = staticmethod(IP)
    python_instances = (IP,)


NetworkType = AddressType
