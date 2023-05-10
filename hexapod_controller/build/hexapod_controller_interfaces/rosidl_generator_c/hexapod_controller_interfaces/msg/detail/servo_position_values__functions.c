// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from hexapod_controller_interfaces:msg/ServoPositionValues.idl
// generated code does not contain a copyright notice
#include "hexapod_controller_interfaces/msg/detail/servo_position_values__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
hexapod_controller_interfaces__msg__ServoPositionValues__init(hexapod_controller_interfaces__msg__ServoPositionValues * msg)
{
  if (!msg) {
    return false;
  }
  // id_pose
  msg->id_pose[0] = 512;
  msg->id_pose[1] = 512;
  msg->id_pose[2] = 512;
  msg->id_pose[3] = 512;
  msg->id_pose[4] = 512;
  msg->id_pose[5] = 512;
  msg->id_pose[6] = 512;
  msg->id_pose[7] = 512;
  msg->id_pose[8] = 512;
  msg->id_pose[9] = 512;
  msg->id_pose[10] = 512;
  msg->id_pose[11] = 512;
  msg->id_pose[12] = 512;
  msg->id_pose[13] = 512;
  msg->id_pose[14] = 512;
  msg->id_pose[15] = 512;
  msg->id_pose[16] = 512;
  msg->id_pose[17] = 512;
  return true;
}

void
hexapod_controller_interfaces__msg__ServoPositionValues__fini(hexapod_controller_interfaces__msg__ServoPositionValues * msg)
{
  if (!msg) {
    return;
  }
  // id_pose
}

bool
hexapod_controller_interfaces__msg__ServoPositionValues__are_equal(const hexapod_controller_interfaces__msg__ServoPositionValues * lhs, const hexapod_controller_interfaces__msg__ServoPositionValues * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // id_pose
  for (size_t i = 0; i < 18; ++i) {
    if (lhs->id_pose[i] != rhs->id_pose[i]) {
      return false;
    }
  }
  return true;
}

bool
hexapod_controller_interfaces__msg__ServoPositionValues__copy(
  const hexapod_controller_interfaces__msg__ServoPositionValues * input,
  hexapod_controller_interfaces__msg__ServoPositionValues * output)
{
  if (!input || !output) {
    return false;
  }
  // id_pose
  for (size_t i = 0; i < 18; ++i) {
    output->id_pose[i] = input->id_pose[i];
  }
  return true;
}

hexapod_controller_interfaces__msg__ServoPositionValues *
hexapod_controller_interfaces__msg__ServoPositionValues__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  hexapod_controller_interfaces__msg__ServoPositionValues * msg = (hexapod_controller_interfaces__msg__ServoPositionValues *)allocator.allocate(sizeof(hexapod_controller_interfaces__msg__ServoPositionValues), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(hexapod_controller_interfaces__msg__ServoPositionValues));
  bool success = hexapod_controller_interfaces__msg__ServoPositionValues__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
hexapod_controller_interfaces__msg__ServoPositionValues__destroy(hexapod_controller_interfaces__msg__ServoPositionValues * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    hexapod_controller_interfaces__msg__ServoPositionValues__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
hexapod_controller_interfaces__msg__ServoPositionValues__Sequence__init(hexapod_controller_interfaces__msg__ServoPositionValues__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  hexapod_controller_interfaces__msg__ServoPositionValues * data = NULL;

  if (size) {
    data = (hexapod_controller_interfaces__msg__ServoPositionValues *)allocator.zero_allocate(size, sizeof(hexapod_controller_interfaces__msg__ServoPositionValues), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = hexapod_controller_interfaces__msg__ServoPositionValues__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        hexapod_controller_interfaces__msg__ServoPositionValues__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
hexapod_controller_interfaces__msg__ServoPositionValues__Sequence__fini(hexapod_controller_interfaces__msg__ServoPositionValues__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      hexapod_controller_interfaces__msg__ServoPositionValues__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

hexapod_controller_interfaces__msg__ServoPositionValues__Sequence *
hexapod_controller_interfaces__msg__ServoPositionValues__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  hexapod_controller_interfaces__msg__ServoPositionValues__Sequence * array = (hexapod_controller_interfaces__msg__ServoPositionValues__Sequence *)allocator.allocate(sizeof(hexapod_controller_interfaces__msg__ServoPositionValues__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = hexapod_controller_interfaces__msg__ServoPositionValues__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
hexapod_controller_interfaces__msg__ServoPositionValues__Sequence__destroy(hexapod_controller_interfaces__msg__ServoPositionValues__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    hexapod_controller_interfaces__msg__ServoPositionValues__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
hexapod_controller_interfaces__msg__ServoPositionValues__Sequence__are_equal(const hexapod_controller_interfaces__msg__ServoPositionValues__Sequence * lhs, const hexapod_controller_interfaces__msg__ServoPositionValues__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!hexapod_controller_interfaces__msg__ServoPositionValues__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
hexapod_controller_interfaces__msg__ServoPositionValues__Sequence__copy(
  const hexapod_controller_interfaces__msg__ServoPositionValues__Sequence * input,
  hexapod_controller_interfaces__msg__ServoPositionValues__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(hexapod_controller_interfaces__msg__ServoPositionValues);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    hexapod_controller_interfaces__msg__ServoPositionValues * data =
      (hexapod_controller_interfaces__msg__ServoPositionValues *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!hexapod_controller_interfaces__msg__ServoPositionValues__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          hexapod_controller_interfaces__msg__ServoPositionValues__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!hexapod_controller_interfaces__msg__ServoPositionValues__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
