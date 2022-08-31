//do not upload code while writing serial data :)(:
#include <Servo.h>

String data;

Servo motor;


//Servo x;

void setup(){
    Serial.begin(9600);
    Serial.setTimeout(1);
    pinMode(LED_BUILTIN, OUTPUT);
    motor.attach(2);
}

void loop(){
    if (Serial.available()>0){
        Serial.write("data available");
       
        data = Serial.readString();

        if (data == "n"){
            digitalWrite(LED_BUILTIN, HIGH);
            motor.write(45);
            Serial.write("led on");
        }else if (data == "f"){
            digitalWrite(LED_BUILTIN, LOW);
            motor.write(135);
            Serial.write("led off");
        } else {
            Serial.write("come again");
        }
    }
}