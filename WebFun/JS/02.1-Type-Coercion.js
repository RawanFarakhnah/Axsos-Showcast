const value1 = "5";
const value2 = 9;
let sum = value1 + value2;
console.log(sum); //output: 59
console.log(typeof sum); //string

sum = Number(value1) + value2;
console.log(sum); //output: 14
console.log(typeof sum); //number

//--------------------------------
//Primitave data type --> not object
//example string, number, bigint, boolean, undefined, symbole, null

//we use null to intalize proprty or to refer to invalid object or adderes
//absence of any object value.
console.log(typeof null); //object it consider as a bug

function getVowels(str) {
  const match = str.match(/[aeiou]/gi);
  if (match === null) {
    return 0;
  }
  return match.length;
}

console.log("number of vowels : ", getVowels("sky"));
console.log("number of vowels : ", getVowels("eat"));

//foo;// error not defined

//avoideng error should at first defined it
const foo = null; //initalize foo for absence of any object value
