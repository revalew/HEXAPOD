# generated from rosidl_generator_py/resource/_idl.py.em
# with input from hexapod_controller_interfaces:msg/ServoPositionValues.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

# Member 'id_pose'
import numpy  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_ServoPositionValues(type):
    """Metaclass of message 'ServoPositionValues'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('hexapod_controller_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'hexapod_controller_interfaces.msg.ServoPositionValues')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__servo_position_values
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__servo_position_values
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__servo_position_values
            cls._TYPE_SUPPORT = module.type_support_msg__msg__servo_position_values
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__servo_position_values

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'ID_POSE__DEFAULT': numpy.array((512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, ), dtype=numpy.int16),
        }

    @property
    def ID_POSE__DEFAULT(cls):
        """Return default value for message field 'id_pose'."""
        return numpy.array((512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, ), dtype=numpy.int16)


class ServoPositionValues(metaclass=Metaclass_ServoPositionValues):
    """Message class 'ServoPositionValues'."""

    __slots__ = [
        '_id_pose',
    ]

    _fields_and_field_types = {
        'id_pose': 'int16[18]',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('int16'), 18),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.id_pose = kwargs.get(
            'id_pose', ServoPositionValues.ID_POSE__DEFAULT)

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if all(self.id_pose != other.id_pose):
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def id_pose(self):
        """Message field 'id_pose'."""
        return self._id_pose

    @id_pose.setter
    def id_pose(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.int16, \
                "The 'id_pose' numpy.ndarray() must have the dtype of 'numpy.int16'"
            assert value.size == 18, \
                "The 'id_pose' numpy.ndarray() must have a size of 18"
            self._id_pose = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) == 18 and
                 all(isinstance(v, int) for v in value) and
                 all(val >= -32768 and val < 32768 for val in value)), \
                "The 'id_pose' field must be a set or sequence with length 18 and each value of type 'int' and each integer in [-32768, 32767]"
        self._id_pose = numpy.array(value, dtype=numpy.int16)
