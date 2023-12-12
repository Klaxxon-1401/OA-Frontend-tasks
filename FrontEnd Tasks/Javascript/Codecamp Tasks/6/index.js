const doc=document;
let button1=doc.querySelector(".button");
var main=doc.querySelector(".main");
let body=doc.querySelector("body")
let html=doc.querySelector("html")

let div=doc.querySelector("#div")

button1.addEventListener("click",() => {
    body.classList.toggle("body2");
    main.classList.toggle("shadow");
    div.classList.toggle("Dnone");
    html.classList.toggle("shadow");
    document.body.classList.add('has-shadow');

})