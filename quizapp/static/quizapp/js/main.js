document.addEventListener("DOMContentLoaded", function() {
    // Get the clear button and forms
    const clearButton = document.getElementById('clearBtn');
    const loginForm = document.getElementById('loginForm');
    const registerForm = document.getElementById('registerForm');

    // Function to clear form fields and error messages
    function clearForm() {
        if (loginForm) {
            loginForm.reset(); // Reset the form fields
            document.getElementById('id_username').value = ''; // Explicitly clear the username field
            removeErrorMessages(); // Remove error messages
        }

        if (registerForm) {
            registerForm.reset(); // Reset the form fields
            document.getElementById('id_username').value = ''; // Explicitly clear the username field
            document.getElementById('id_email').value = ''; // Explicitly clear the email field if necessary
            removeErrorMessages(); // Remove error messages
        }
    }

    // Function to remove error messages
    function removeErrorMessages() {
        const errorAlerts = document.querySelectorAll('.alert-danger');
        errorAlerts.forEach(alert => alert.remove());
    }

    // Function to automatically clear alerts after a set time
    function autoClearAlerts() {
        const alerts = document.querySelectorAll('.alert');
        alerts.forEach(alert => {
            setTimeout(() => {
                alert.classList.add('fade');
                setTimeout(() => {
                    alert.remove();
                }, 500);
            }, 3000); // Adjust the time here (3000ms = 3 seconds)
        });
    }

    // Attach event listener to clear button
    if (clearButton) {
        clearButton.addEventListener('click', clearForm);
    }

    // Clear the form fields on page refresh, including the username field
    window.addEventListener('load', function () {
        if (loginForm) {
            loginForm.reset(); // Reset the form fields
            document.getElementById('id_username').value = ''; // Explicitly clear the username field
        }

        if (registerForm) {
            registerForm.reset(); // Reset the form fields
            document.getElementById('id_username').value = ''; // Explicitly clear the username field
            document.getElementById('id_email').value = ''; // Explicitly clear the email field if necessary
        }

        autoClearAlerts(); // Automatically clear alerts on page load
    });
});
