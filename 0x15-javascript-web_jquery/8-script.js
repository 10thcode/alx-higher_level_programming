/**
 * fetches and lists the title for all movies from a URL
 */
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.getJSON(url, function (data) {
  for (const movie of data.results) {
    $('UL#list_movies').append(`<LI>${movie.title}</LI>`);
  }
});
