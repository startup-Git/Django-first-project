// sticky nav
window.addEventListener("scroll", function () {
    let fixedNav = document.querySelector(".primary_fixed");
    if(window.pageYOffset > 0){
        fixedNav.classList.add("sticky_top");
    }else{
        fixedNav.classList.remove("sticky_top");
    }
});
// sticky nav end

// slider home
let flag = 0;
function controlar(x){
    flag = flag + x;
    SlideShow(flag);
}
function SlideShow(num) {
    let Slide = document.getElementsByClassName('slider_item');
    if(num == Slide.length){
        flag = 0;
        num = 0;
    }
    if(num < 0){
        flag = Slide.length-1;
        num = Slide.length-1;
    }
    for(let y of Slide){
        y.style.display = "none";
    }
    Slide[num].style.display = "block";
}
SlideShow(flag);
// slider home end

// slider Typing text
const textDisplay = document.getElementById('text')
const phrases = [`Hello! I'm ARR.`,`Web Designer & Developer.`, `I love to code.`, `I love to teach.`];
let i = 0;
let j = 0 ;
let currentPhrase = [];
let isDeleting = false;
let isEnd = false;

function loop () {
  isEnd = false;
  textDisplay.innerHTML = currentPhrase.join('');

  if (i < phrases.length) {

    if (!isDeleting && j <= phrases[i].length) {
      currentPhrase.push(phrases[i][j]);
      j++;
      textDisplay.innerHTML = currentPhrase.join('');
    }

    if(isDeleting && j <= phrases[i].length) {
      currentPhrase.pop(phrases[i][j]);
      j--;
      textDisplay.innerHTML = currentPhrase.join('');
    }

    if (j == phrases[i].length) {
      isEnd = true;
      isDeleting = true;
    }

    if (isDeleting && j === 0) {
      currentPhrase = [];
      isDeleting = false;
      i++;
      if (i === phrases.length) {
        i = 0;
      }
    }
  }
  const spedUp = Math.random() * (80 -50) + 50;
  const normalSpeed = Math.random() * (300 -200) + 200;
  const time = isEnd ? 2000 : isDeleting ? spedUp : normalSpeed;
  setTimeout(loop, time);
}
loop();
// slider Typing text end

// like_box
let Like_Flag = 0;
function ArrowControlar(x){
    Like_Flag = Like_Flag + x;
    Like_box(Like_Flag);
}
function Like_box(count){
    let like = document.getElementsByClassName("like_box");
    if(count == like.length){
        Like_Flag = 0;
        count = 0;
    }
    for(let m of like){
        m.style.display = "block";
    }
    like[count].style.display = "none";
}
Like_box(Like_Flag);
// like_box end

//project tabs
let tabs = 0;
function ProjectTab(evt, tabName){
  const projectItems = document.getElementsByClassName("projects_items");
  const projectButtons = document.getElementsByClassName("tabButton");

  for (let tabAll = 0; tabAll < projectItems.length; tabAll++) {
    projectItems[tabAll].style.display = "none";
    
  }
  for (let i = 0; i < projectButtons.length; i++) {
    projectButtons[i].className = projectButtons[i].className.replace(" active", "");
  }
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";
}
document.getElementById("defaultOpen").click();