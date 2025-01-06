// arrays
/**
 *a large amount of data needs to be stored in order to resolve a particular issue. If we were attempting to analyze a programmers expenses through coding, we might think about storing each purchase as a variable
 */

//Why Use ARRAYES
/**
 * IT IS Essential in data structure in programming
 * provide us a simple and efficient way to store and manage collection of data
 * Insted of creating multiple variables for related items
 * array allow you to store all those items in one place
 */

//[1] Organized Storge for Multiple items
//Without array
let item1 = "Apple";
let item2 = "Banana";
let item3 = "Chery";

//With Array : code cleaner and easier to maintinance
let items = ["Apple", "Banana", "Chery"];

//[2] Easy Access With Indexes
let fruits = ["Apple", "Banana", "Cherry"];
//Each item can be accessed using its index(position in the array)
//First item is at index 0

fruits[0];

//[3] Dynamically Sized Array can grow or shrinks in size, maxing them flexible for different types of data manipulation

let numberes = [1, 2, 3, 4];
numberes.push(5);
console.log(numberes);

//Removing itemes
numbers.pop(); // Removes the last item
console.log(numbers); // Output: [1, 2, 3, 4]

//[4] Looping Through Items
//Arrays work seamlessly with loops, allowing you to iterate through all their elements.
let colors = ["Red", "Green", "Blue"];
for (let i = 0; i < colors.length; i++) {
  console.log(colors[i]);
}

//[5] Useful Array Methods
/**
 * push(): Adds an item to the end.
 * pop(): Removes an item from the end.
 * shift(): Removes an item from the start.
 * map(): Transforms each element.
 * filter(): Filters elements based on a condition.
 */
