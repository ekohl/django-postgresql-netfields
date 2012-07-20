from __future__ import absolute_import

from . import base
from ..lib.IPy import AddressType, NetworkType
from ..forms.IPy import (InetAddressFormField, CidrAddressFormField,
                             MACAddressFormField)

__all__ = ('InetAddressField', 'CidrAddressField', 'MACAddressField')


class CidrAddressField(NetworkType, base.CidrAddressField):
    form_class = CidrAddressFormField


class InetAddressField(AddressType, base.InetAddressField):
    form_class = InetAddressFormField


class MACAddressField(base.MACAddressField):
    form_class = MACAddressFormField
