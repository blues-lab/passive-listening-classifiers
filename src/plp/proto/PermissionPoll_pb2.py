# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PermissionPoll.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='PermissionPoll.proto',
  package='plp.proto',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14PermissionPoll.proto\x12\tplp.proto\"%\n\x15PermissionPollRequest\x12\x0c\n\x04type\x18\x01 \x01(\t\"E\n\x16PermissionPollResponse\x12\x10\n\x08template\x18\x01 \x01(\t\x12\x0c\n\x04slot\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t2p\n\x15PermissionPollService\x12W\n\x0ePermissionPoll\x12 .plp.proto.PermissionPollRequest\x1a!.plp.proto.PermissionPollResponse\"\x00\x62\x06proto3'
)




_PERMISSIONPOLLREQUEST = _descriptor.Descriptor(
  name='PermissionPollRequest',
  full_name='plp.proto.PermissionPollRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='plp.proto.PermissionPollRequest.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=35,
  serialized_end=72,
)


_PERMISSIONPOLLRESPONSE = _descriptor.Descriptor(
  name='PermissionPollResponse',
  full_name='plp.proto.PermissionPollResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='template', full_name='plp.proto.PermissionPollResponse.template', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='slot', full_name='plp.proto.PermissionPollResponse.slot', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='url', full_name='plp.proto.PermissionPollResponse.url', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=74,
  serialized_end=143,
)

DESCRIPTOR.message_types_by_name['PermissionPollRequest'] = _PERMISSIONPOLLREQUEST
DESCRIPTOR.message_types_by_name['PermissionPollResponse'] = _PERMISSIONPOLLRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PermissionPollRequest = _reflection.GeneratedProtocolMessageType('PermissionPollRequest', (_message.Message,), {
  'DESCRIPTOR' : _PERMISSIONPOLLREQUEST,
  '__module__' : 'PermissionPoll_pb2'
  # @@protoc_insertion_point(class_scope:plp.proto.PermissionPollRequest)
  })
_sym_db.RegisterMessage(PermissionPollRequest)

PermissionPollResponse = _reflection.GeneratedProtocolMessageType('PermissionPollResponse', (_message.Message,), {
  'DESCRIPTOR' : _PERMISSIONPOLLRESPONSE,
  '__module__' : 'PermissionPoll_pb2'
  # @@protoc_insertion_point(class_scope:plp.proto.PermissionPollResponse)
  })
_sym_db.RegisterMessage(PermissionPollResponse)



_PERMISSIONPOLLSERVICE = _descriptor.ServiceDescriptor(
  name='PermissionPollService',
  full_name='plp.proto.PermissionPollService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=145,
  serialized_end=257,
  methods=[
  _descriptor.MethodDescriptor(
    name='PermissionPoll',
    full_name='plp.proto.PermissionPollService.PermissionPoll',
    index=0,
    containing_service=None,
    input_type=_PERMISSIONPOLLREQUEST,
    output_type=_PERMISSIONPOLLRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PERMISSIONPOLLSERVICE)

DESCRIPTOR.services_by_name['PermissionPollService'] = _PERMISSIONPOLLSERVICE

# @@protoc_insertion_point(module_scope)
