function custom(element) {
  element.innerText = "Oppps!!";
  console.log("this is element that was clicked", element);
}

function turnOff(element) {
  element.innerText = "Off";
}

function hide(element) {
  // Add the fade-out class
  element.classList.add("fade-out");

  // Wait for the transition to complete, then remove the element
  element.addEventListener("transitionend", () => {
    element.remove();
  });
}

function refreshPage() {
  // Refresh the page
  location.reload();
}

function over(element) {
  element.style.backgroundColor = "lavender";
  element.style.transition = "background-color 0.3s ease"; // Smooth transition
  element.style.cursor = "pointer"; // Change cursor to pointer for interactivity
}

function out(element) {
  element.style.backgroundColor = "white"; // Reset to default color
  element.style.transition = "background-color 0.3s ease"; // Smooth transition
}
