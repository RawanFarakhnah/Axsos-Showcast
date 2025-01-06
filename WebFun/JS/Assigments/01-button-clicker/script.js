//on click change inner text
function changeBtn(element) {
  let message = element.innerText;
  if (message.toLowerCase() === "login") {
    element.innerText = "logout";
  } else {
    element.innerText = "login";
  }
}

//on click remove btn
function removeBtn(element) {
  element.remove();
}

//on click display alert
function displayAlert() {
  alert("This page says \n Ninja was liked");
}
