import colander

from ichnaea.api.schema import (
    InternalMappingSchema,
    InternalSchemaNode,
    InternalSequenceSchema,
)
from ichnaea.api.locate.schema import (
    BaseLocateSchema,
    FallbackSchema,
)


RADIO_STRINGS = ['gsm', 'cdma', 'umts', 'wcdma', 'lte']


class CellSchema(InternalMappingSchema):

    radio = InternalSchemaNode(
        colander.String(),
        validator=colander.OneOf(RADIO_STRINGS), missing=None)
    mcc = InternalSchemaNode(colander.Integer(), missing=None)
    mnc = InternalSchemaNode(colander.Integer(), missing=None)
    lac = InternalSchemaNode(colander.Integer(), missing=None)
    cid = InternalSchemaNode(colander.Integer(), missing=None)

    asu = InternalSchemaNode(colander.Integer(), missing=None)
    psc = InternalSchemaNode(colander.Integer(), missing=None)
    signal = InternalSchemaNode(colander.Integer(), missing=None)
    ta = InternalSchemaNode(colander.Integer(), missing=None)


class CellsSchema(InternalSequenceSchema):

    cell = CellSchema()


class WifiSchema(InternalMappingSchema):

    key = InternalSchemaNode(colander.String(), missing=None)
    frequency = InternalSchemaNode(colander.Integer(), missing=None)
    channel = InternalSchemaNode(colander.Integer(), missing=None)
    signal = InternalSchemaNode(colander.Integer(), missing=None)
    signalToNoiseRatio = InternalSchemaNode(
        colander.Integer(), missing=None, internal_name='snr')


class WifisSchema(InternalSequenceSchema):

    wifi = WifiSchema()


class LocateV1Schema(BaseLocateSchema):

    radio = InternalSchemaNode(
        colander.String(),
        validator=colander.OneOf(RADIO_STRINGS), missing=None)
    cell = CellsSchema(missing=())
    wifi = WifisSchema(missing=())
    fallbacks = FallbackSchema(missing=None)
