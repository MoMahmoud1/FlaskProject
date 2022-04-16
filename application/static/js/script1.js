"use strict";
$(document).ready(() => {

  $("#uplode_form").submit(evt => {
    let isValid = true;

    const ingredients = $("#ingredients").val();

    if (ingredients == "") {
        $("#ingredients").next().text("This field is required.");
        isValid = false;
    } else {
        $("#ingredients").next().text("");
    }
    $("#ingredients").val(ingredients);

    const instructions = $("#instructions").val();

    if (instructions == "") {
        $("#instructions").next().text("This field is required.");
        isValid = false;
    } else {
        $("#instructions").next().text("");
    }
    $("#instructions").val(instructions);

    const servings= $("#servings").val();

    if (ingredients == "") {
        $("#servings").next().text("This field is required.");
        isValid = false;
    } else {
        $("#servings").next().text("");
    }
    $("#servings").val(servings);

    if (isValid === false) {
      evt.preventDefault();
    }
  });
});
