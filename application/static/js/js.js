"use strict";
$(document).ready(() => {

  $("#uplode").submit(evt => {
    let isValid = true;

    const file = $("#file").val().trim();

    if (file == "") {
        $("#file").next().text("This field is required.");
        isValid = false;
 
    } else {
        $("#file").next().text("");
    }
    $("#file").val(file);


    const comment=$("#comment").val().trim();
     if (comment == "") {
         $("#comment").next().text("This field is required.");
         isValid = false;
     }

    else {
        $("#pass").next().text("");
    }

    $("#pass").val(pass);

    if (isValid === false) {
      evt.preventDefault();
    }
  });
});
