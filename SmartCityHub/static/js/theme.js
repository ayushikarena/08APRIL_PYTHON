console.log("theme.js loaded");

document.addEventListener("DOMContentLoaded", function () {

    const button = document.getElementById("theme-toggle");

    if (button) {
        button.addEventListener("click", function () {
            document.body.classList.toggle("dark-mode");
            console.log("Theme button clicked");
        });
    }

});
