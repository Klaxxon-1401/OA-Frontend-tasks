const doc = document;
const button = doc.querySelector("button");


function Submit() {
    const a=doc.querySelector(`input[type="lan"]`).value;
    const b=doc.querySelector(`input[type="eng"]`).value;
    const c=doc.querySelector(`input[type="mat"]`).value;
    const d=doc.querySelector(`input[type="phy"]`).value;
    const e=doc.querySelector(`input[type="chem"]`).value;
    const f=doc.querySelector(`input[type="csc"]`).value;

    A=parseInt(a)
    B=parseInt(b)
    C=parseInt(c)
    D=parseInt(d)
    E=parseInt(e)
    F=parseInt(f)

    const Total= A+B+C+D+E+F
    const AVG=Total/5
    console.log("Your Total is",Total)
    console.log("Your Average is",AVG)
}