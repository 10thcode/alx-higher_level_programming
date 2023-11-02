/**
 * adds a <li> element to a list
 */
$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});
