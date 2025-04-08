// Mitigation Action Modal JavaScript
const saveMitigationActionButton = document.getElementById(
  "saveMitigationAction"
);
const mitigationActionForm = document.getElementById("mitigationActionForm");
const mitigationActionModal = new bootstrap.Modal(
  document.getElementById("mitigationActionModal")
);

// Get the URL for the mitigation action creation endpoint from the template
const mitigationActionCreateAjaxUrl = window.mitigationActionCreateAjaxUrl;

saveMitigationActionButton.addEventListener("click", function () {
  const formData = new FormData(mitigationActionForm);

  // Fetch API call to create a new mitigation action
  fetch(mitigationActionCreateAjaxUrl, {
    method: "POST",
    body: formData,
    headers: {
      "X-CSRFToken": formData.get("csrfmiddlewaretoken"),
    },
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      if (data.success) {
        // Add the new mitigation action to the available mitigation actions list
        const newOption = new Option(
          data.mitigation_action_description,
          data.mitigation_action_id
        );
        document.getElementById("available-mitigation-actions").add(newOption);

        // Close the modal
        mitigationActionModal.hide();
      } else {
        // Display errors
        alert(
          "Error creating mitigation action: " + JSON.stringify(data.errors)
        );
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      alert("An unexpected error occurred. Please try again.");
    });
});
