# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: plp/proto/Classification.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='plp/proto/Classification.proto',
  package='plp.proto',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1eplp/proto/Classification.proto\x12\tplp.proto\"\x0f\n\rEmptyClassify\"1\n\x15\x43lassificationRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04text\x18\n \x01(\t\"l\n\x16\x43lassificationResponse\x12\x16\n\x0e\x63lassifierName\x18\x01 \x01(\t\x12\x16\n\x0e\x63lassification\x18\n \x01(\t\x12\x12\n\nconfidence\x18\x14 \x01(\x02\x12\x0e\n\x06\x65xtras\x18\x1e \x01(\t\"=\n\x12\x43lassifyPermission\x12\x12\n\npermission\x18( \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x32 \x01(\t\"P\n\x1a\x43lassifyPermissionResponse\x12\x32\n\x0bpermDetails\x18< \x03(\x0b\x32\x1d.plp.proto.ClassifyPermission2\xcb\x01\n\x15\x43lassificationService\x12U\n\x0c\x43lassifyText\x12 .plp.proto.ClassificationRequest\x1a!.plp.proto.ClassificationResponse\"\x00\x12[\n\x16getClassifyPermissions\x12\x18.plp.proto.EmptyClassify\x1a%.plp.proto.ClassifyPermissionResponse\"\x00\x62\x06proto3'
)




_EMPTYCLASSIFY = _descriptor.Descriptor(
  name='EmptyClassify',
  full_name='plp.proto.EmptyClassify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=60,
)


_CLASSIFICATIONREQUEST = _descriptor.Descriptor(
  name='ClassificationRequest',
  full_name='plp.proto.ClassificationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='plp.proto.ClassificationRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='plp.proto.ClassificationRequest.text', index=1,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=111,
)


_CLASSIFICATIONRESPONSE = _descriptor.Descriptor(
  name='ClassificationResponse',
  full_name='plp.proto.ClassificationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='classifierName', full_name='plp.proto.ClassificationResponse.classifierName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='classification', full_name='plp.proto.ClassificationResponse.classification', index=1,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='plp.proto.ClassificationResponse.confidence', index=2,
      number=20, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extras', full_name='plp.proto.ClassificationResponse.extras', index=3,
      number=30, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=221,
)


_CLASSIFYPERMISSION = _descriptor.Descriptor(
  name='ClassifyPermission',
  full_name='plp.proto.ClassifyPermission',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='permission', full_name='plp.proto.ClassifyPermission.permission', index=0,
      number=40, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='plp.proto.ClassifyPermission.description', index=1,
      number=50, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=223,
  serialized_end=284,
)


_CLASSIFYPERMISSIONRESPONSE = _descriptor.Descriptor(
  name='ClassifyPermissionResponse',
  full_name='plp.proto.ClassifyPermissionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='permDetails', full_name='plp.proto.ClassifyPermissionResponse.permDetails', index=0,
      number=60, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=286,
  serialized_end=366,
)

_CLASSIFYPERMISSIONRESPONSE.fields_by_name['permDetails'].message_type = _CLASSIFYPERMISSION
DESCRIPTOR.message_types_by_name['EmptyClassify'] = _EMPTYCLASSIFY
DESCRIPTOR.message_types_by_name['ClassificationRequest'] = _CLASSIFICATIONREQUEST
DESCRIPTOR.message_types_by_name['ClassificationResponse'] = _CLASSIFICATIONRESPONSE
DESCRIPTOR.message_types_by_name['ClassifyPermission'] = _CLASSIFYPERMISSION
DESCRIPTOR.message_types_by_name['ClassifyPermissionResponse'] = _CLASSIFYPERMISSIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EmptyClassify = _reflection.GeneratedProtocolMessageType('EmptyClassify', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYCLASSIFY,
  '__module__' : 'plp.proto.Classification_pb2'
  # @@protoc_insertion_point(class_scope:plp.proto.EmptyClassify)
  })
_sym_db.RegisterMessage(EmptyClassify)

ClassificationRequest = _reflection.GeneratedProtocolMessageType('ClassificationRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFICATIONREQUEST,
  '__module__' : 'plp.proto.Classification_pb2'
  # @@protoc_insertion_point(class_scope:plp.proto.ClassificationRequest)
  })
_sym_db.RegisterMessage(ClassificationRequest)

ClassificationResponse = _reflection.GeneratedProtocolMessageType('ClassificationResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFICATIONRESPONSE,
  '__module__' : 'plp.proto.Classification_pb2'
  # @@protoc_insertion_point(class_scope:plp.proto.ClassificationResponse)
  })
_sym_db.RegisterMessage(ClassificationResponse)

ClassifyPermission = _reflection.GeneratedProtocolMessageType('ClassifyPermission', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFYPERMISSION,
  '__module__' : 'plp.proto.Classification_pb2'
  # @@protoc_insertion_point(class_scope:plp.proto.ClassifyPermission)
  })
_sym_db.RegisterMessage(ClassifyPermission)

ClassifyPermissionResponse = _reflection.GeneratedProtocolMessageType('ClassifyPermissionResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFYPERMISSIONRESPONSE,
  '__module__' : 'plp.proto.Classification_pb2'
  # @@protoc_insertion_point(class_scope:plp.proto.ClassifyPermissionResponse)
  })
_sym_db.RegisterMessage(ClassifyPermissionResponse)



_CLASSIFICATIONSERVICE = _descriptor.ServiceDescriptor(
  name='ClassificationService',
  full_name='plp.proto.ClassificationService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=369,
  serialized_end=572,
  methods=[
  _descriptor.MethodDescriptor(
    name='ClassifyText',
    full_name='plp.proto.ClassificationService.ClassifyText',
    index=0,
    containing_service=None,
    input_type=_CLASSIFICATIONREQUEST,
    output_type=_CLASSIFICATIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getClassifyPermissions',
    full_name='plp.proto.ClassificationService.getClassifyPermissions',
    index=1,
    containing_service=None,
    input_type=_EMPTYCLASSIFY,
    output_type=_CLASSIFYPERMISSIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CLASSIFICATIONSERVICE)

DESCRIPTOR.services_by_name['ClassificationService'] = _CLASSIFICATIONSERVICE

# @@protoc_insertion_point(module_scope)
