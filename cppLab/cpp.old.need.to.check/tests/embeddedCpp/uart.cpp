#include "uart.h"


void uartInit(void){
    RCC -> APB1ENR |= 0x01; // Enable GPIOA  clock   
    RCC -> APB1ENR |= 0x02; //Enable USART2 clock

    /* Configure PA2, PA3 for USART2 TX, RX*/
     GPIOA -> AFR[0] |= 0x7700;   //7=0111
     GPIOA -> MODER  |= 0x00A0;   //enamble alternate function for PA2, PA3

     USART2 -> BRR = 0x0683;     //9600  baud @16Mhz
     USART2 -> CR1 = 0x000C;     //Enable Rx, Tx, 8-Bit data
     USART2 -> CR2 = 0x0000;     //1 Stop Bit
     USART2 -> CR3 = 0x0000;     // No flow control
     USART2 -> CR1 = 0x2000;     //enable usart2 
}