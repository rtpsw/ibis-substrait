"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...substrait import type_pb2 as substrait_dot_type__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%substrait/extensions/extensions.proto\x12\x14substrait.extensions\x1a\x14substrait/type.proto\x1a\x19google/protobuf/any.proto"X\n\x12SimpleExtensionURI\x120\n\x14extension_uri_anchor\x18\x01 \x01(\rR\x12extensionUriAnchor\x12\x10\n\x03uri\x18\x02 \x01(\tR\x03uri"\x8d\x0b\n\x1aSimpleExtensionDeclaration\x12g\n\x0eextension_type\x18\x01 \x01(\x0b2>.substrait.extensions.SimpleExtensionDeclaration.ExtensionTypeH\x00R\rextensionType\x12\x83\x01\n\x18extension_type_variation\x18\x02 \x01(\x0b2G.substrait.extensions.SimpleExtensionDeclaration.ExtensionTypeVariationH\x00R\x16extensionTypeVariation\x12s\n\x12extension_function\x18\x03 \x01(\x0b2B.substrait.extensions.SimpleExtensionDeclaration.ExtensionFunctionH\x00R\x11extensionFunction\x1a|\n\rExtensionType\x126\n\x17extension_uri_reference\x18\x01 \x01(\rR\x15extensionUriReference\x12\x1f\n\x0btype_anchor\x18\x02 \x01(\rR\ntypeAnchor\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x1a\x98\x01\n\x16ExtensionTypeVariation\x126\n\x17extension_uri_reference\x18\x01 \x01(\rR\x15extensionUriReference\x122\n\x15type_variation_anchor\x18\x02 \x01(\rR\x13typeVariationAnchor\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x1a\xe1\x05\n\x11ExtensionFunction\x126\n\x17extension_uri_reference\x18\x01 \x01(\rR\x15extensionUriReference\x12\'\n\x0ffunction_anchor\x18\x02 \x01(\rR\x0efunctionAnchor\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12h\n\x03udf\x18\x04 \x01(\x0b2V.substrait.extensions.SimpleExtensionDeclaration.ExtensionFunction.UserDefinedFunctionR\x03udf\x1a\xec\x03\n\x13UserDefinedFunction\x12\x12\n\x04code\x18\x01 \x01(\x0cR\x04code\x12\x18\n\x07summary\x18\x02 \x01(\tR\x07summary\x12 \n\x0bdescription\x18\x03 \x01(\tR\x0bdescription\x120\n\x0binput_types\x18\x04 \x03(\x0b2\x0f.substrait.TypeR\ninputTypes\x120\n\x0boutput_type\x18\x05 \x01(\x0b2\x0f.substrait.TypeR\noutputType\x12z\n\x06scalar\x18\x06 \x01(\x0b2`.substrait.extensions.SimpleExtensionDeclaration.ExtensionFunction.UserDefinedFunction.ScalarUDFH\x00R\x06scalar\x12}\n\x07tabular\x18\x07 \x01(\x0b2a.substrait.extensions.SimpleExtensionDeclaration.ExtensionFunction.UserDefinedFunction.TabularUDFH\x00R\x07tabular\x1a\x0b\n\tScalarUDF\x1a\x0c\n\nTabularUDFB\x0b\n\tfunc_typeB\x0e\n\x0cmapping_type"\x85\x01\n\x11AdvancedExtension\x128\n\x0coptimization\x18\x01 \x01(\x0b2\x14.google.protobuf.AnyR\x0coptimization\x126\n\x0benhancement\x18\x02 \x01(\x0b2\x14.google.protobuf.AnyR\x0benhancementB+\n\x12io.substrait.protoP\x01\xaa\x02\x12Substrait.Protobufb\x06proto3')
_SIMPLEEXTENSIONURI = DESCRIPTOR.message_types_by_name['SimpleExtensionURI']
_SIMPLEEXTENSIONDECLARATION = DESCRIPTOR.message_types_by_name['SimpleExtensionDeclaration']
_SIMPLEEXTENSIONDECLARATION_EXTENSIONTYPE = _SIMPLEEXTENSIONDECLARATION.nested_types_by_name['ExtensionType']
_SIMPLEEXTENSIONDECLARATION_EXTENSIONTYPEVARIATION = _SIMPLEEXTENSIONDECLARATION.nested_types_by_name['ExtensionTypeVariation']
_SIMPLEEXTENSIONDECLARATION_EXTENSIONFUNCTION = _SIMPLEEXTENSIONDECLARATION.nested_types_by_name['ExtensionFunction']
_SIMPLEEXTENSIONDECLARATION_EXTENSIONFUNCTION_USERDEFINEDFUNCTION = _SIMPLEEXTENSIONDECLARATION_EXTENSIONFUNCTION.nested_types_by_name['UserDefinedFunction']
_SIMPLEEXTENSIONDECLARATION_EXTENSIONFUNCTION_USERDEFINEDFUNCTION_SCALARUDF = _SIMPLEEXTENSIONDECLARATION_EXTENSIONFUNCTION_USERDEFINEDFUNCTION.nested_types_by_name['ScalarUDF']
_SIMPLEEXTENSIONDECLARATION_EXTENSIONFUNCTION_USERDEFINEDFUNCTION_TABULARUDF = _SIMPLEEXTENSIONDECLARATION_EXTENSIONFUNCTION_USERDEFINEDFUNCTION.nested_types_by_name['TabularUDF']
_ADVANCEDEXTENSION = DESCRIPTOR.message_types_by_name['AdvancedExtension']
SimpleExtensionURI = _reflection.GeneratedProtocolMessageType('SimpleExtensionURI', (_message.Message,), {'DESCRIPTOR': _SIMPLEEXTENSIONURI, '__module__': 'substrait.extensions.extensions_pb2'})
_sym_db.RegisterMessage(SimpleExtensionURI)
SimpleExtensionDeclaration = _reflection.GeneratedProtocolMessageType('SimpleExtensionDeclaration', (_message.Message,), {'ExtensionType': _reflection.GeneratedProtocolMessageType('ExtensionType', (_message.Message,), {'DESCRIPTOR': _SIMPLEEXTENSIONDECLARATION_EXTENSIONTYPE, '__module__': 'substrait.extensions.extensions_pb2'}), 'ExtensionTypeVariation': _reflection.GeneratedProtocolMessageType('ExtensionTypeVariation', (_message.Message,), {'DESCRIPTOR': _SIMPLEEXTENSIONDECLARATION_EXTENSIONTYPEVARIATION, '__module__': 'substrait.extensions.extensions_pb2'}), 'ExtensionFunction': _reflection.GeneratedProtocolMessageType('ExtensionFunction', (_message.Message,), {'UserDefinedFunction': _reflection.GeneratedProtocolMessageType('UserDefinedFunction', (_message.Message,), {'ScalarUDF': _reflection.GeneratedProtocolMessageType('ScalarUDF', (_message.Message,), {'DESCRIPTOR': _SIMPLEEXTENSIONDECLARATION_EXTENSIONFUNCTION_USERDEFINEDFUNCTION_SCALARUDF, '__module__': 'substrait.extensions.extensions_pb2'}), 'TabularUDF': _reflection.GeneratedProtocolMessageType('TabularUDF', (_message.Message,), {'DESCRIPTOR': _SIMPLEEXTENSIONDECLARATION_EXTENSIONFUNCTION_USERDEFINEDFUNCTION_TABULARUDF, '__module__': 'substrait.extensions.extensions_pb2'}), 'DESCRIPTOR': _SIMPLEEXTENSIONDECLARATION_EXTENSIONFUNCTION_USERDEFINEDFUNCTION, '__module__': 'substrait.extensions.extensions_pb2'}), 'DESCRIPTOR': _SIMPLEEXTENSIONDECLARATION_EXTENSIONFUNCTION, '__module__': 'substrait.extensions.extensions_pb2'}), 'DESCRIPTOR': _SIMPLEEXTENSIONDECLARATION, '__module__': 'substrait.extensions.extensions_pb2'})
_sym_db.RegisterMessage(SimpleExtensionDeclaration)
_sym_db.RegisterMessage(SimpleExtensionDeclaration.ExtensionType)
_sym_db.RegisterMessage(SimpleExtensionDeclaration.ExtensionTypeVariation)
_sym_db.RegisterMessage(SimpleExtensionDeclaration.ExtensionFunction)
_sym_db.RegisterMessage(SimpleExtensionDeclaration.ExtensionFunction.UserDefinedFunction)
_sym_db.RegisterMessage(SimpleExtensionDeclaration.ExtensionFunction.UserDefinedFunction.ScalarUDF)
_sym_db.RegisterMessage(SimpleExtensionDeclaration.ExtensionFunction.UserDefinedFunction.TabularUDF)
AdvancedExtension = _reflection.GeneratedProtocolMessageType('AdvancedExtension', (_message.Message,), {'DESCRIPTOR': _ADVANCEDEXTENSION, '__module__': 'substrait.extensions.extensions_pb2'})
_sym_db.RegisterMessage(AdvancedExtension)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x12io.substrait.protoP\x01\xaa\x02\x12Substrait.Protobuf'
    _SIMPLEEXTENSIONURI._serialized_start = 112
    _SIMPLEEXTENSIONURI._serialized_end = 200
    _SIMPLEEXTENSIONDECLARATION._serialized_start = 203
    _SIMPLEEXTENSIONDECLARATION._serialized_end = 1624
    _SIMPLEEXTENSIONDECLARATION_EXTENSIONTYPE._serialized_start = 589
    _SIMPLEEXTENSIONDECLARATION_EXTENSIONTYPE._serialized_end = 713
    _SIMPLEEXTENSIONDECLARATION_EXTENSIONTYPEVARIATION._serialized_start = 716
    _SIMPLEEXTENSIONDECLARATION_EXTENSIONTYPEVARIATION._serialized_end = 868
    _SIMPLEEXTENSIONDECLARATION_EXTENSIONFUNCTION._serialized_start = 871
    _SIMPLEEXTENSIONDECLARATION_EXTENSIONFUNCTION._serialized_end = 1608
    _SIMPLEEXTENSIONDECLARATION_EXTENSIONFUNCTION_USERDEFINEDFUNCTION._serialized_start = 1116
    _SIMPLEEXTENSIONDECLARATION_EXTENSIONFUNCTION_USERDEFINEDFUNCTION._serialized_end = 1608
    _SIMPLEEXTENSIONDECLARATION_EXTENSIONFUNCTION_USERDEFINEDFUNCTION_SCALARUDF._serialized_start = 1570
    _SIMPLEEXTENSIONDECLARATION_EXTENSIONFUNCTION_USERDEFINEDFUNCTION_SCALARUDF._serialized_end = 1581
    _SIMPLEEXTENSIONDECLARATION_EXTENSIONFUNCTION_USERDEFINEDFUNCTION_TABULARUDF._serialized_start = 1583
    _SIMPLEEXTENSIONDECLARATION_EXTENSIONFUNCTION_USERDEFINEDFUNCTION_TABULARUDF._serialized_end = 1595
    _ADVANCEDEXTENSION._serialized_start = 1627
    _ADVANCEDEXTENSION._serialized_end = 1760