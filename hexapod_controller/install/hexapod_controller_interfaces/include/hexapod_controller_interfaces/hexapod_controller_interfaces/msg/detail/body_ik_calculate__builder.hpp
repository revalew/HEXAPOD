// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from hexapod_controller_interfaces:msg/BodyIKCalculate.idl
// generated code does not contain a copyright notice

#ifndef HEXAPOD_CONTROLLER_INTERFACES__MSG__DETAIL__BODY_IK_CALCULATE__BUILDER_HPP_
#define HEXAPOD_CONTROLLER_INTERFACES__MSG__DETAIL__BODY_IK_CALCULATE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "hexapod_controller_interfaces/msg/detail/body_ik_calculate__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace hexapod_controller_interfaces
{

namespace msg
{

namespace builder
{

class Init_BodyIKCalculate_position_of_the_body
{
public:
  Init_BodyIKCalculate_position_of_the_body()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::hexapod_controller_interfaces::msg::BodyIKCalculate position_of_the_body(::hexapod_controller_interfaces::msg::BodyIKCalculate::_position_of_the_body_type arg)
  {
    msg_.position_of_the_body = std::move(arg);
    return std::move(msg_);
  }

private:
  ::hexapod_controller_interfaces::msg::BodyIKCalculate msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::hexapod_controller_interfaces::msg::BodyIKCalculate>()
{
  return hexapod_controller_interfaces::msg::builder::Init_BodyIKCalculate_position_of_the_body();
}

}  // namespace hexapod_controller_interfaces

#endif  // HEXAPOD_CONTROLLER_INTERFACES__MSG__DETAIL__BODY_IK_CALCULATE__BUILDER_HPP_
