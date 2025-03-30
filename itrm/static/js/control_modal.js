// Control Modal JavaScript
const saveControlButton = document.getElementById("saveControl");
const controlForm = document.getElementById("controlForm");
const controlModal = new bootstrap.Modal(
  document.getElementById("controlModal")
);

saveControlButton.addEventListener("click", function () {
  const formData = new FormData(controlForm);

  fetch("{% url 'control_create_ajax' %}", {
    // ToDo: Create new url control_create_ajax
    method: "POST",
    body: formData,
    headers: {
      "X-CSRFToken": formData.get("csrfmiddlewaretoken"),
    },
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        // Add the new control to the available controls list
        const newOption = new Option(data.control_name, data.control_id);
        document.getElementById("available-controls").add(newOption);

        // Close the modal
        controlModal.hide();
      } else {
        // Display errors (you'll need to handle this better in a real application)
        alert("Error creating control: " + data.errors);
      }
    });
});
