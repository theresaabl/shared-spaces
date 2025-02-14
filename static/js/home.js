/**
* Dynamically set margin-bottom of hero section, depending on height of cover text
*/

addEventListener("DOMContentLoaded", (e) => {

    const coverTextHeight = document.getElementById("cover-text").offsetHeight;
    document.getElementById("hero-section").style.marginBottom = (coverTextHeight * 0.6).toString() + "px";

    // set hero-section margin-bottom each time window resized
    window.addEventListener("resize", (e) => {
        const newCoverTextHeight = document.getElementById("cover-text").offsetHeight;
        document.getElementById("hero-section").style.marginBottom = (newCoverTextHeight * 0.6).toString() + "px";
    });

});