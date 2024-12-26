console.log("page loaded...");

const _$videoElement = document.querySelector("#video");
const _$previewHeader = document.querySelector(".preview");

//on mouse over play video
function play() {
    _$videoElement.play();
    _$previewHeader.style.opacity = "0.9";
}

//on mouse out pause video
function pause() {
    _$videoElement.pause();
    _$previewHeader.style.opacity = "0";
}