//Objects - Stored information in named properties
////////////////////////////////////////////////////////////////////////
// 1. Arrays vs. Objects: The Key Difference

// Arrays are ordered lists, ideal for storing collections of similar items, where the order of the elements matters. Arrays use numeric indices (0, 1, 2, etc.) to access elements.

// Objects are collections of key-value pairs, where the keys are typically strings (or symbols) and the values can be any type of data. Objects are better for storing data where key names are important, and the order doesn't matter.

////////////////////////////////////////////////////////////////////////
// 2. When to Use Objects
// Objects are great for scenarios where you want to associate properties with specific names (keys). They allow for easy access to data using meaningful names instead of numeric indices.

// Example: Storing Information About a Person
const person = {
  name: "Rawan",
  age: 25,
  job: "Developer",
};

console.log(person.name); // "Rawan"
console.log(person.age); // 25

// In this case, using an object makes it clear that name, age, and job are attributes of a person, and you can access each by its name.
////////////////////////////////////////////////////////////////////////

// 3. When to Use Arrays
// Arrays are useful when you have a collection of similar items (like numbers or strings) and the order matters. You access elements in an array by their index (0-based).

// Example: Storing a List of Numbers
const numbers = [1, 2, 3, 4];
console.log(numbers[0]); // 1
////////////////////////////////////////////////////////////////////////

// 4. Efficiency and Use Cases
///////////////////////////////////
// a) Grouping Data:
// Objects allow you to group data logically based on names, whereas arrays store data sequentially.

// Arrays: Ideal when you have an ordered collection of similar data.
// Objects: Ideal when you need to associate values with specific keys (i.e., attributes of something).
// Example:

// Array: A list of user names
const users = ["John", "Jane", "Doe"];

//Object: Storing a user's details with attributes.
const user = {
  name: "John",
  age: 30,
  email: "john@example.com",
};
//////////////////////////////////////
// b) Named Access vs. Indexing:
// In objects, you can directly access properties by name, making the code more readable and self-explanatory.

// Example: Accessing the property by name:
const book = {
  title: "JavaScript Basics",
  author: "John Doe",
  year: 2024,
};

console.log(book.title); // "JavaScript Basics"
// This is more meaningful and readable compared to accessing array elements by index (e.g., book[0] for the title).

//////////////////////////////////////////////////////////////////
// 5. Complex Data Structures
// Objects can store multiple types of data and can even contain other objects or arrays, making them flexible for complex data structures.

// Example: A Nested Object
const employee = {
  name: "Alice",
  department: "HR",
  address: {
    street: "123 Main St",
    city: "New York",
  },
  skills: ["Communication", "Negotiation", "Recruitment"],
};

console.log(employee.name); // "Alice"
console.log(employee.address.city); // "New York"
console.log(employee.skills[1]); // "Negotiation"
// Here, you have nested objects and arrays, and using objects allows you to structure data in a way that's easy to navigate.
