const messageStatus = document.getElementById('message_status');

function sendMail(contactForm) {
    emailjs.send("service_5x8dw5r", "contact_form", {
            "full_name": contactForm.full_name.value,
            "email_address": contactForm.email.value,
            "message": contactForm.message.value
        })
        .then(
            //Change button text to confirm feedback has been sent
            function (response) {
                messageStatus.innerHTML = `<p class="message-status">Thanks For Contacting Us <i class="far fa-grin-beam"></i></p>`;
            },
            //If feedback fails to send, change button text to ask user to try again
            function (error) {
                messageStatus.innerHTML = `<p class="message-status">Message Failed to Send. Please Try Again!</p>`;
            }
        );
    //Resets form after submission
    document.getElementById('contact_form').reset();
    return false;
}