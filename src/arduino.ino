#include <Servo.h>

const unsigned int MAX_MESSAGE_LENGTH = 6;

Servo MX;
Servo MY;

void setup() {
    Serial.begin(9600);
    MX.attach(2);
}

void loop() {

 //Check to see if anything is available in the serial receive buffer
    while (Serial.available() > 0){
    //Create a place to hold the incoming message
    static char message[MAX_MESSAGE_LENGTH];
    static unsigned int message_pos = 0;

    //Read the next available byte in the serial receive buffer
    char inByte = Serial.read();

    //Message coming in (check not terminating character) and guard for over message size
    if ( inByte != '\n' && (message_pos < MAX_MESSAGE_LENGTH-1))   {
        //Add the incoming byte to our message
        message[message_pos] = inByte;
        message_pos++;
        } else {//Full message received...
            //Add last byte.
            message[message_pos] = inByte;

            //Print the message (or do other things)
            int xPos = (String(message[0]) + String(message[1]) + String(message[2])).toInt() - 100; 
            int yPos = (String(message[3]) + String(message[4]) + String(message[5])).toInt() - 100; 
            Serial.println(xPos);
            Serial.println(yPos);
            MX.write(xPos);
        

            //Reset for the next message
            message_pos = 0;
        }
    }
}
