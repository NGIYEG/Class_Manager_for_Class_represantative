document.addEventListener("mousedown", function(event) {
    let mouseButton = event.button; // 0 = Left, 1 = Middle, 2 = Right

    // Check which mouse button was clicked
    if (mouseButton === 0) {
        document.getElementById("demo").innerHTML = "Left click detected!";
    } else if (mouseButton === 1) {
        document.getElementById("demo").innerHTML = "Middle click detected!";
    } else if (mouseButton === 2) {
        document.getElementById("demo").innerHTML = "Right click detected!";
    }
});
