#include <Arduino.h>

#define PIR_PIN 5

void setup() {
    Serial.begin(115200);
    pinMode(PIR_PIN, INPUT);
}

void loop() {
    int motion = digitalRead(PIR_PIN);
    Serial.println(motion);
    delay(1000);
}
