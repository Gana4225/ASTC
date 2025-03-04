document.addEventListener("DOMContentLoaded", function() {
    let header = document.getElementById("header");
    header.style.transition = "all 0.5s ease-in-out";

    header.addEventListener("mouseover", function() {
        header.style.backgroundColor = "#ff00ff";
    });

    header.addEventListener("mouseleave", function() {
        header.style.backgroundColor = "rgba(0, 255, 128, 0.8)";
    });

    // Theme switching (optional)
    let themeButton = document.createElement("button");
    themeButton.innerText = "Switch Theme";
    themeButton.style.position = "fixed";
    themeButton.style.top = "10px";
    themeButton.style.right = "10px";
    themeButton.style.padding = "10px";
    themeButton.style.background = "#ff0000";
    themeButton.style.color = "white";
    themeButton.style.border = "none";
    themeButton.style.cursor = "pointer";

    document.body.appendChild(themeButton);

    themeButton.addEventListener("click", function() {
        document.body.classList.toggle("dark-mode");
    });
});
