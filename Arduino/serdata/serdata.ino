const int ser_PIN = A0;
const int PIN = 12;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(ser_PIN, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
//  if (digitalRead(PIN) == HIGH){
//    Serial.println("通電");
//  }
  float t = analogRead(ser_PIN);
  String data = String(t, DEC);
  Serial.println(data);
  delay(500);
}
