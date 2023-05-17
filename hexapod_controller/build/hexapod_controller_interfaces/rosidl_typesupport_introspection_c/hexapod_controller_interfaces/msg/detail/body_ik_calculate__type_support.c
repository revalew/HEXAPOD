// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from hexapod_controller_interfaces:msg/BodyIKCalculate.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "hexapod_controller_interfaces/msg/detail/body_ik_calculate__rosidl_typesupport_introspection_c.h"
#include "hexapod_controller_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "hexapod_controller_interfaces/msg/detail/body_ik_calculate__functions.h"
#include "hexapod_controller_interfaces/msg/detail/body_ik_calculate__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void hexapod_controller_interfaces__msg__BodyIKCalculate__rosidl_typesupport_introspection_c__BodyIKCalculate_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  hexapod_controller_interfaces__msg__BodyIKCalculate__init(message_memory);
}

void hexapod_controller_interfaces__msg__BodyIKCalculate__rosidl_typesupport_introspection_c__BodyIKCalculate_fini_function(void * message_memory)
{
  hexapod_controller_interfaces__msg__BodyIKCalculate__fini(message_memory);
}

size_t hexapod_controller_interfaces__msg__BodyIKCalculate__rosidl_typesupport_introspection_c__size_function__BodyIKCalculate__position_of_the_body(
  const void * untyped_member)
{
  (void)untyped_member;
  return 6;
}

const void * hexapod_controller_interfaces__msg__BodyIKCalculate__rosidl_typesupport_introspection_c__get_const_function__BodyIKCalculate__position_of_the_body(
  const void * untyped_member, size_t index)
{
  const int16_t * member =
    (const int16_t *)(untyped_member);
  return &member[index];
}

void * hexapod_controller_interfaces__msg__BodyIKCalculate__rosidl_typesupport_introspection_c__get_function__BodyIKCalculate__position_of_the_body(
  void * untyped_member, size_t index)
{
  int16_t * member =
    (int16_t *)(untyped_member);
  return &member[index];
}

void hexapod_controller_interfaces__msg__BodyIKCalculate__rosidl_typesupport_introspection_c__fetch_function__BodyIKCalculate__position_of_the_body(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const int16_t * item =
    ((const int16_t *)
    hexapod_controller_interfaces__msg__BodyIKCalculate__rosidl_typesupport_introspection_c__get_const_function__BodyIKCalculate__position_of_the_body(untyped_member, index));
  int16_t * value =
    (int16_t *)(untyped_value);
  *value = *item;
}

void hexapod_controller_interfaces__msg__BodyIKCalculate__rosidl_typesupport_introspection_c__assign_function__BodyIKCalculate__position_of_the_body(
  void * untyped_member, size_t index, const void * untyped_value)
{
  int16_t * item =
    ((int16_t *)
    hexapod_controller_interfaces__msg__BodyIKCalculate__rosidl_typesupport_introspection_c__get_function__BodyIKCalculate__position_of_the_body(untyped_member, index));
  const int16_t * value =
    (const int16_t *)(untyped_value);
  *item = *value;
}

static rosidl_typesupport_introspection_c__MessageMember hexapod_controller_interfaces__msg__BodyIKCalculate__rosidl_typesupport_introspection_c__BodyIKCalculate_message_member_array[1] = {
  {
    "position_of_the_body",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    6,  // array size
    false,  // is upper bound
    offsetof(hexapod_controller_interfaces__msg__BodyIKCalculate, position_of_the_body),  // bytes offset in struct
    NULL,  // default value
    hexapod_controller_interfaces__msg__BodyIKCalculate__rosidl_typesupport_introspection_c__size_function__BodyIKCalculate__position_of_the_body,  // size() function pointer
    hexapod_controller_interfaces__msg__BodyIKCalculate__rosidl_typesupport_introspection_c__get_const_function__BodyIKCalculate__position_of_the_body,  // get_const(index) function pointer
    hexapod_controller_interfaces__msg__BodyIKCalculate__rosidl_typesupport_introspection_c__get_function__BodyIKCalculate__position_of_the_body,  // get(index) function pointer
    hexapod_controller_interfaces__msg__BodyIKCalculate__rosidl_typesupport_introspection_c__fetch_function__BodyIKCalculate__position_of_the_body,  // fetch(index, &value) function pointer
    hexapod_controller_interfaces__msg__BodyIKCalculate__rosidl_typesupport_introspection_c__assign_function__BodyIKCalculate__position_of_the_body,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers hexapod_controller_interfaces__msg__BodyIKCalculate__rosidl_typesupport_introspection_c__BodyIKCalculate_message_members = {
  "hexapod_controller_interfaces__msg",  // message namespace
  "BodyIKCalculate",  // message name
  1,  // number of fields
  sizeof(hexapod_controller_interfaces__msg__BodyIKCalculate),
  hexapod_controller_interfaces__msg__BodyIKCalculate__rosidl_typesupport_introspection_c__BodyIKCalculate_message_member_array,  // message members
  hexapod_controller_interfaces__msg__BodyIKCalculate__rosidl_typesupport_introspection_c__BodyIKCalculate_init_function,  // function to initialize message memory (memory has to be allocated)
  hexapod_controller_interfaces__msg__BodyIKCalculate__rosidl_typesupport_introspection_c__BodyIKCalculate_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t hexapod_controller_interfaces__msg__BodyIKCalculate__rosidl_typesupport_introspection_c__BodyIKCalculate_message_type_support_handle = {
  0,
  &hexapod_controller_interfaces__msg__BodyIKCalculate__rosidl_typesupport_introspection_c__BodyIKCalculate_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_hexapod_controller_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, hexapod_controller_interfaces, msg, BodyIKCalculate)() {
  if (!hexapod_controller_interfaces__msg__BodyIKCalculate__rosidl_typesupport_introspection_c__BodyIKCalculate_message_type_support_handle.typesupport_identifier) {
    hexapod_controller_interfaces__msg__BodyIKCalculate__rosidl_typesupport_introspection_c__BodyIKCalculate_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &hexapod_controller_interfaces__msg__BodyIKCalculate__rosidl_typesupport_introspection_c__BodyIKCalculate_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
