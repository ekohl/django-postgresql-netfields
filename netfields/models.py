from django.db.models import Model

from netfields import NetManager
from netfields.fields import IPy, ipaddr


class BaseTestModel(Model):
    objects = NetManager()

    class Meta:
        abstract = True


# IPy models

class IPyInetTestModel(BaseTestModel):
    field = IPy.InetAddressField()


class IPyNullInetTestModel(BaseTestModel):
    field = IPy.InetAddressField(null=True)


class IPyCidrTestModel(BaseTestModel):
    field = IPy.CidrAddressField()


class IPyNullCidrTestModel(BaseTestModel):
    field = IPy.CidrAddressField(null=True)


class IPyMACTestModel(BaseTestModel):
    mac = IPy.MACAddressField(null=True)


# ipaddr models

class IpaddrInetTestModel(BaseTestModel):
    field = ipaddr.InetAddressField()


class IpaddrNullInetTestModel(BaseTestModel):
    field = ipaddr.InetAddressField(null=True)


class IpaddrCidrTestModel(BaseTestModel):
    field = ipaddr.CidrAddressField()


class IpaddrNullCidrTestModel(BaseTestModel):
    field = ipaddr.CidrAddressField(null=True)


class IpaddrMACTestModel(BaseTestModel):
    mac = ipaddr.MACAddressField(null=True)
