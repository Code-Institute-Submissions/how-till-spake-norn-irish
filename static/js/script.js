// Code is from Materialize Documentation for initializing JavaScript components:
// https://materializecss.com/

$(document).ready(function () {
    // Initialise Sidenav Trigger
    $('.sidenav').sidenav({
        edge: "right"
    });

    // Form Input Character Count
    $('input#first_name, input#username, input#password').characterCounter();

    // Dictionary Collapsible
    $('.collapsible').collapsible();

    //Delete Confirmation Modal
    $('.modal').modal();

    //Sort By Dropdown
    $('.dropdown-trigger').dropdown();
});