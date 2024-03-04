#include <LiquidCrystal.h>
//initialise the library with the numbers of the interface pins 
LiquidCrystal lcd(12, 11, 5, 4, 3, 2); 
int buzzer = 8;
int firstOccur = 0;
int thermopin = A5;
int lcdscreen = 8;
int enable = 9;
float v; 
float R1 = 10000;
float logr2, r2;
int t = 0;
float c1 = 1.009249522e-03, c2 = 2.378405444e-04 , c3 = 2.019202697e-07;
int digitalV;
// Constants for the Steinhart-Hart equation
const float A = 0.001125308852122;   // Steinhart-Hart coefficient A
const float B = 0.000234711863267;   // Steinhart-Hart coefficient B
const float C = 0.000000085663516;   // Steinhart-Hart coefficient C




void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
// set up the LCD's number of columns and rows: 
  lcd.begin(16, 2); 
  lcd.setCursor(0,0);
    // Print a message to the LCD. 
  lcd.print("current tem: "); 
   pinMode(buzzer, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
   lcd.setCursor(0,1);
     
v = analogRead(thermopin);
// Convert the analog value to resistance
   float resistance = (1023.0 / v) - 1.0;
   resistance = 10000.0 / resistance;

  // // Calculate the temperature using the Steinhart-Hart equation
   t = 1.0 / (A + (B * log(resistance)) + (C * pow(log(resistance), 3)));
//digitalV = v*5 / 1024;
// r2 = ((R1 * 5) / digitalV) - R1; 
// Serial.println(r2);
 //r2 = R1 * (1023.0 / (float)digitalV - 1.0);
//logr2 = log(r2);
//t = (1.0/(c1 + c2 * logr2 + c3*logr2 *logr2 * logr2));
t = t - 273.15;
if (float(t) > 10 || float(t) < -4)
{
  if (firstOccur == 1)
    digitalWrite(buzzer, HIGH); 
}
 else
 {
  digitalWrite(buzzer, LOW); 
  firstOccur = 1;
 }

Serial.println(t,2);
lcd.print(float(t));
lcd.print(" celsius");
delay(1000);

}
