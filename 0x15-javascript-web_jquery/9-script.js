/**
 * fetches and display info from a URL
 */
const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$(document).ready(function () {
  $.getJSON(url, function (data) {
    $('DIV#hello').text(`${data.hello}`);
  });
});
