"use strict";
$(document).ready(() => {
  const emailPattern = /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}\b/;
  // const passwordPattern=/^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$/;


  $("#registration_form").submit(evt => {
    let isValid = true;

    const email = $("#email").val().trim();

    if (email == "") {
        $("#email").next().text("This field is required.");
        isValid = false;
    } else if ( !emailPattern.test(email) ) {
        $("#email").next().text("Must be a valid email address.");
        isValid = false;
    } else {
        $("#email").next().text("");
    }
    $("#email").val(email);


    const pass=$("#pass").val().trim();
     if (pass == "") {
         $("#pass").next().text("This field is required.");
         isValid = false;
     }

    // else if  (!passwordPattern.test(pass)) {
    //   $("#pass").next().text("Must be valid Password");
    //   isValid = false;
    // }
     else {
      pass.next().text("");
    }

    $("#pass").val(pass);

    if (isValid === false) {
      evt.preventDefault();
    }
  });
});
