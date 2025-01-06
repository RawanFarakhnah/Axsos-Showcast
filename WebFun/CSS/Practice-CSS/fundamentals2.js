//Fundamentals To Do 2

console.log(`\n---- Happy coding! Fundamentals To Do 2-----\n`);
/**
 * Countdown
 * Create a function that accepts a number as an input.
 * Return a new array counts down by one,from the number
 * (as array's 'Zeroth' element) down to 0(as the last element)
 * How long is this array?
 */
console.log(`\n---- TODO:1 Countdown -----`);
function Countdown(num) {
  let countdownArr = [];
  for (; num >= 0; num--) {
    countdownArr.push(num);
  }

  console.log(`Length of countdown array: ${countdownArr.length}`);
  return countdownArr;
}
console.log(`counting down ${Countdown(9)}`);

/**
 * Print and Return
 * Your Function will receive an array with two numbers.
 * Print the first value, and return the second
 */
console.log(`\n---- TODO:2 Print and Return -----`);

function PrintAndReturn(arr) {
  if (arr.length !== 2) {
    console.log("Array must contain exactly two elements.");
    return;
  }

  let first = arr[0];
  console.log("Array first value is ", first); // output 5
  return arr[1];
}

let second = PrintAndReturn([5, 7]); // return the second
console.log("Array second value is ", second); // output 7

/**
 * First Plus Length
 * Given an array, return the sum of the first value in the array,
 * plus the array's length.What happenes if the arrayy's first value is not a number, but a string(like "what?") or a boolean (like false)
 */
console.log(`\n---- TODO:3 First Plus Length  -----`);
function GetFirstElementPlusLength(arr) {
  if (arr.length < 1) {
    console.log("Array must contain at least one elements.");
    return;
  }

  return arr[0] + arr.length;
}

console.log(GetFirstElementPlusLength([])); // output undefined
console.log(GetFirstElementPlusLength([1])); // output 2
console.log(GetFirstElementPlusLength([false, true, "what?"])); // output 3
console.log(GetFirstElementPlusLength(["rawan", true, 70])); // output rawan3
console.log(GetFirstElementPlusLength([true])); // output 2
console.log(GetFirstElementPlusLength([false])); // output 1

/**
 * Values Greater than Second
 * For [1,3,5,7,9,13] print values that are greater than its 2nd value
 * return how many values this is
 */
console.log(`\n---- TODO:4 Values Greater than Second -----`);

function GreaterThanSecond(arr) {
  let count = 0; // Initialize counter
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > arr[1]) {
      // Compare to the second element in the array
      console.log(arr[i]); // Print each value that is greater than the second element
      count++; // Increment counter
    }
  }
  return count; // Return the count of values greater than the second
}

let resultCount = GreaterThanSecond([1, 3, 5, 7, 9, 13]);
console.log(`Number of values Greater than Second: ${resultCount}`);

/**
 * Values Greater than Second, Generalized
 * write a function that accepts any array and return a
 * new array with the array values that are greater than its 2nd value.
 * Print how many values this is.
 * What will you do if the array is only one element long
 */
console.log(`\n---- TODO:5 Values Greater than Second, Generalized -----`);

function GreaterThanSecondGeneralized(arr) {
  if (arr.length < 2) {
    console.log("Array must have at least two elements.");
    return []; // Return an empty array if there are fewer than 2 elements
  }

  let newArray = []; // Initialize the new array
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > arr[1]) {
      // Compare each value to the second element
      console.log(arr[i]); // Print each value greater than the second
      newArray.push(arr[i]); // Add to the new array
    }
  }

  return newArray; // Return the new array with values greater than the second
}

let newArrayResult = GreaterThanSecondGeneralized([1, 3, 5, 7, 9, 13]);
console.log(
  `Number of values greater than the second: ${newArrayResult.length}`
);

/**
 * This Length, That Value
 * Given two numbers, return array of length num1 with each value num2
 * print "Jinx!" if they are same
 */
console.log(`\n---- TODO:6 This Length, That Value -----`);
