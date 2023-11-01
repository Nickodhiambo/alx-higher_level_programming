// Alternates header between to colors

$(document).ready(function () {
  // Select DIV and header
  const toggleDiv = $('DIV#toggle_header');
  const headerElement = $('header');
  // Add a toggle event handler
  toggleDiv.click(function () {
    headerElement.toggleClass('red green');
  });
});
