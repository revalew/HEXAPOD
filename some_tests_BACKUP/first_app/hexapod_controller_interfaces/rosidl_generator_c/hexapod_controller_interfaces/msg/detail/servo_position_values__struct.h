// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from hexapod_controller_interfaces:msg/ServoPositionValues.idl
// generated code does not contain a copyright notice

#ifndef HEXAPOD_CONTROLLER_INTERFACES__MSG__DETAIL__SERVO_POSITION_VALUES__STRUCT_H_
#define HEXAPOD_CONTROLLER_INTERFACES__MSG__DETAIL__SERVO_POSITION_VALUES__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/ServoPositionValues in the package hexapod_controller_interfaces.
/**
  * using an existing interface as part of the new custom one
  * geometry_msgs/Point coordinate 
 */
typedef struct hexapod_controller_interfaces__msg__ServoPositionValues
{
  /// SET THE DEFAULT VALUE FOR EACH SERVO AS 512 (DEAD CENTER)
  int16_t id_pose[18];
} hexapod_controller_interfaces__msg__ServoPositionValues;

// Struct for a sequence of hexapod_controller_interfaces__msg__ServoPositionValues.
typedef struct hexapod_controller_interfaces__msg__ServoPositionValues__Sequence
{
  hexapod_controller_interfaces__msg__ServoPositionValues * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} hexapod_controller_interfaces__msg__ServoPositionValues__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // HEXAPOD_CONTROLLER_INTERFACES__MSG__DETAIL__SERVO_POSITION_VALUES__STRUCT_H_
