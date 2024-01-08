int led = 13;
char tada ;

void setup()
{
  pinMode(led, OUTPUT);
  //pinMode(LED_BUILTIN, OUTPUT);
  //Serial.begin(9600);
  digitalWrite(led, LOW);
  //digitalWrite(LED_BUILTIN, LOW);
  
}

void loop()
{
  if ( Serial.available()>0 )
  {
    tada = Serial.read();

    if ( tada == '1')
    {
      digitalWrite(led, HIGH);
      delay(1000);
      //digitalWrite(LED_BUILTIN, HIGH);
    }
    else if ( tada == '0')
    {
      digitalWrite(led, LOW);
      delay(1000);
      //digitalWrite(LED_BUILTIN, LOW);
    }
  }
  }
