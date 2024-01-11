## Calculator

### What is it?
It's a simple calculator.

### What does it do?
It can do simple calculations. Meaning, it can add, subtract, multiply, and divide.

### How do you use it?
1. Enter a number.
2. Select an operator.
3. Enter a second number.
4. Hit the "=" button to see your results.
(Optional) 
5. Select an operator.
6. Enter a number.
7. Hit "=".

### Challenges and things I learned.
My biggest issue with this project was figuring out how take the numers entered in the calculator and create one number.
For example, getting 123, from individual entries of 1, 2, and 3.

What I ended up doing was appending each number to a list and then joining the list upon selecting an operator.
This made it so you can enter your first number, select an operator, and start entering your second number.

When it comes time to actually do the math, I then convert the joined list into a float so operations can be performed against them.

So to recap, the entry 123, would first be [1, 2, 3], then converted to "123", which would then be converted to 123.0.

### Known Issues and Bugs.
YMMV, but in my experience on Mac OS 14.2, there's an issue with the buttons in the UI being really hard to press.
I ended up having to long press each button before it would register.



