# 8-bit CPU & Assembler
The CPU was built with logic gate simulation software called Logisim-Evolution and the Assembler is built in Python.

This project contains:
* 8-bit CPU with a basic instruction set
* 16 bytes of RAM
* Simple assembler

## Installation and Setup Instructions
Clone this repository. You will need to have Java SE Development Kit installed in order to run Logisim-Evolution. Java SE Development Kit: https://www.oracle.com/java/technologies/javase-jdk13-downloads.html

To open logisim-evolution you will then have to run the 'logisim-evolution.bat' file. Upon opening Logisim-Evolution you can then open the 'CPU_8_bit.circ' file to open the CPU circuit.

## Operation
To use the CPU you will first need to write an assembly program that you wish to run in a .txt file. After writing the .txt file you will then have to run the 'Assembler.py' file to convert the assembly code to machine code. 

Once retrieving the machine code you can now open the 'CPU_8_bit.circ' file and load the machine code into the 16 byte RAM. To load the program into RAM you will have to enable 'program_mode' and then change the 'program_mem' and 'program_addr' inputs to the machine code specified in the file retrieved with the python program. To save the information into memory you will have to clock the 'pclk' one time per instruction.

After loading the program into the 16 byte RAM you can turn off the 'program_mode' and set the 'pclk' to be in a low state. To run the program you can either manual toggle the 'clk' input or go to the 'Simulate' tab in Logisim-Evolution menu bar and check the 'Ticks Enabled' box.

## Screenshots
![Circuit showcase](screenshots/8bitcpu.PNG)
