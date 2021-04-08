/*	Author: sdong027
 *  Partner(s) Name: 
 *	Lab Section:
 *	Assignment: Lab #2  Exercise #2
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

	while(1) {
		// Read pins 3 to 0
		tmpA = PINA & 0x0F;	
		// Counting number of available spaces
		unsigned char i;
		for (i = 0; i < 4; i++) {
			// cntavail = (cntavail & 0x0F) | (cntavail << 1 | !((tmpA >> i) & 0x01));
			if (!((tmpA >> i) & 0x01)) {
				cntavail++;	
			}
		}

		// 3) Write output
		PORTC = cntavail;
	}
	return 0;
}
