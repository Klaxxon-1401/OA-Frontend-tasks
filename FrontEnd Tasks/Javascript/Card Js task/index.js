const doc = document;
const database = [
    {
        "name": "John Doe",
        "address": "123 Main Street, Cityville, State, 12345"
    },
    {
        "name": "Jane Smith",
        "address": "456 Oak Avenue, Townsville, State, 56789"
    },
    {
        "name": "Bob Johnson",
        "address": "789 Pine Road, Villagetown, State, 98765"
    },
    {
        "name": "Emily Davis",
        "address": "321 Maple Lane, Hamletville, State, 54321"
    },
    {
        "name": "Michael Wilson",
        "address": "555 Cedar Street, Suburbia, State, 13579"
    },
    {
        "name": "Sara Miller",
        "address": "876 Birch Court, Countryside, State, 24680"
    },
    {
        "name": "Chris Taylor",
        "address": "999 Elm Avenue, Metropolis, State, 86420"
    },
    {
        "name": "Alex Turner",
        "address": "234 Oakwood Drive, Riverside, State, 97531"
    },
    {
        "name": "Laura White",
        "address": "678 Walnut Street, Uptown, State, 31415"
    },
    {
        "name": "Laura White",
        "address": "678 Walnut Street, Uptown, State, 31415"
    },
    {
        "name": "Kevin Brown",
        "address": "111 Pinecrest Road, Downtown, State, 61724"
    }

]


function createObject(name, designation) {
    return {
        "name": name,
        "address": designation
    };
}


function submit() {
    const name = doc.querySelector("#name").value;
    const designation = doc.querySelector("#designation").value;
    const newObject = createObject(name, designation);
    database.push(newObject);
    render(database);
    console.log(database);
}

// function newCardComponent1(name, designation) {
//     const card = doc.createElement("main");
//     card.classList.add("new-card");
//     card.innerHTML = `<h1>Name : ${name}</h1>
//     <h2>Designation : ${designation}</h2>`
//     return card;
// }

function newCardComponent(name, address) {
    const card = doc.createElement("main");
    card.classList.add("card-section");
    card.innerHTML = `<h1>Name : ${name}</h1>
    <h2>Address : ${address}</h2>`
    return card;
}

const row = doc.querySelector(".row");


// It loops your UI based on your data

function render(dataLayer) {
    dataLayer.map((data) => {
        const newCard = newCardComponent(data.name, data.address);
        row.appendChild(newCard);
    })
}

render(database)