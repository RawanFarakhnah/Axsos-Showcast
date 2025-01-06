function name_of_function() {}

function counter() {
  for (let num = 0; num <= 5; num++) {
    console.log(num);
  }
}

counter(); //run the function
console.log("\n");
counter(); //run the function

function counter(startNum) {
  for (let num = startNum; num >= 0; num--) {
    console.log(num);
  }
}

counter(8); //run the function
console.log("\n");
counter(4); //run the function
