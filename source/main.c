/*	Author: sdong027
 *  Partner(s) Name: 
 *	Lab Section:
 *	Assignment: Lab #2  Exercise #3
 *	Exercise Description: [optional - include for your own benefit]
 *
 *	I acknowledge all content contained herein, excluding template or example
 *	code, is my own original work.
 */
#include <avr/io.h>
#ifdef _SIMULATE_
#include "simAVRHeader.h"
#endif	

int main(void) {
	DDRA = 0x00; PORTA = 0xFF; // Configure port A's 8 pins as inputs
	DDRB = 0x00; PORTB = 0xFF; // Configure port B's 8 pins as inputs
	DDRC = 0x00; PORTC = 0xFF; // Configure port C's 8 pins as inputs
	DDRD = 0xFF; PORTD = 0x00; // Configure port D's 8 pins as inputs; all pins to 0
	
	unsigned char tmpA = 0x00; 
	unsigned char tmpB = 0x00; 
	unsigned char tmpC = 0x00; 
	unsigned char tmpD = 0x00; 
	unsigned short totWeight = 0x0000;

	while(1) {
		// Read all pins
		tmpA = PINA & 0xFF;	
		tmpB = PINB & 0xFF;	
		tmpC = PINC & 0xFF;	

		totWeight = tmpA + tmpB + tmpC;
		if (totWeight > 140) {
			tmpD = (tmpD & 0x00) | 0x01;
		}
		
		if ((tmpA - tmpC) > 80) {
			tmpD = tmpD | 0x02;
		}
		else if ((tmpC - tmpA) > 80) {
			tmpD = tmpD | 0x02;
		}

		tmpD = tmpD | ((totWeight & 0x03F0) >> 2);	// get the top 6 most significant bits, 765 max -> 10 bits will be used

		PORTD = tmpD;
	}
	return 0;
}
