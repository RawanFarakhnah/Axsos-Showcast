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