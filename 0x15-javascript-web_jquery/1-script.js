// Apply JQuery
$(document).ready(function () {
  // Use JQuery selector
  const element = $('header');
  // Check if header element was found
  if (element) {
    // Use css to set color
    element.css('color', '#FF0000');
  } else {
    console.error('Element not found');
  }
});
