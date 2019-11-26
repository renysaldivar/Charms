var blockCountRead = 0;
var blockCountPrint = 0;
var blockCountVarInt = 0;
var blockCountVarBool = 0;
var blockCountVarChar = 0;
var blockCountIf = 0;
var blockCountElse = 0;
var blockCountEndCondition = 0;
var blockCountWhile = 0;
var blockCountEndLoop = 0;
var blockCountFunction = 0;
var blockCountStartParameters = 0;
var blockCountParameter = 0;
var blockCountEndParameters = 0;
var blockCountEndFunction = 0;
var blockCountReturn = 0;
var blockCountCall = 0;
var blockCountAssignment = 0;

function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("block", ev.target.id);
}

function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("block");
    var newBlock = document.getElementById(data).cloneNode(true);

    // Creates new id for every new block added to the canvas
    switch(data) {
        case 'block-read':
            newBlock.id = data + "-" + blockCountRead;
            blockCountRead += 1;
            break;
        case 'block-print':
            newBlock.id = data + "-" + blockCountPrint;
            blockCountPrint += 1;
            break;
        case 'block-variable-int':
            newBlock.id = data + "-" + blockCountVarInt;
            blockCountVarInt += 1;
            break;
        case 'block-variable-bool':
            newBlock.id = data + "-" + blockCountVarBool;
            blockCountVarBool += 1;
            break;
        case 'block-variable-char':
            newBlock.id = data + "-" + blockCountVarChar;
            blockCountVarChar += 1;
            break;
        case 'block-if':
            newBlock.id = data + "-" + blockCountIf;
            blockCountIf += 1;
            break;
        case 'block-else':
            newBlock.id = data + "-" + blockCountElse;
            blockCountElse += 1;
            break;
        case 'block-end-condition':
            newBlock.id = data + "-" + blockCountEndCondition;
            blockCountEndCondition += 1;
            break;
        case 'block-while':
            newBlock.id = data + "-" + blockCountWhile;
            blockCountWhile += 1;
            break;
        case 'block-end-while':
            newBlock.id = data + "-" + blockCountEndLoop;
            blockCountEndLoop += 1;
            break;
        case 'block-function':
            newBlock.id = data + "-" + blockCountFunction;
            blockCountFunction += 1;
            break;
        case 'block-startp-parameters':
            newBlock.id = data + "-" + blockCountStartParameters;
            blockCountStartParameters += 1;
            break;
        case 'block-parameter':
            newBlock.id = data + "-" + blockCountParameter;
            blockCountParameter += 1;
            break;
        case 'block-endp-parameters':
            newBlock.id = data + "-" + blockCountEndParameters;
            blockCountEndParameters += 1;
            break;
        case 'block-end-function':
            newBlock.id = data + "-" + blockCountEndFunction;
            blockCountEndFunction += 1;
            break;
        case 'block-return':
            newBlock.id = data + "-" + blockCountReturn;
            blockCountReturn += 1;
            break;
        case 'block-call':
            newBlock.id = data + "-" + blockCountCall;
            blockCountCall += 1;
            break;
        case 'block-assignment':
            newBlock.id = data + "-" + blockCountAssignment;
            blockCountAssignment += 1;
            break;
    }

    ev.target.appendChild(newBlock);
}

$(document).ready(function () {
    $("#btn-execute").click(function(){
        $('#block-canvas').each(function () {
            console.log($("#block-canvas").children());
        });
    });

    $('#btn-clear').click(function(){
        $('#block-canvas').empty();
        blockCountRead = 0;
        blockCountPrint = 0;
        blockCountVarInt = 0;
        blockCountVarBool = 0;
        blockCountVarChar = 0;
        blockCountIf = 0;
        blockCountElse = 0;
        blockCountEndCondition = 0;
        blockCountWhile = 0;
        blockCountEndLoop = 0;
        blockCountFunction = 0;
        blockCountStartParameters = 0;
        blockCountParameter = 0;
        blockCountEndParameters = 0;
        blockCountEndFunction = 0;
        blockCountReturn = 0;
        blockCountCall = 0;
        blockCountAssignment = 0;
    })
});
