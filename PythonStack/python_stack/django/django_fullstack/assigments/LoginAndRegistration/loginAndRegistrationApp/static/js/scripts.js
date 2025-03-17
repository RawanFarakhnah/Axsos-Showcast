// Flash Message
setTimeout(function() {
    const flashMessage = document.getElementById("flash-message");
    if (flashMessage) {
        flashMessage.style.display = "none";
    }

    const loginFlashMessage = document.getElementById("login-flash-message");
    if (flashMessage) {
        flashMessage.style.display = "none";
    }

}, 5000);
