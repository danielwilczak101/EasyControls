# Adafruit MPU6050 Tutorial

## Pin Setup
![Image of Wire Connections]()

## Ensure 

# Using the Moteus Controller

[The Moteus controller](https://mjbots.com/products/moteus-r4-11) was chosen for the CubeSat testbed because of it's ease of use and capability to control position, velocity, acceleration, and torque with one command. The following is a step by step guide explaining how to implement the Moteus controller as well as vital commands to properly use the controller. 

[Moteus controller reference document](https://github.com/mjbots/moteus/blob/main/docs/reference.md)

## Step 1

Install the moteus and asynchio libraries to your raspberry pi:

```pip3 install moteus
pip3 install asynchio
```

## Step 2

The CubeSat testbed made use of the [mj5208 brushless motor](https://mjbots.com/collections/accessories/products/mj5208) which is made by the same company which sells the Moteus controller. But, the controller should work with any other motor. 

Calibrate your motor:

```python3 -m moteus.moteus_tool --target 1 --calibrate```

## Step 3

The controller comes with limiting default values by default. These configurable values must be changed to properly utilize the controller.

In the terminal, run the following to open the controller console:

```moteus_tool --console```

You should see "Target 1" printed on the terminal.

You may now type ```conf set``` followed by any of the following to configure the controller's deafult values:

```servo.default_velocity_limit``` / ```servo.default_accel_limit```

These commands may be following by a space and either ```nan``` or a numerical value (these are set the ```nan``` for the CubeSat project). **The unit for velocity is rotations per second.**

```servo.max_velocity```

DO NOT SET THIS VALUE TO ```nan```. This value is configured to 120 for the CubeSat project.

There is a comprehensive list of all configurable values in the Moteus controller reference document linked above.


After having set confirgurable values, permanently save these changes with ```conf write```. If you do not save your values, they will be reset the next time you use the controller.

Additionally, you can check the value of a configurable value with ```conf set``` followed by the parameter of interest. 

## Step 4

One tricky aspect of using this controller is that it requires the use of asynchronous code (even if your goals only require synchronous code). Please refer to the example scripts to understand how to format your python code. 

## Step 5

At the start of your main asynchronous function, initialize the Moteus controller with the following:

```c = moteus.Controller()```

Then, run ```await c.set_stop()``` to clear any fault state which the controller may currently be in. The controller may enter a fault state for many different reasons. Some common faults include forcing the motor to accelerate at a rate greater than the configured max_accel_limit value, undervoltage on behalf of the power source, etc. An extensive list can be found below. 

## Step 6

It is now time to send a control command to the controller. 

```state = await c.set_position()```

The arguments for this command may include any or all of the following:

-position (set to ```math.nan``` if velocity control is desired)
-velocity
-feedforward_torque
-kp_scale
-maximum_torque
-stop_position
-watchdog_timeout
-query (must = True)

The CubeSat tesbeds commonly uses this command in the following manner:

```state = await c.set_position(position = math.nan, velocity = expectedVelocity, query = True)```
