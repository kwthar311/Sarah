// Check If There's Local Storage Color Option
let mainColors = localStorage.getItem("color-option");

if (mainColors !== null){
    document.documentElement.style.setProperty("--main-color", mainColors);

    // Check For Active Class
    document.querySelectorAll(".colors-list li").forEach(e => {
        e.classList.remove("active");
        // Add Active Class On Element With Data Color === Local Storage Color (mainColors)
        if (e.dataset.color === mainColors){
            e.classList.add("active");
        }
    });
}



// Toggle Spin Class On Icon
document.querySelector(".toggle-settings .fa-gear").onclick = function () {
    // Toggle Class Fa-spin For Rotation on Self
    this.classList.toggle("fa-spin");
    // Toggle Class Open On Main Settings Box
    document.querySelector(".settings-box").classList.toggle("open");
};


// Switch Colors settings
const colorsLi = document.querySelectorAll(".colors-list li");


// Loop On All List Items
colorsLi.forEach(li => {

    // Click On Every List Items
    li.addEventListener("click", (e) =>{

        // Set Color On Root
        document.documentElement.style.setProperty('--main-color', e.target.dataset.color);
        // Set Color On Local Storage
        localStorage.setItem("color-option", e.target.dataset.color);
        // Remove Active Class From All Childrens
        e.target.parentElement.querySelectorAll(".active").forEach(element => {
            element.classList.remove("active");
        });
        // Add Active Class To The Clicked Color
        e.target.classList.add("active");
    });
});



/*******  Images Rounding *********/
// Select Landing Page Element
let landingPage = document.querySelector('.landing-page');
// Get Array Of Imgs
let imgsArray = ["01.jpg", "02.jpg", "03.jpg", "04.jpeg", "05.jpeg", "06.jpeg", "07.jpeg"];
setInterval(() => {
// Get Random Number
let randomIndex = Math.floor(Math.random() * imgsArray.length);
// Changing Background Image URL
landingPage.style.backgroundImage = 'url("/static/imgs/'+ imgsArray[randomIndex] +'")';

}, 8000);








