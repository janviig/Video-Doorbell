
//creating servo object
Servo servoMotor;  

int rotationAngle = 0; 

void setup()
{
  //attaching trigger pin to D4
  servoMotor.attach(D4);  
}

void loop()
{
}

int motorRotate(String button)
{
    if(button=="open the door")
    {
        //button = 1
        //rotates to 180 degrees
        for(rotationAngle = 0; rotationAngle < 180; rotationAngle += 1)  
        {                             
        servoMotor.write(rotationAngle);          
        delay(10);                 
        }
        //rotates back to 0 degrees
        for(rotationAngle = 180; rotationAngle>=1; rotationAngle-=1)  
        {
        servoMotor.write(rotationAngle);   
        delay(10);                    
        }
        return 1;
    }
    else if(button=="ignore")
    {
        rotationAngle = 0;
        return 0;
    }
    else
    {
        return 0;
    }
}
