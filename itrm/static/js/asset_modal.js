// ==========================
// Asset Modal JavaScript
// ==========================

// Get a reference to the "Save Asset" button in the modal
// This button is used to trigger the form submission when clicked
const saveAssetButton = document.getElementById("saveAsset");

// Get a reference to the asset form inside the modal
// This form contains the fields for creating a new asset
const assetForm = document.getElementById("assetForm");

// Create a Bootstrap modal instance for the Asset Modal
// This allows programmatic control over the modal, such as opening or closing it
const assetModal = new bootstrap.Modal(document.getElementById("assetModal"));

// Add an event listener to the "Save Asset" button
// This function will execute when the "Save Asset" button is clicked
saveAssetButton.addEventListener("click", function () {
  // Create a FormData object from the asset form
  // This object collects all the form fields and their values for submission
  const formData = new FormData(assetForm);

  // Send the form data to the server using the Fetch API
  fetch("{% url 'asset_create_ajax' %}", {
    // Specify the HTTP method as POST, which is used to create a new asset
    method: "POST",
    // Attach the form data to the request body
    body: formData,
    // Include the CSRF token in the request headers for security
    headers: {
      "X-CSRFToken": formData.get("csrfmiddlewaretoken"), // Extract CSRF token from the form
    },
  })
    // Parse the server's response as JSON
    .then((response) => response.json())
    .then((data) => {
      // Check if the server indicates that the asset was successfully created
      if (data.success) {
        // If successful, create a new <option> element for the asset
        const newOption = new Option(data.asset_name, data.asset_id);

        // Add the new <option> to the "Available Assets" dropdown list
        document.getElementById("available-assets").add(newOption);

        // Close the modal programmatically using the Bootstrap modal instance
        assetModal.hide();
      } else {
        // If there are errors, display them in an alert box
        // Note: This is a basic implementation; consider improving error handling
        alert("Error creating asset: " + data.errors);

        // If there are validation errors, display them in the modal
        if (data.errors) {
          // Get a reference to the error container in the form
          const errorContainer = document.getElementById("assetFormErrors");

          // Clear any previous errors displayed in the container
          errorContainer.innerHTML = "";

          // Loop through the errors returned by the server
          for (const [field, messages] of Object.entries(data.errors)) {
            // Create a new <p> element for each error message
            const errorMessage = document.createElement("p");

            // Set the text content of the <p> element to the error message
            errorMessage.textContent = `${field}: ${messages.join(", ")}`;

            // Append the error message to the error container
            errorContainer.appendChild(errorMessage);
          }
        }
      }
    })
    .catch((error) => {
      // Catch any unexpected errors, such as network issues or server errors
      console.error("Error:", error); // Log the error to the console for debugging
      alert("An unexpected error occurred. Please try again."); // Display a generic error message to the user
    });
});
