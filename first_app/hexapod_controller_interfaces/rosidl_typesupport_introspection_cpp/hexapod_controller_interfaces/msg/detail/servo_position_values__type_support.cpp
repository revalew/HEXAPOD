// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from hexapod_controller_interfaces:msg/ServoPositionValues.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "hexapod_controller_interfaces/msg/detail/servo_position_values__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace hexapod_controller_interfaces
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void ServoPositionValues_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) hexapod_controller_interfaces::msg::ServoPositionValues(_init);
}

void ServoPositionValues_fini_function(void * message_memory)
{
  auto typed_message = static_cast<hexapod_controller_interfaces::msg::ServoPositionValues *>(message_memory);
  typed_message->~ServoPositionValues();
}

size_t size_function__ServoPositionValues__id_pose(const void * untyped_member)
{
  (void)untyped_member;
  return 18;
}

const void * get_const_function__ServoPositionValues__id_pose(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::array<int16_t, 18> *>(untyped_member);
  return &member[index];
}

void * get_function__ServoPositionValues__id_pose(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::array<int16_t, 18> *>(untyped_member);
  return &member[index];
}

void fetch_function__ServoPositionValues__id_pose(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const int16_t *>(
    get_const_function__ServoPositionValues__id_pose(untyped_member, index));
  auto & value = *reinterpret_cast<int16_t *>(untyped_value);
  value = item;
}

void assign_function__ServoPositionValues__id_pose(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<int16_t *>(
    get_function__ServoPositionValues__id_pose(untyped_member, index));
  const auto & value = *reinterpret_cast<const int16_t *>(untyped_value);
  item = value;
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember ServoPositionValues_message_member_array[1] = {
  {
    "id_pose",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT16,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    18,  // array size
    false,  // is upper bound
    offsetof(hexapod_controller_interfaces::msg::ServoPositionValues, id_pose),  // bytes offset in struct
    nullptr,  // default value
    size_function__ServoPositionValues__id_pose,  // size() function pointer
    get_const_function__ServoPositionValues__id_pose,  // get_const(index) function pointer
    get_function__ServoPositionValues__id_pose,  // get(index) function pointer
    fetch_function__ServoPositionValues__id_pose,  // fetch(index, &value) function pointer
    assign_function__ServoPositionValues__id_pose,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers ServoPositionValues_message_members = {
  "hexapod_controller_interfaces::msg",  // message namespace
  "ServoPositionValues",  // message name
  1,  // number of fields
  sizeof(hexapod_controller_interfaces::msg::ServoPositionValues),
  ServoPositionValues_message_member_array,  // message members
  ServoPositionValues_init_function,  // function to initialize message memory (memory has to be allocated)
  ServoPositionValues_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t ServoPositionValues_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &ServoPositionValues_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace hexapod_controller_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<hexapod_controller_interfaces::msg::ServoPositionValues>()
{
  return &::hexapod_controller_interfaces::msg::rosidl_typesupport_introspection_cpp::ServoPositionValues_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, hexapod_controller_interfaces, msg, ServoPositionValues)() {
  return &::hexapod_controller_interfaces::msg::rosidl_typesupport_introspection_cpp::ServoPositionValues_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
