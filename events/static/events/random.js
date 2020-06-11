// random color generator on page load/refresh

var colors = ["#D1DFDF", "#E2D7C3", "#F4F4F4", "#BA987C"];
var card = document.querySelectorAll("#random-bgcolor");

for (i = 0; i < card.length; i++) {
    // pick random color from array of 'colors'
    card[i].style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
};

// other random colors
// "#577F67", "#BE7C66", "#BF845C", "#DBAB61"
