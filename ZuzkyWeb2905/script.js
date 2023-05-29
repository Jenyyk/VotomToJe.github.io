// script pro index.html

let menuState = 0

function menuFnc() {
  if (menuState == 0) {
    document.getElementById("bgBlur").style.visibility = "visible";
    document.getElementById("bgBlur").style.opacity = "1";
    document.getElementById("sidebar").style.left = "calc(100% - 300px)"
    menuState = 1;
    console.log("blurring")
  } else {
    document.getElementById("bgBlur").style.visibility = "hidden";
    document.getElementById("bgBlur").style.opacity = "0";
    document.getElementById("sidebar").style.left = "100%"
    menuState = 0;
    console.log("clearing")
  }
  console.log("ende")
}
// otevře a zavře postranní meníčko
// zviditelní a zneviditelní zatmavení při otevření postranního meníčka
