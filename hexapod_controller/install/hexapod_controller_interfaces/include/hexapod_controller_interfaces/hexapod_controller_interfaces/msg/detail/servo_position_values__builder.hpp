// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from hexapod_controller_interfaces:msg/ServoPositionValues.idl
// generated code does not contain a copyright notice

#ifndef HEXAPOD_CONTROLLER_INTERFACES__MSG__DETAIL__SERVO_POSITION_VALUES__BUILDER_HPP_
#define HEXAPOD_CONTROLLER_INTERFACES__MSG__DETAIL__SERVO_POSITION_VALUES__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "hexapod_controller_interfaces/msg/detail/servo_position_values__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace hexapod_controller_interfaces
{

namespace msg
{

namespace builder
{

class Init_ServoPositionValues_id_pose
{
public:
  Init_ServoPositionValues_id_pose()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::hexapod_controller_interfaces::msg::ServoPositionValues id_pose(::hexapod_controller_interfaces::msg::ServoPositionValues::_id_pose_type arg)
  {
    msg_.id_pose = std::move(arg);
    return std::move(msg_);
  }

private:
  ::hexapod_controller_interfaces::msg::ServoPositionValues msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::hexapod_controller_interfaces::msg::ServoPositionValues>()
{
  return hexapod_controller_interfaces::msg::builder::Init_ServoPositionValues_id_pose();
}

}  // namespace hexapod_controller_interfaces

#endif  // HEXAPOD_CONTROLLER_INTERFACES__MSG__DETAIL__SERVO_POSITION_VALUES__BUILDER_HPP_
