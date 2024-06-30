$(document).ready(function () {

    $("#form").submit(function (event) {
        event.preventDefault();
        handleSubmission();
    });
});

/**
 * Handles form submission via AJAX and displays messages based on server response.
 */
function handleSubmission() {
    const formData = $("#form").serialize();
    $("#message-container").removeClass('alert-success alert-danger').html('').hide();

    $.ajax({
        url: "/registration",
        type: "POST",
        data: formData,
        success: function (response) {
            let alertClass = response.status ? 'alert-success' : 'alert-danger';
            let messageDiv = `<div class='alert ${alertClass} alert-dismissible'>
                                  <a href='#' class='close' data-dismiss='alert' aria-label='close'>&times;</a>
                                  ${response.message}
                              </div>`;
            
            $("#message-container").html(messageDiv).show();

            if (response.status) {
                setTimeout(function () {
                    window.location.href = response.redirect;
                }, 2000); // Redirect after 2 seconds if success
            }
        },
        error: function () {
            let errorMessageDiv = `<div class='alert alert-danger alert-dismissible'>
                                      <a href='#' class='close' data-dismiss='alert' aria-label='close'>&times;</a>
                                      An error occurred.
                                  </div>`;
            
            $("#message-container").html(errorMessageDiv).show();
        }
    });
}

