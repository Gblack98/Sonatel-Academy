const API_KEY = '04c35731a5ee918f014970082a0088b1';
const API_URL = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=04c35731a5ee918f014970082a0088b1&page=1";
const POSTER_URL = 'https://image.tmdb.org/t/p/w1280';
const searchInput = document.getElementById('searchInput');
const moviesContainer = document.getElementById('moviesContainer');

// Récupère les films les plus populaires
function fetchMovies() {
  fetch(`${API_URL}/discover/movie?sort_by=popularity.desc&api_key=${API_KEY}`)
    .then(response => response.json())
    .then(data => {
      moviesContainer.innerHTML = '';
      data.results.forEach(movie => {
        const movieCard = createMovieCard(movie);
        moviesContainer.appendChild(movieCard);
      });
    })
    .catch(error => console.error('Erreur lors de la récupération des données de film:', error));
}
function debounce(func, wait, immediate) {
  let timeout;
  return function() {
    const context = this, args = arguments;
    const later = function() {
      timeout = null;
      if (!immediate) func.apply(context, args);
    };
    const callNow = immediate && !timeout;
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
    if (callNow) func.apply(context, args);
  };
}


// Effectue une recherche de films
const searchMoviesDebounced = debounce((query) => {
  fetch(`${API_URL}/search/movie?api_key=${API_KEY}&query=${query}`)
    .then(response => response.json())
    .then(data => {
      moviesContainer.innerHTML = '';
      data.results.forEach(movie => {
        const movieCard = createMovieCard(movie);
        moviesContainer.appendChild(movieCard);
      });
    })
    .catch(error => console.error('Erreur lors de la recherche de films:', error));
}, 500);


// Crée une carte de film à partir des données de film
function createMovieCard(movie) {
  const movieCard = document.createElement('div');
  movieCard.classList.add('movie-card');

  const movieTitle = document.createElement('h2');
  movieTitle.classList.add('movie-title');
  movieTitle.textContent = movie.title;
  movieCard.appendChild(movieTitle);

  const moviePoster = document.createElement('img');
  moviePoster.classList.add('movie-poster');
  moviePoster.src = `${POSTER_URL}${movie.poster_path}`;
  moviePoster.alt = movie.title;
  movieCard.appendChild(moviePoster);

  const movieOverview = document.createElement('h3');
  movieOverview.classList.add('movie-overview', 'description');
  movieOverview.textContent = movie.overview;
  movieCard.appendChild(movieOverview);

  return movieCard;
}

fetchMovies(); // afficher les films les plus populaires par défaut

searchInput.addEventListener('keyup', e => {
  const query = e.target.value.trim();
  if (query) {
    searchMoviesDebounced(query);
  } else {
    fetchMovies();
  }
});
const searchForm = document.querySelector('form');
searchForm.addEventListener('submit', e => {
  e.preventDefault();
  const query = searchInput.value.trim();
  if (query) {
    searchMovies(query);
  } else {
    fetchMovies();
  }
});



    // script pour faire apparaître la description au survol de la souris
    const movies = document.querySelector('.movie-card');
    movies.forEach(movie => {
      const description = movie.querySelector('.movie-overview');
      description.style.display = 'none';
      movie.addEventListener('mouseover', () => {
        description.style.display = 'block';
      });
      movie.addEventListener('mouseout', () => {
        description.style.display = 'none';
      });
    });

