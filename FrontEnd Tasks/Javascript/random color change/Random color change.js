doc=document;
const body=doc.querySelector("body")
const h1=doc.querySelector("h1")
function Button() {
    let red=Math.floor(Math.random()*256)
    let blue=Math.floor(Math.random()*256)
    let green=Math.floor(Math.random()*256)
    let RGBColor = "rgb(" + red + "," + blue + "," + green + ")";  
    body.style.backgroundColor=RGBColor;
} 