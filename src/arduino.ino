//do not upload code while writing serial data :)(:
//#include <Servo.h>

String data;



//Servo x;

void setup(){
    Serial.begin(9600);
    Serial.setTimeout(1);
    pinMode(LED_BUILTIN, OUTPUT);
}

void loop(){
    if (Serial.available()>0){
        digitalWrite(LED_BUILTIN, HIGH);
    }
}