if ({}) {
  console.log("Object is Empty");
}

if ([]) {
  console.log("Array is Empty");
}

//Common Misunderstanding
console.log("\n Common Misunderstanding");
if ({}) {
  console.log("This won't run because the object is empty");
}
// the thing is people thought that "empty" with "nothingness", which feels like it should evaluate to false -> this true for "" (empty string) , null , undefined , 0

//in our case : obects ({}) and arrays ([]) are not "nothingness" they are reference types with memory allocated for them, even if they contain no data.

//To Check empty in objects or arrayes
const obj = {};
if (Object.keys(obj).length === 0) {
  console.log("Object is Empty");
}

const arr = [];
if (arr.length === 0) {
  console.log("Array is Empty");
}

//Properties set of null to indicates the absence of a value
console.log("Explicitly assigned");
const obj0 = {
  name: "Alice",
  age: null, // explicity has no values ' is often used when you intentionally want to indicate that a property should not have a value yet.'
};

console.log("\nVariables Declared but Not Initialized");
var age;
console.log("age", age); //output undefined mean declared without assigning any values or it declared from object

const obj1 = {
  name: "Bob",
  age: 20,
};

delete obj1.age;
console.log(obj.age);

//undefined in arrays
console.log("\n undefined in arrays");
const arr1 = [10, 20, 30];
console.log(arr1);
delete arr1[1];
console.log(arr1);
console.log(arr1[1]);
console.log(arr1.length);

function greet(name, age) {
  console.log("Name:", name); // If not passed, 'name' will be undefined
  console.log("Age:", age); // If not passed, 'age' will be undefined
}

greet("David");

//Object Destructuring
console.log("\n\n Missing Return Statements in Functions");
const user = { name: "Eve" };
const { name, age2 } = user;

console.log(name); //output: Eve
console.log(age2); //output: undefine

//Missing Return Statements in Functions
console.log("\n\n Missing Return Statements in Functions");
function noReturn() {
  const x = 5;
}

console.log(noReturn()); //output: undefine
