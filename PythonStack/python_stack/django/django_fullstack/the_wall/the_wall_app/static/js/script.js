document.addEventListener("DOMContentLoaded", function () {
    setTimeout(function () {
        let alertBox = document.querySelector(".general-errors");
        if (alertBox) {
            alertBox.style.transition = "opacity 1s ease";
            alertBox.style.opacity = "0";
            setTimeout(() => alertBox.remove(), 1000);
        }
    }, 3000);
});