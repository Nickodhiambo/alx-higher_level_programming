// Select the element to apply style
const element = document.querySelector('header');

// Check if element was found
if (element) {
  // Set color
  element.style.color = 'FF000000';
} else {
  console.error('Element not found');
}
