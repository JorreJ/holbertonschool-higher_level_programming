fetch('https://swapi-api.hbtn.io/api/films/?format=json')
.then(response => response.json())
.then(data => {
    data.results.forEach(film => {
        document.getElementById("list_movies").append(Object.assign(document.createElement('li'), { textContent: film.title }));
    })
    
})
.catch(error => console.error('Erreur', error));
