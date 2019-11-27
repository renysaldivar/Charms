$(document).ready(function () {
  var spellName = "";

  $("#dropdown-spell").on('change', function() {
    if ($(this).val() == '') {
      spellName = "";
      $("#spell-name").text(spellName);
      hideSpellDescription();
      hideSpellTodo();
    } else if ($(this).val() == 'levitation') {
      spellName = "Levitation";
      $("#spell-name").text(spellName);
      showSpellDescription();
      hideSpellTodo();
    } else {
      spellName = "Freezing";
      $("#spell-name").text(spellName);
      showSpellDescription();
      hideSpellTodo();
    }
  });

  $("#left-button").click(function(){
    if (spellName != "") {
      showSpellDescription();
      hideSpellTodo();
    }
  });

  $("#right-button").click(function(){
    if (spellName != "") {
      hideSpellDescription();
      showSpellTodo();
    }
  });

  function showSpellDescription() {
    document.getElementById("spell-description").style.display = "block";
    $("#description-label").text(getDescriptionText());
  }

  function hideSpellDescription() {
    document.getElementById("spell-description").style.display = "none";
  }

  function showSpellTodo() {
    document.getElementById("spell-todo").style.display = "block";
    $("#todo-label").text(getTodoText());
  }

  function hideSpellTodo() {
    document.getElementById("spell-todo").style.display = "none";
  }

  function getDescriptionText() {
    if (spellName == "Levitation") {
      return "There is not better way to test your magical skills, than trying to do this spell. The Levitation charm is used to make any object fly, or levitate."
    } else {
      return "If you ever want to immobilize any target, this is the spell you want to try. The Freezing charm can stop the actions of any object or living thing."
    }
  }

  function getTodoText() {
    if (spellName == "Levitation") {
      return "Create a function called Levitation that receives an int variable called height as a parameter. This function should return the height times 2."
    } else {
      return "Create a function called Freeze that receives a bool variable called dangerousMagicalCreature as a parameter. If the variable is equal to true, print the following statement: 'Immobulus'. On the other hand, if the variable is equal to false, print the following: 'Stop'."
    }
  }
});
