//Fundamentals To Do 1
console.log(`\n---- Happy coding! Fundamentals To Do 1 -----\n`);
/**
 * Setting and Swapping 
 * Set myNumber to 42. set myName to your name 
  swap myNumber into myName and vice versa
 */
console.log(`\n---- TODO:1 Setting and Swapping -----`);

let myNumber = 42;
let myName = "Rawan Farakhna";
console.log(
  `Initial values (setting) => myNumber: ${myNumber}, myName: ${myName}.`
);

// First swap
let temp = myNumber; // holding 42
myNumber = myName; // holding "Rawan Farakhna"
myName = temp; // holding 42
console.log(`After first swap => myNumber: ${myNumber}, myName: ${myName}.`);

// Second swap (vice versa)
temp = myNumber; // holding "Rawan Farakhna"
myNumber = myName; // holding 42
myName = temp; // holding "Rawan Farakhna"
console.log(
  `After second swap (vice versa)=> myNumber: ${myNumber}, myName: ${myName}.`
);

/**
 * Print -52 to 1066
 * print integers from -52 to 1066 using  a For loop
 */
console.log(`\n---- TODO:2 Print -52 to 1066 -----`);
for (let i = -52; i <= 1066; i++) {
  console.log(`Counter: ${i}`);
}

/**
 * DON'T Worry, Be Happy
 * create beCheerful(). Whithin it, console.log string "good morning!"
 * call it 98 times.
 */
console.log(`\n---- TODO:3 DON'T Worry, Be Happy -----`);
function beCheerful() {
  console.log("good morning!");
}

//calling beCheerful function 98 times
for (let i = 1; i <= 98; i++) {
  beCheerful();
}

/**
 * Multiples of Three - but Not All
 * using FOR , print multiples of 3 from -300 to 0.
 * skip -3 and -6
 */

console.log(`\n---- TODO:4 Multiples of Three - but Not All -----`);

for (let i = -300; i <= 0; i++) {
  if (i % 3 === 0 && i !== -3 && i !== -6) {
    console.log(i);
  }
}

/**
 * Printing Integers With While
 * Print integers from 2000 to 5280, using a While
 */

console.log(`\n---- TODO:5 Printing Integers With While -----`);

let i = 2000;
while (i <= 5280) {
  console.log(`Counter: ${i}`);
  i++;
}

/**
 * You Say It's Your Birthday
 * If 2 given numbers represent your birth month and day in either order,
 * log "How did you Know?" , else log "Just another day...."
 */

console.log(`\n---- TODO:6 You Say It's Your Birthday -----`);
function yourBirthday(num1, num2) {
  let day = 26,
    month = 12;
  if ((num1 === day && num2 === month) || (num1 === month && num2 === day)) {
    console.log("How did you Know?");
  } else {
    console.log("Just another day....");
  }
}

yourBirthday(26, 12);

/**
 * Leap Year
 * Write a function that determines whether a given year is a leap year.
 * If a year is divisble by four, it is a leap year,
 * unless it it divisible by 100.
 * if it is divisible by 400, then it is
 */
console.log(`\n---- TODO:7 Leap Year -----`);
function IsLeapYear(year) {
  if (year % 400 == 0) {
    return true; // divisble by 400
  } else if (year % 100 === 0) {
    return false; // divisble by 100
  } else if (year % 4 === 0) {
    return true; // divisble by 4
  } else {
    return false;
  }
}

console.log(`2000 Is Leap Year? ${IsLeapYear(2000)}`);
console.log(`1900 Is Leap Year? ${IsLeapYear(1900)}`);
console.log(`2024 Is Leap Year? ${IsLeapYear(2024)}`);
console.log(`2023 Is Leap Year? ${IsLeapYear(2023)}`);

/**
 * Print and Count
 * Print all integer multiples of 5, from 512 to 4096.
 * Afterward, also log how many there were.
 */
console.log(`\n---- TODO:8 Print and Count -----`);
let count = 0;
for (let i = 512; i <= 4096; i += 5) {
  count++;
  console.log(`${i} multiples of 5`);
}

console.log(`Count is ${count}`);

/**
 * Multiples of Six
 * Print multiples of 6 up to 60,000 using a While
 */
console.log(`\n---- TODO:9 Multiples of Six -----`);
let multipleOfSix = 6,
  multiplesCount = 0;

while (multipleOfSix <= 60000) {
  multiplesCount++;
  console.log(`Multiple of 6: ${multipleOfSix}`);
  multipleOfSix += 6;
}

console.log(`Count is ${multiplesCount}`);

/**
 * Counting, the Dojo Way
 * Print integers 1 to 100. If divisible by 5, print "Coding"
 * insted. If by 10, also PRINT "Dojo"
 */
console.log(`\n---- TODO:10 Counting, the Dojo Way -----`);
for (let i = 1; i <= 100; i++) {
  if (i % 10 === 0) {
    console.log("Coding Dojo");
  } else if (i % 5 === 0) {
    console.log("Coding");
  } else {
    console.log(i);
  }
}

/**
 * What Do You Know
 * your function will be given an input parameter incoming.
 * please console.log this valve
 */
console.log(`\n---- TODO:11 What Do You Know -----`);
function PrintOut(incoming) {
  console.log(incoming);
}

PrintOut("Coding is fun :)");

/**
 * Whoa, That Sucker's Huge
 * Add odd integers from -300,000 to 300,000
 * and console.log the final sum
 * Is there a shortcut?
 */
console.log(`\n---- TODO:12 Whoa, That Sucker's Huge -----`);
let OddSummation = 0;

for (let i = -300000; i <= 300000; i++) {
  if (i % 2 !== 0) {
    OddSummation += i; // it is odd
  }
}

console.log(`\n---- Summation is ${OddSummation}-----`);

/**
 * Countdown by Fours
 *Log positive numbers starting at 2016, counting down by 
 fours (exclude 0)
 without a FOR loop
 */
console.log(`\n---- TODO:13 Countdown by Fours -----`);
let countdown = 2016;

while (countdown > 0) {
  console.log(`countdown is ${countdown}`);
  countdown -= 4;
}

/**
 * Flexible Countdown
 *Based on earlier "Countdown by Fours",
 given lowNum, highNum, mult, print multiples of mult 
 from highNom down to lowNum,
 using a FOR, For (2,9,3), print 9 6 3
 on successive lines
 */
console.log(`\n---- TODO:14 Flexible Countdown -----`);

function FlexibleCountdown(lowNum, highNum, mult) {
  let message = "";
  for (; highNum >= lowNum; highNum--) {
    if (highNum % mult === 0) {
      message += `${highNum} `;
    }
  }
  return message.trim();
}

console.log(FlexibleCountdown(2, 9, 3)); // Expected output: "9 6 3"

/**
 * The Final Countdown
 *Based on "Flexible Countdown", The parameter names are not as helpful,
 but the problm is essentially identical; don't be thrown off!
 Given 4 parameters (param1,param2,param3,param4)
 print the multiples of param1, starting at param2 and extending to param3
 if a multiple is equal to param4 then skip (don't print) it
 Do this using While Given (3,5,17,9), print 6,12,15

 */
console.log(`\n---- TODO:14 Flexible Countdown -----`);
function FinalCountdown(param1, param2, param3, param4) {
  let message = "";
  while (param2 <= param3) {
    //Given (3,5,17,9)
    if (param2 % param1 === 0 && param2 !== param4) {
      message += `${param2} `;
    }
    param2++;
  }

  return message.trim();
}

console.log(FinalCountdown(3, 5, 17, 9)); // Expected output: "6,12,15"
