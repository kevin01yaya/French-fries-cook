// MultiStepper.pde
// -*- mode: C++ -*-
// Use MultiStepper class to manage multiple steppers and make them all move to 
// the same position at the same time for linear 2d (or 3d) motion.

#include <AccelStepper.h>
#include <MultiStepper.h>

// Joint 1
#define E1_STEP_PIN 36
#define E1_DIR_PIN 34
#define E1_ENABLE_PIN 30

// Joint 2
#define Z_STEP_PIN         46
#define Z_DIR_PIN          48
#define Z_ENABLE_PIN       A8
#define Z_MIN_PIN          18
#define Z_MAX_PIN          19

// Joint 3
#define Y_STEP_PIN         A6
#define Y_DIR_PIN          A7
#define Y_ENABLE_PIN       A2
#define Y_MIN_PIN          14
#define Y_MAX_PIN          15

// Joint 4
#define X_STEP_PIN 54
#define X_DIR_PIN 55
#define X_ENABLE_PIN 38

// Joint 5 
#define E0_STEP_PIN 26
#define E0_DIR_PIN 28
#define E0_ENABLE_PIN 24


// EG X-Y position bed driven by 2 steppers
// Alas its not possible to build an array of these with different pins for each :-(
AccelStepper joint1(1,E1_STEP_PIN, E1_DIR_PIN);
AccelStepper joint2(1,Z_STEP_PIN, Z_DIR_PIN);
AccelStepper joint3(1,Y_STEP_PIN, Y_DIR_PIN);
AccelStepper joint4(1,X_STEP_PIN, X_DIR_PIN);
AccelStepper joint5(1, E0_STEP_PIN, E0_DIR_PIN);

// Up to 10 steppers can be handled as a group by MultiStepper
MultiStepper steppers;

//test with uint8 converted to long
unsigned int x = 1000;

void setup() {
  Serial.begin(250000);




  // Configure each stepper
  joint1.setMaxSpeed(200);
  joint2.setMaxSpeed(200);
  joint3.setMaxSpeed(200);
  joint4.setMaxSpeed(200);
  joint5.setMaxSpeed(200);

  joint1.setMinPulseWidth(20);
  joint2.setMinPulseWidth(20);
  joint3.setMinPulseWidth(20);
  joint4.setMinPulseWidth(20);
  joint5.setMinPulseWidth(20);
 // joint2.setSpeed(2000);
  joint1.setAcceleration(20);
  joint2.setAcceleration(20);
  joint3.setAcceleration(20);
  joint4.setAcceleration(20);
  joint5.setAcceleration(20);



  // Then give them to MultiStepper to manage
  steppers.addStepper(joint1);
  steppers.addStepper(joint2);
  steppers.addStepper(joint3);
  steppers.addStepper(joint4);
  steppers.addStepper(joint5);
}

void loop() {
  long positions[5]; // Array of desired stepper positions

  // Back of the envelope calculation for microsteps/revolution, where positions[i] is the number of steps (or microsteps).
  positions[0] = 1000; //4100 microsteps is 1/8 revolutions ----> 32800 microsteps/rev
  positions[1] = 1000; //2000 is 40/360 revolutions ---> 18000 microsteps/rev
  positions[2] = 1000; //4000 is 20/360 revolutions ---> 72000 microsteps/rev
  positions[3] = 1000; //820 is 1/4 revolution (200steps/revolution * 16microsteps/step (since microstepping) ~= 32800 microsteps/rev)
  positions[4] = 1000; //2000 is 50/360 revolution ---> 14400
  
  steppers.moveTo(positions);
  steppers.runSpeedToPosition(); // Blocks until all are in position
  delay(1);
  
  // Move to a different coordinate
  positions[0] = 0;
  positions[1] = 0;
  positions[2] = 0;
  positions[3] = 0;
  positions[4] = 0;
  steppers.moveTo(positions);
  steppers.runSpeedToPosition(); // Blocks until all are in position
  delay(1);
}
