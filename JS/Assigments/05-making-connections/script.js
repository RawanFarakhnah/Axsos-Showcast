console.log("page loaded...");

//function to change username
function changeUsername() {
    let _$username = document.getElementById("username");
    _$username.innerHTML = "Rawan Farakhna";
}

// Remove list item and Decrease Connection Badge
function handlingConnection(elementId) {
    let _$element = document.getElementById(elementId);
    _$element.remove();

    let _$badgeElement = document.querySelector(".badge");
    _$badgeElement.innerHTML --;
}

// Increase Your Connection Badge
function handlingYourConnectionBadge() {
     let _$badgeElement = document.querySelectorAll(".badge");
     let _$count = _$badgeElement[1].innerHTML;
     _$count = parseInt(_$count);
     _$count += 1;
     _$badgeElement[1].innerHTML = `${_$count}+`;
}

//handling accept connection request
function onAcceptConnection(elementId) {
    handlingConnection(elementId);
    handlingYourConnectionBadge();
}

//handling reject connection request
function onRejectConnection(elementId) {
    handlingConnection(elementId);
}