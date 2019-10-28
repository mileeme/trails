// random color generator on page load/refresh

var colors = ["#577F67","#D1DFDF","#BE7C66", "#BA987C", "#E2D7C3", "#BF845C", "#F4F4F4", "#DBAB61"];
var card = document.querySelectorAll("#random-bgcolor");

for (i = 0; i < card.length; i++) {
    // pick random color from array of 'colors'
    card[i].style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
};
