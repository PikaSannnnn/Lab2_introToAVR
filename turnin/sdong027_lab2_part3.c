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
	DDRC = 0xFF; PORTC = 0x00; // Configure port B's 8 pins as outputs, initialize to 0s
	unsigned char tmpA = 0x00; // Temporary variable to hold the value of A
	unsigned char cntavail = 0x00; // Counter of available spaces
	unsigned char tmpC = 0x00;

	while(1) {
		// Read pins 3 to 0
		tmpA = PINA & 0x0F;	

		cntavail = !(tmpA & 0x01) + !((tmpA >> 1) & 0x01) + !((tmpA >> 2) & 0x01) + !((tmpA >> 3) & 0x01);
		tmpC = cntavail & 0x0F;
		
		if (!cntavail) {	// If the number of available spaces is 0 (full), do this
			tmpC = tmpC | 0x80;
		}

		// 3) Write output
		PORTC = tmpC;
	}
	return 0;
}
