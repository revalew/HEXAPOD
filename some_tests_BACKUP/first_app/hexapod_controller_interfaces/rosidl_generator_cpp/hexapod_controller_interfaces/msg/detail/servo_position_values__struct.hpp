// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from hexapod_controller_interfaces:msg/ServoPositionValues.idl
// generated code does not contain a copyright notice

#ifndef HEXAPOD_CONTROLLER_INTERFACES__MSG__DETAIL__SERVO_POSITION_VALUES__STRUCT_HPP_
#define HEXAPOD_CONTROLLER_INTERFACES__MSG__DETAIL__SERVO_POSITION_VALUES__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__hexapod_controller_interfaces__msg__ServoPositionValues __attribute__((deprecated))
#else
# define DEPRECATED__hexapod_controller_interfaces__msg__ServoPositionValues __declspec(deprecated)
#endif

namespace hexapod_controller_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ServoPositionValues_
{
  using Type = ServoPositionValues_<ContainerAllocator>;

  explicit ServoPositionValues_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::DEFAULTS_ONLY == _init)
    {
      std::fill<typename std::array<int16_t, 18>::iterator, int16_t>(this->id_pose.begin(), this->id_pose.end(), 512);
    } else if (rosidl_runtime_cpp::MessageInitialization::ZERO == _init) {
      std::fill<typename std::array<int16_t, 18>::iterator, int16_t>(this->id_pose.begin(), this->id_pose.end(), 0);
    }
  }

  explicit ServoPositionValues_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : id_pose(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::DEFAULTS_ONLY == _init)
    {
      std::fill<typename std::array<int16_t, 18>::iterator, int16_t>(this->id_pose.begin(), this->id_pose.end(), 512);
    } else if (rosidl_runtime_cpp::MessageInitialization::ZERO == _init) {
      std::fill<typename std::array<int16_t, 18>::iterator, int16_t>(this->id_pose.begin(), this->id_pose.end(), 0);
    }
  }

  // field types and members
  using _id_pose_type =
    std::array<int16_t, 18>;
  _id_pose_type id_pose;

  // setters for named parameter idiom
  Type & set__id_pose(
    const std::array<int16_t, 18> & _arg)
  {
    this->id_pose = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    hexapod_controller_interfaces::msg::ServoPositionValues_<ContainerAllocator> *;
  using ConstRawPtr =
    const hexapod_controller_interfaces::msg::ServoPositionValues_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<hexapod_controller_interfaces::msg::ServoPositionValues_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<hexapod_controller_interfaces::msg::ServoPositionValues_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      hexapod_controller_interfaces::msg::ServoPositionValues_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<hexapod_controller_interfaces::msg::ServoPositionValues_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      hexapod_controller_interfaces::msg::ServoPositionValues_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<hexapod_controller_interfaces::msg::ServoPositionValues_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<hexapod_controller_interfaces::msg::ServoPositionValues_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<hexapod_controller_interfaces::msg::ServoPositionValues_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__hexapod_controller_interfaces__msg__ServoPositionValues
    std::shared_ptr<hexapod_controller_interfaces::msg::ServoPositionValues_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__hexapod_controller_interfaces__msg__ServoPositionValues
    std::shared_ptr<hexapod_controller_interfaces::msg::ServoPositionValues_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ServoPositionValues_ & other) const
  {
    if (this->id_pose != other.id_pose) {
      return false;
    }
    return true;
  }
  bool operator!=(const ServoPositionValues_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ServoPositionValues_

// alias to use template instance with default allocator
using ServoPositionValues =
  hexapod_controller_interfaces::msg::ServoPositionValues_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace hexapod_controller_interfaces

#endif  // HEXAPOD_CONTROLLER_INTERFACES__MSG__DETAIL__SERVO_POSITION_VALUES__STRUCT_HPP_
