$(document).ready(function () {
    // Initialise Sidenav Trigger
    $('.sidenav').sidenav({
        edge: "right"
    });
    // Form Input Character Count
    $('input#first_name, input#username, input#password').characterCounter();
    // Collapsible
    $('.collapsible').collapsible();
    //Modal
    $('.modal').modal();
});