// Mitigation Action Modal JavaScript
const saveMitigationActionButton = document.getElementById(
  "saveMitigationAction"
);
const mitigationActionForm = document.getElementById("mitigationActionForm");
const mitigationActionModal = new bootstrap.Modal(
  document.getElementById("mitigationActionModal")
);

saveMitigationActionButton.addEventListener("click", function () {
  const formData = new FormData(mitigationActionForm);

  fetch("{% url 'mitigationaction_create_ajax' %}", {
    // Ensure this URL matches the backend endpoint
    method: "POST",
    body: formData,
    headers: {
      "X-CSRFToken": formData.get("csrfmiddlewaretoken"),
    },
  })
    .then((response) => response.json())
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
      alert("An unexpected error occurred.");
    });
});
