var tortilla = "soft corn tortilla";
var protein = "tinga chicken";
var cheese = "cotija cheese";
var toppings = ["lettuce", "pico de gallo", "guacamole"];

var taco1 = {
  tortilla: "soft corn tortilla",
  protein: "tinga chicken",
  cheese: "cotija cheese",
  toppings: ["lettuce", "pico de gallo", "guacamole"],
  tacoInfo: function () {
    console.log(this.tortilla);
    console.log(this.protein);
    console.log(this.cheese);
    console.log(this.toppings);
  },
};

taco1.tacoInfo();
