from __future__ import absolute_import

from .base import NetAddressFormField, MACAddressFormField
from ..lib.ipaddr import AddressType, NetworkType

__all__ = ('CidrAddressFormField', 'InetAddressFormField', \
        'MACAddressFormField')


class CidrAddressFormField(NetworkType, NetAddressFormField):
    pass


class InetAddressFormField(AddressType, NetAddressFormField):
    pass


class MACAddressFormField(MACAddressFormField):
    pass
