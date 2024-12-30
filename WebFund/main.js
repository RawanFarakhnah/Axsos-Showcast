function removeButton(element) {
    element.remove();
}

//This function will update counter when Book button clicked 
function onBooking(elementId) {
    let _$counterElement = document.getElementById(elementId);
    let _$count = _$counterElement.innerHTML;
    _$count = Number(_$count) + 1;
    _$counterElement.innerHTML = _$count;
}

function onReadMore() {
    let _$paragrphElement = document.querySelector(".header-content");
    _$paragrphElement.innerText = "This content changed !!!" 
    // _$paragrphElement.style.opacity = "0";
    
    let clientImageElement = document.querySelector("#client-image");
    clientImageElement.src = "images/client.png";
}

function showImage(element){
    let imageElement = document.getElementsByClassName(element);
    imageElement[0].classList.remove("imag");
}