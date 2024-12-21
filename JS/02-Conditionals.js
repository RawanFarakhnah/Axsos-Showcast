//Conditionals

var isSunny = false;
var isRaining = true;

if (isSunny) {
  console.log("Wear sunscreen");
}

if (isRaining) {
  console.log("Bring an umbrella");
}

//else and else if
var today = new Date();
if (today.getDay() == 1) {
  console.log("I hate Mondays!");
}

if (today.getDay() != 1) {
  console.log("Today is alright!");
}

if (today.getDay() == 1) {
  console.log("I hate Mondays!");
} else {
  console.log("Today is alright!");
}

if (today.getDay() == 1) {
  console.log("I hate Mondays!");
} else if (today.getDay() != 1) {
  console.log("Friday? More like Fri-yay!");
} else {
  console.log("Today is alright!");
}

var temperature = 60;
var isRaining = false;

if (temperature >= 50) {
  if (!isRaining) {
    console.log("This is a good day to go for a walk!");
  }
}

if (temperature >= 50 && !isRaining) {
  console.log("This is a good day to go for a walk!");
}

//Modulo Operation ..
var isFiveEven = 5 % 2 == 0;
var is500Even = 500 % 2 == 0;

console.log(isFiveEven);
console.log(is500Even);

//Applaying modulo to other values
var isDivisible = 78 % 3 == 0;
console.log(isDivisible);

if (Infinity) {
  console.log("Infinity");
}

if (-Infinity) {
  console.log("-Infinity");
}
