//Initalize Pizzeria
let pizza = {
  //function for making pizza
  pizzaOven: function (crust, sauce, cheese, toppings) {
    this.crust = crust;
    this.sauce = sauce;
    this.cheese = cheese;
    this.toppings = toppings;
    return pizza;
  },

  //function to Display Pizza Ingredients
  displayPizza: function () {
    let message = `PIZZA  INGREDIENTS \n CRUST: ${this.crust}\n SAUCE: ${this.sauce}\n CHEESE: ${this.cheese}\n TOPPINGS: ${this.toppings}\n`;
    return message;
  },
};

//function to Display Random Pizza
function randomPizza(arrOfPizza) {
  let randomNo = Math.floor(Math.random() * 4);
  let message = `My Random Pizza #${randomNo}\n ${arrOfPizza[
    randomNo
  ].displayPizza()}`;
  console.log(message);
}

//Array of Pizza
let myPizza = [
  pizza.pizzaOven("deep dish","tradidional",["mozzarella"],["pepperoni", "sausage"]),
  pizza.pizzaOven("hand tossed","marinara",["mozzarella", "feta"],["mushrooms", "olives", "onions"]),
  pizza.pizzaOven("thin crust","pesto",["mozzarella", "parmesan"],["chicken", "spinach", "tomatoes"]),
  pizza.pizzaOven("stuffed crust","bbq sauce",["cheddar", "mozzarella"],["bacon", "onions", "green peppers"])
];

//Display all Pizzas
myPizza.forEach((pizza) => {
  console.log(pizza.displayPizza());
});

//Display Random Pizza
randomPizza(myPizza);
