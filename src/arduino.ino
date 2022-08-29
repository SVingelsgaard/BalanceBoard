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
        Serial.write("data available");
       
        data = Serial.readString();

        if (data == "n"){
            digitalWrite(LED_BUILTIN, HIGH);
            Serial.write("led on");
        }else if (data == "f"){
            digitalWrite(LED_BUILTIN, LOW);
            Serial.write("led off");
        } else {
            Serial.write("come again");
        }
    }
}