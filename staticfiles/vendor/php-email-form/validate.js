// Get the form element
const form = document.querySelector('.contact-form');

// Get the sent-message and error-message elements
const sentMessage = document.querySelector('.sent-message');
const errorMessage = document.querySelector('.error-message');

// Add a submit event listener to the form
form.addEventListener('submit', async (event) => {
  // Prevent the default form submission
  event.preventDefault();
  
  // Send a POST request to the server
  try {
    const response = await fetch(event.target.action, {
      method: 'POST',
      body: new FormData(event.target),
    });

    // Check if the request was successful
    if (response.ok) {
      // Show the success message and hide the form
      sentMessage.style.display = 'block';
      form.style.display = 'none';
    } else {
      // Show the error message
      errorMessage.style.display = 'block';
    }
  } catch (error) {
    // Show the error message
    errorMessage.style.display = 'block';
  }
});
