/**
 * fetches and prints how to say “Hello” depending on the language
 */
$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();
    const url = `https://hellosalut.stefanbohacek.dev/?lang=${lang}`;
    $.getJSON(url, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
