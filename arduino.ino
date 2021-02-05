#define echoPin 7
#define trigPin 8

long duration;
long distance;

void setup() {  
  
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);  
  
}

void loop() {  
  
  digitalWrite(trigPin,LOW);
  delayMicroseconds(5);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = duration / 58.2;

  if(distance >= 50)
    distance = 0; 
  
  Serial.println(distance);
  delay(200);    
  
}
