// Wait for the DOM to fully load before executing the script
document.addEventListener("DOMContentLoaded", function () {
  // ==========================
  // Asset Management Section
  // ==========================

  // Get references to the buttons and select elements for managing assets
  const addAssetButton = document.getElementById("add-asset"); // Button to add selected assets
  const removeAssetButton = document.getElementById("remove-asset"); // Button to remove selected assets
  const availableAssetsSelect = document.getElementById("available-assets"); // Select element for available assets
  const associatedAssetsSelect = document.getElementById("associated-assets"); // Select element for associated assets

  // Event listener for adding selected assets from "Available Assets" to "Associated Assets"
  addAssetButton.addEventListener("click", function () {
    // Loop through all selected options in the "Available Assets" list
    Array.from(availableAssetsSelect.selectedOptions).forEach((option) => {
      // Add the selected option to the "Associated Assets" list
      associatedAssetsSelect.add(
        new Option(option.text, option.value, false, true)
      );
      // Remove the selected option from the "Available Assets" list
      option.remove();
    });
  });

  // Event listener for removing selected assets from "Associated Assets" to "Available Assets"
  removeAssetButton.addEventListener("click", function () {
    // Loop through all selected options in the "Associated Assets" list
    Array.from(associatedAssetsSelect.selectedOptions).forEach((option) => {
      // Add the selected option back to the "Available Assets" list
      availableAssetsSelect.add(new Option(option.text, option.value));
      // Remove the selected option from the "Associated Assets" list
      option.remove();
    });
  });

  // Reset the Asset Modal Form when the modal is shown
  const assetModal = document.getElementById("assetModal"); // Reference to the Asset Modal
  assetModal.addEventListener("show.bs.modal", function () {
    const assetForm = document.getElementById("assetForm"); // Reference to the Asset Form inside the modal
    assetForm.reset(); // Reset all form fields to their default values

    // Clear the readonly "asset_id" field specifically
    const assetIdField = assetForm.querySelector('[name="asset_id"]');
    if (assetIdField) {
      assetIdField.value = ""; // Clear the value of the "asset_id" field
    }
  });

  // Save the Asset when the "Save" button in the modal is clicked
  const saveAssetButton = document.getElementById("saveAsset"); // Reference to the "Save" button
  const assetForm = document.getElementById("assetForm"); // Reference to the Asset Form
  const assetModalInstance = new bootstrap.Modal(assetModal); // Bootstrap modal instance for the Asset Modal

  saveAssetButton.addEventListener("click", function () {
    const formData = new FormData(assetForm); // Collect form data for submission

    // Send the form data to the server using a POST request
    fetch("{% url 'asset_create_ajax' %}", {
      method: "POST",
      body: formData,
      headers: {
        "X-CSRFToken": formData.get("csrfmiddlewaretoken"), // Include CSRF token for security
      },
    })
      .then((response) => response.json()) // Parse the JSON response
      .then((data) => {
        if (data.success) {
          // If the asset is successfully created, add it to the "Available Assets" list
          const newOption = new Option(data.asset_name, data.asset_id);
          document.getElementById("available-assets").add(newOption);

          // Close the modal
          assetModalInstance.hide();
        } else {
          // Display errors if the asset creation fails
          alert("Error creating asset: " + data.errors);
        }
      });
  });

  // ==========================
  // Control Management Section
  // ==========================

  // Get references to the buttons and select elements for managing controls
  const addControlButton = document.getElementById("add-control"); // Button to add selected controls
  const removeControlButton = document.getElementById("remove-control"); // Button to remove selected controls
  const availableControlsSelect = document.getElementById("available-controls"); // Select element for available controls
  const associatedControlsSelect = document.getElementById("associated-controls"); // Select element for associated controls

  // Event listener for adding selected controls from "Available Controls" to "Associated Controls"
  addControlButton.addEventListener("click", function () {
    // Loop through all selected options in the "Available Controls" list
    Array.from(availableControlsSelect.selectedOptions).forEach((option) => {
      // Add the selected option to the "Associated Controls" list
      associatedControlsSelect.add(
        new Option(option.text, option.value, false, true)
      );
      // Remove the selected option from the "Available Controls" list
      option.remove();
    });
  });

  // Event listener for removing selected controls from "Associated Controls" to "Available Controls"
  removeControlButton.addEventListener("click", function () {
    // Loop through all selected options in the "Associated Controls" list
    Array.from(associatedControlsSelect.selectedOptions).forEach((option) => {
      // Add the selected option back to the "Available Controls" list
      availableControlsSelect.add(new Option(option.text, option.value));
      // Remove the selected option from the "Associated Controls" list
      option.remove();
    });
  });

  // ==========================
  // Mitigation Action Management Section
  // ==========================

  // Get references to the buttons and select elements for managing mitigation actions
  const addMitigationActionButton = document.getElementById(
    "add-mitigation-action"
  ); // Button to add selected mitigation actions
  const removeMitigationActionButton = document.getElementById(
    "remove-mitigation-action"
  ); // Button to remove selected mitigation actions
  const availableMitigationActionsSelect = document.getElementById(
    "available-mitigation-actions"
  ); // Select element for available mitigation actions
  const associatedMitigationActionsSelect = document.getElementById(
    "associated-mitigation-actions"
  ); // Select element for associated mitigation actions

  // Event listener for adding selected mitigation actions from "Available Mitigation Actions" to "Associated Mitigation Actions"
  addMitigationActionButton.addEventListener("click", function () {
    // Loop through all selected options in the "Available Mitigation Actions" list
    Array.from(availableMitigationActionsSelect.selectedOptions).forEach(
      (option) => {
        // Add the selected option to the "Associated Mitigation Actions" list
        associatedMitigationActionsSelect.add(
          new Option(option.text, option.value, false, true)
        );
        // Remove the selected option from the "Available Mitigation Actions" list
        option.remove();
      }
    );
  });

  // Event listener for removing selected mitigation actions from "Associated Mitigation Actions" to "Available Mitigation Actions"
  removeMitigationActionButton.addEventListener("click", function () {
    // Loop through all selected options in the "Associated Mitigation Actions" list
    Array.from(associatedMitigationActionsSelect.selectedOptions).forEach(
      (option) => {
        // Add the selected option back to the "Available Mitigation Actions" list
        availableMitigationActionsSelect.add(
          new Option(option.text, option.value)
        );
        // Remove the selected option from the "Associated Mitigation Actions" list
        option.remove();
      }
    );
  });
});
