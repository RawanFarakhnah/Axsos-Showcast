//Loop Challenges

console.log("\n Loop Challenges \n");

// Challenge [1]: Display odd numbers between [1-20]
console.log("\n Challenge [1] : Display odd numbers between [1-20] \n");

for (let i = 1; i < 20; i++) {
  let isOdd = i % 2 != 0;
  if (isOdd) {
    console.log(i);
  }
}

// Challenge [2]: Display all numbers between [100-0] that divisible by 3
console.log("\n Challenge [2] : Decreasing multiples of 3 \n");
for (let i = 100; i > 0; i--) {
  let isDivisibleBy3 = i % 3 == 0;
  if (isDivisibleBy3) {
    console.log(i);
  }
}

// Challenge [3]: Write to print the values in sequence 4, 2.5, 1, -0.5, -2, -3.5
console.log("\n Challenge [3] : Print the given sequence \n");
for (let i = 4; i >= -3.5; i -= 1.5) {
  console.log(i);
}

// Challenge [4]: sum of all numbers [1-100]
console.log("\n Challenge [4] : Sigma \n");
let sum = 0;
for (let i = 1; i <= 100; i++) {
  sum += i;
}
console.log(sum);

// Challenge [5]: Factorial
console.log("\n Challenge [5] : Factorial \n");
let product = 1;
for (let i = 1; i <= 12; i++) {
  product *= i;
}
console.log(product);
