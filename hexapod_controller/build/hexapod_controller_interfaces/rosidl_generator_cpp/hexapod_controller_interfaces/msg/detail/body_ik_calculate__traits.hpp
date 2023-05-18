// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from hexapod_controller_interfaces:msg/BodyIKCalculate.idl
// generated code does not contain a copyright notice

#ifndef HEXAPOD_CONTROLLER_INTERFACES__MSG__DETAIL__BODY_IK_CALCULATE__TRAITS_HPP_
#define HEXAPOD_CONTROLLER_INTERFACES__MSG__DETAIL__BODY_IK_CALCULATE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "hexapod_controller_interfaces/msg/detail/body_ik_calculate__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace hexapod_controller_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const BodyIKCalculate & msg,
  std::ostream & out)
{
  out << "{";
  // member: position_of_the_body
  {
    if (msg.position_of_the_body.size() == 0) {
      out << "position_of_the_body: []";
    } else {
      out << "position_of_the_body: [";
      size_t pending_items = msg.position_of_the_body.size();
      for (auto item : msg.position_of_the_body) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const BodyIKCalculate & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: position_of_the_body
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.position_of_the_body.size() == 0) {
      out << "position_of_the_body: []\n";
    } else {
      out << "position_of_the_body:\n";
      for (auto item : msg.position_of_the_body) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const BodyIKCalculate & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace hexapod_controller_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use hexapod_controller_interfaces::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const hexapod_controller_interfaces::msg::BodyIKCalculate & msg,
  std::ostream & out, size_t indentation = 0)
{
  hexapod_controller_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use hexapod_controller_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const hexapod_controller_interfaces::msg::BodyIKCalculate & msg)
{
  return hexapod_controller_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<hexapod_controller_interfaces::msg::BodyIKCalculate>()
{
  return "hexapod_controller_interfaces::msg::BodyIKCalculate";
}

template<>
inline const char * name<hexapod_controller_interfaces::msg::BodyIKCalculate>()
{
  return "hexapod_controller_interfaces/msg/BodyIKCalculate";
}

template<>
struct has_fixed_size<hexapod_controller_interfaces::msg::BodyIKCalculate>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<hexapod_controller_interfaces::msg::BodyIKCalculate>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<hexapod_controller_interfaces::msg::BodyIKCalculate>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // HEXAPOD_CONTROLLER_INTERFACES__MSG__DETAIL__BODY_IK_CALCULATE__TRAITS_HPP_
