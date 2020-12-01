
//Reciever code
#include<SPI.h>
#include<nRF24L01.h>
#include<RF24.h>

#define CE_PIN 8
#define CSN_PIN 7

const byte thisSlaveAddress[5] = {'R', 'x', 'A', 'A', 'A'};

RF24 radio(CE_PIN, CSN_PIN);

char dataRecieved[500];

bool newData = false;


void setup() {
  Serial.begin(19200);
  radio.begin(); 
  radio.setDataRate(RF24_250KBPS);
  radio.openReadingPipe(1, thisSlaveAddress);
  radio.startListening();
}


void loop() {
  if(radio.available()){    radio.read(&dataRecieved, sizeof(dataRecieved));
    newData = true;
    showData();  
  }

}


void showData(){
  if(newData == true){
    Serial.println(dataRecieved);
    newData = false;  
  }  
}
