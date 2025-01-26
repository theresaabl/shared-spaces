const objectKeys = document.getElementsByClassName("replace-underscore");

/**
* Remove underscores from model object keys
* 
*/
addEventListener("DOMContentLoaded", (e) => {
    for (const key of objectKeys){
        console.log(key.innerText);
        newKeyText = key.innerText.replaceAll("_", " ");
        key.innerText = newKeyText.charAt(0).toUpperCase() + newKeyText.slice(1);
    }
});