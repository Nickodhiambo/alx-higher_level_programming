// Adds a list item to an unordered list
$('DIV#add_item').click(() => {
  $('UL.my_list').append('<li>item</li>');
});
