$(document).ready(function () {
  $("#itWorks").click(function(){
    spellName = document.getElementById("spell-name").textContent;
    if (spellName != "") {
      $("#output-title").text("Well done Wizard!");
      $("#output-message").text(getSuccesMessage());
    }
  });
  $("#itDoesntWork").click(function(){
    spellName = document.getElementById("spell-name").textContent;
    if (spellName != "") {
      $("#output-title").text("Almost there Wizard...");
      $("#output-message").text(getErrorMessage());
    }
  });

  function getSuccesMessage() {
    spellName = document.getElementById("spell-name").textContent;
    if (spellName == 'Levitation') {
      return "You've managed to elevate the object correctly. Thanks to you, your house has earned 100 points."
    } else {
      return "You've managed to perform the Freezing spell correctly. Thanks to you, your house has earned 200 points."
    }
  }

  function getErrorMessage() {
    return "It looks like you're missing something. Read the instructions and run your code again."
  }
});
