$(document).ready(function () {
    
    // Code is from Materialize Documentation for initializing JavaScript components:
    // https://materializecss.com/

    // Initialise Sidenav Trigger
    $('.sidenav').sidenav({
        edge: "right"
    });

    // Form Input Character Count
    $('input#first_name, input#username, input#password, input#confirm_password').characterCounter();

    // Dictionary Collapsible
    $('.collapsible').collapsible();

    // Delete Confirmation Modal
    $('.modal').modal();

    // Sort By Dropdown
    $('.dropdown-trigger').dropdown();

    // Code is from Stack Overflow for confirm Password:
    // https://stackoverflow.com/questions/21727317/how-to-check-confirm-password-field-in-form-without-reloading-page
    $('#password, #confirm_password').on('keyup', function () {
        if ($('#password').val() == $('#confirm_password').val()) {
            $('#message').html('Passwords Match').css('color', 'green');
        } else
            $('#message').html('Passwords Do Not Match').css('color', 'red');
    });
});