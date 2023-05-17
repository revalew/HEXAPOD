// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from hexapod_controller_interfaces:msg/BodyIKCalculate.idl
// generated code does not contain a copyright notice

#ifndef HEXAPOD_CONTROLLER_INTERFACES__MSG__DETAIL__BODY_IK_CALCULATE__STRUCT_HPP_
#define HEXAPOD_CONTROLLER_INTERFACES__MSG__DETAIL__BODY_IK_CALCULATE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__hexapod_controller_interfaces__msg__BodyIKCalculate __attribute__((deprecated))
#else
# define DEPRECATED__hexapod_controller_interfaces__msg__BodyIKCalculate __declspec(deprecated)
#endif

namespace hexapod_controller_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct BodyIKCalculate_
{
  using Type = BodyIKCalculate_<ContainerAllocator>;

  explicit BodyIKCalculate_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::DEFAULTS_ONLY == _init)
    {
      std::fill<typename std::array<int16_t, 6>::iterator, int16_t>(this->position_of_the_body.begin(), this->position_of_the_body.end(), 0);
    } else if (rosidl_runtime_cpp::MessageInitialization::ZERO == _init) {
      std::fill<typename std::array<int16_t, 6>::iterator, int16_t>(this->position_of_the_body.begin(), this->position_of_the_body.end(), 0);
    }
  }

  explicit BodyIKCalculate_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : position_of_the_body(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::DEFAULTS_ONLY == _init)
    {
      std::fill<typename std::array<int16_t, 6>::iterator, int16_t>(this->position_of_the_body.begin(), this->position_of_the_body.end(), 0);
    } else if (rosidl_runtime_cpp::MessageInitialization::ZERO == _init) {
      std::fill<typename std::array<int16_t, 6>::iterator, int16_t>(this->position_of_the_body.begin(), this->position_of_the_body.end(), 0);
    }
  }

  // field types and members
  using _position_of_the_body_type =
    std::array<int16_t, 6>;
  _position_of_the_body_type position_of_the_body;

  // setters for named parameter idiom
  Type & set__position_of_the_body(
    const std::array<int16_t, 6> & _arg)
  {
    this->position_of_the_body = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    hexapod_controller_interfaces::msg::BodyIKCalculate_<ContainerAllocator> *;
  using ConstRawPtr =
    const hexapod_controller_interfaces::msg::BodyIKCalculate_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<hexapod_controller_interfaces::msg::BodyIKCalculate_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<hexapod_controller_interfaces::msg::BodyIKCalculate_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      hexapod_controller_interfaces::msg::BodyIKCalculate_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<hexapod_controller_interfaces::msg::BodyIKCalculate_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      hexapod_controller_interfaces::msg::BodyIKCalculate_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<hexapod_controller_interfaces::msg::BodyIKCalculate_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<hexapod_controller_interfaces::msg::BodyIKCalculate_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<hexapod_controller_interfaces::msg::BodyIKCalculate_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__hexapod_controller_interfaces__msg__BodyIKCalculate
    std::shared_ptr<hexapod_controller_interfaces::msg::BodyIKCalculate_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__hexapod_controller_interfaces__msg__BodyIKCalculate
    std::shared_ptr<hexapod_controller_interfaces::msg::BodyIKCalculate_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const BodyIKCalculate_ & other) const
  {
    if (this->position_of_the_body != other.position_of_the_body) {
      return false;
    }
    return true;
  }
  bool operator!=(const BodyIKCalculate_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct BodyIKCalculate_

// alias to use template instance with default allocator
using BodyIKCalculate =
  hexapod_controller_interfaces::msg::BodyIKCalculate_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace hexapod_controller_interfaces

#endif  // HEXAPOD_CONTROLLER_INTERFACES__MSG__DETAIL__BODY_IK_CALCULATE__STRUCT_HPP_
