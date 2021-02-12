const messageStatus = document.getElementById('message_status');

function sendMail(contactForm) {
    emailjs.send("service_5x8dw5r", "contact_form", {
            "full_name": contactForm.name.value,
            "email_address": contactForm.email.value,
            "message": contactForm.message.value
        })
        .then(
            //Change button text to confirm feedback has been sent
            function (response) {
                messageStatus.innerHTML = `Thanks For Contacting Us <i class="far fa-grin-beam"></i>`;
            },
            //If feedback fails to send, change button text to ask user to try again
            function (error) {
                messageStatus.innerHTML = `Message Failed to Send. Please Try Again!`;
            }
        );
    //Resets form after submission
    document.getElementById('contact_form').reset();
    return false;
}