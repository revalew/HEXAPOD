// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from hexapod_controller_interfaces:msg/BodyIKCalculate.idl
// generated code does not contain a copyright notice

#ifndef HEXAPOD_CONTROLLER_INTERFACES__MSG__DETAIL__BODY_IK_CALCULATE__STRUCT_H_
#define HEXAPOD_CONTROLLER_INTERFACES__MSG__DETAIL__BODY_IK_CALCULATE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/BodyIKCalculate in the package hexapod_controller_interfaces.
/**
  * MESSAGE TO COMMUNICATE BETWEEN THE KEYBOARD AND BODY TO CALCLATE THE IK
 */
typedef struct hexapod_controller_interfaces__msg__BodyIKCalculate
{
  /// INITIALIZE ALL OF THE VALUES WITH 0
  /// int? zamiast uint? bedziemy przekazywac ujemne # FLAGA BLEDU
  int16_t position_of_the_body[6];
} hexapod_controller_interfaces__msg__BodyIKCalculate;

// Struct for a sequence of hexapod_controller_interfaces__msg__BodyIKCalculate.
typedef struct hexapod_controller_interfaces__msg__BodyIKCalculate__Sequence
{
  hexapod_controller_interfaces__msg__BodyIKCalculate * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} hexapod_controller_interfaces__msg__BodyIKCalculate__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // HEXAPOD_CONTROLLER_INTERFACES__MSG__DETAIL__BODY_IK_CALCULATE__STRUCT_H_
