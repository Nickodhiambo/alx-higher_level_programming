// Adds a 'red' class to header when user clicks a div
$(document).ready(function () {
  // Select the div by ID
  const redHeaderDiv = $('DIV#red_header');
  // Add an event handler
  redHeaderDiv.click(function () {
    // Find header element
    const element = $('header');
    if (element) {
      // Use addClass method to add 'red' class
      element.addClass('red');
    } else {
      console.error('Header element not found');
    }
  });
});
