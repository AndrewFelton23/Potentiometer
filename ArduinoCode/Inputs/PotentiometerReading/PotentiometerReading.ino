//Include the CV zone header file
#include <cvzone.h>
//Initialize the Serial data 
SerialData serialData;
//Initialize the array thats being sent
int SendVals[2];  //the array should always have a 
                  //size of two as it sometimes creates issues


void setup() {
  //Initialize serial data with the baud rate of 9600
  serialData.begin(9600);
  pinMode(A0,INPUT);

}

void loop() {
  //define inputs
  int PotVal = analogRead(A0);
  //populate the array being sent to python
  SendVals[0] = PotVal;
  //Send values to python code
  serialData.Send(SendVals);
}
