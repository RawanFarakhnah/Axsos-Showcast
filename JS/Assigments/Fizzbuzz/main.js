// FizzBuzz coding challenge

const fizzNumber = 3; // Divisible number for "Fizz"
const buzzNumber = 5; // Divisible number for "Buzz"

for (let i = 1; i <= 100; i++) {
  const isFizz = i % fizzNumber === 0; // Check divisibility by fizzNumber
  const isBuzz = i % buzzNumber === 0; // Check divisibility by buzzNumber

  if (isFizz && isBuzz) {
    console.log('"FizzBuzz"');
  } else if (isFizz) {
    console.log('"Fizz"');
  } else if (isBuzz) {
    console.log('"Buzz"');
  } else {
    console.log(i);
  }
}
