const WINX_API = {
    SERVICE_URL: "https://api.tvmaze.com",
    WinxClub: "/shows/5883",
    WorldOfWinx: "/shows/22651",
    FateTheWinxSaga: "/shows/43917"
}

let selectInfo = document.getElementById('info-type');

document.addEventListener('DOMContentLoaded', () => {
    const defaultOption = selectInfo.value;
    loadData(defaultOption);
});

selectInfo.addEventListener('change', event => {
    loadData(event.target.value)
});

function loadData(infoType) {
    let url = WINX_API.SERVICE_URL + WINX_API[infoType];
    fetch(url)
      .then((response) => response.json())
      .then((json) => {
        let title = document.getElementById('moreInfoTitle');
        title.textContent = json.name;

        let img = document.getElementById('moreInfoImg');
        img.src = json.image ? json.image.medium : '';
        img.alt = json.name;

        let descripcion = document.getElementById('moreInfoDescripcion');
        descripcion.textContent = json.summary ? json.summary.replace(/<\/?[^>]+(>|$)/g, "") : 'Description no disponible.';

        let generos = document.getElementById('moreInfoGeneros');
        generos.innerHTML = '';
        if (json.genres && json.genres.length > 0) {
            json.genres.forEach((genre) => {
            let li = document.createElement('li');
            li.textContent = genre;
            generos.appendChild(li);
        });
        } else {
            let li = document.createElement('li');
            li.textContent = 'No genres available.';
            generos.appendChild(li);
        }
    });
}
