// Updates the color of header element to red
// when user clicks red header button on html

$(document).ready(function () {
  // Select the div tag by ID
  const redHeaderDiv = $('DIV#red_header');
  // Add a click event handler
  redHeaderDiv.click(function () {
    // Find the header element
    const element = $('header');
    if (element) {
      // Apply style to element if found
      element.css('color', '#FF0000');
    } else {
      console.error('Header element not found');
    }
  });
});
