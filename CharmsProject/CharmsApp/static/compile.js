$(document).ready(function () {
  $("#btn-compile").click(function(){
    var result = [];
    var canvas = document.getElementById('block-canvas').childNodes;
    var canvasLength = canvas.length;
    for (var i = 0; i < canvasLength; i ++) {
      block = canvas[i];
      blockId = block.id;
      blockClassName = block.className;
      if (blockClassName == "block-input-output") {
        var inputOutput = block.childNodes[3];
        var value = inputOutput.value;
        var isInput = blockId.split("-")[1] == 'read';
        if(isInput) {
          result.push(`read(${value});`);
        } else {
          result.push(`print(${value});`);
        }
      } else if (blockClassName == "block-variable") {
        var variableType = blockId.split("-")[2];
        var variableInput = block.childNodes[3];
        var value = variableInput.value;
        result.push(`${variableType} ${value};`);
      } else if (blockClassName == "block-condition") {
        var conditionType = blockId.split("-")[1];
        if (conditionType == 'if') {
          var ifInput = block.childNodes[3];
          var value = ifInput.value;
          result.push(`if(${value})`);
          result.push(`{`);
        } else if (conditionType == 'else') {
          result.push(`}`);
          result.push(`else`);
          result.push(`{`);
        } else {
          result.push(`}`);
        }
      } else if (blockClassName == 'block-assignment') {
        var assignmentVariable = block.childNodes[1];
        var assignmentResult = block.childNodes[5];
        var variableValue = assignmentVariable.value;
        var resultValue = assignmentResult.value;
        result.push(`${variableValue} = ${resultValue};`);
      }
      console.log(result);
    }
  });
});
