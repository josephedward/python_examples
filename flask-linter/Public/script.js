const EDITOR_CONTENTS = {
    "JavaScript": "var widgets = []\nfunction updateHints() {/*from w  w w.  ja va  2 s.c o  m*/\n\teditor.operation(function(){\n\tfor (var i = 0; i &lt; widgets.length; ++i)\n\t\teditor.removeLineWidget(widgets[i]);\n\twidgets.length = 0;\n\tJSHINT(editor.getValue());\n\tfor (var i = 0; i &lt; JSHINT.errors.length; ++i) {\n\t\t\t...\n\t\t\t...\n\t\t\t...\n\t}\n\t});\n\tvar info = editor.getScrollInfo();\n\tvar after = editor.charCoords({line: editor.getCursor().line + 1, ch: 0}, 'local').top;\n\tif (info.top + info.clientHeight &lt; after)\n\t\teditor.scrollTo(null, after - info.clientHeight + 3);\n}",
    "HTML": "<div>\n\t<p\n</div>",
    "CSS": "#language{\n\tcolor:#234562\n\tdf:\n}",
    "PHP": "<?php\necho 'Hello world';\n$foo = [1, 2, 3]\n\t\n\twp_list_cats($bar);\nproc_open(false);\nexit(0);\neval('evil');\n",
    "Java": `public class Main{\n\tpublic static void main(String args[]){\n\t\tSystem.out.println("Hello World !");\n\t}\nasdf\n}`,
    "C": `#include <stdio.h>\nint main() {\n\tprintf("Hello, World!");\n\tint a = ;\n\tfor ( d)\n\treturn 0;}`,
    "C++": `#include<iostream> \nusing namespace std;\nint main() \n{ \n\tcout<<"Hello World"; \n\tdfg\n\treturn 0; \n}`,
    "C#": `using System;\nnamespace Project_1 {\n\tclass MainClass {\n\t\tpublic static void Main (string[] args) {\n\t\t\tConsole.WriteLine ("Hello World!");\n\t\t\tConsole.ReadKey ();\n\t\t\tsdf;\n\t\t}\n\t}\n}`,
    "Python": `print("Hello World")\nsdf("34")\nvbn`,
    "Ruby": `print "Hello, World!"\nasd`,
    "Golang": `package main\nfunc main() {\n\tprintln("Hello world!")\nasdf\n}`
};
const MODES = {
    "HTML": "ace/mode/html",
    "CSS": "ace/mode/css",
    "JavaScript": "ace/mode/javascript",
    "PHP": "ace/mode/php",
    "Java": "ace/mode/java",
    "C": "ace/mode/c_cpp",
    "C++": "ace/mode/c_cpp",
    "C#": "ace/mode/csharp",
    "Python": "ace/mode/python",
    "Ruby": "ace/mode/ruby",
    "Golang": "ace/mode/golang",
};
var current_lang = "JavaScript";

var editor = ace.edit("editor");
editor.setTheme("ace/theme/monokai");
editor.setValue(EDITOR_CONTENTS["JavaScript"]);
editor.session.setMode(MODES["JavaScript"]);
document.getElementById("languages").value = "JavaScript";
editor.setOptions({
    enableBasicAutocompletion: true
});
var isSendingRequest = false;
var isSwitchingLanguage = false;
const userFolder = "temp/" + Math.random().toString(36).substring(2, 15); // This is the folder which will be generated on the backend for temp compiling files. This folder will be removed when user leaves the site.
var currentFileName = null;
var operationArray = [];

// Remove userfolder generated for compiling files on the back-end.
window.onbeforeunload = function() {
    $.ajax({
        type: 'POST',
        url: 'api-linter/removeTemp',
        data: {
            folderName: userFolder
        }
    });
}
editor.session.on("change", function(e) {
    if (current_lang === "Java" || current_lang === "C" || current_lang === "C++" || current_lang === "C#" || current_lang === "Ruby" || current_lang === "Golang" || current_lang === "Python") {
        var operation = {};
        operation.action = e.action;
        operation.start = editor.session.doc.positionToIndex(e.start, 0);
        operation.end = editor.session.doc.positionToIndex(e.end, 0);
        operation.text = e.lines.join('\n');
        console.log(operation);
        if (isSwitchingLanguage === false) {
            if (isSendingRequest === false) {
                operation_syntax_check([operation], current_lang, currentFileName);
            } else {
                operationArray.push(operation);
            }
        }
    }
});
editor.keyBinding.addKeyboardHandler({
    handleKeyboard: function(data, hash, keyString, keyCode, event) {
        if (hash === -1 || (keyCode <= 40 && keyCode >= 37)) return false;
        isSwitchingLanguage = false;
    }
});
document.getElementById("languages").onchange = function() {
    isSendingRequest = false;
    isSwitchingLanguage = true;
    current_lang = document.getElementById("languages").value;
    editor.setValue(EDITOR_CONTENTS[current_lang]);
    editor.session.setMode(MODES[current_lang]);
    if (current_lang === "Java" || current_lang === "C" || current_lang === "C++" || current_lang === "C#" || current_lang === "Ruby" || current_lang === "Golang" || current_lang === "Python") {
        init_syntax_check(current_lang);
    }
}
function init_syntax_check(lang) {
    if (isSendingRequest) return;
    isSendingRequest = true;
    $.ajax({
        type: 'POST',
        url: 'api-linter/initlint',
        data: {
            text: editor.getValue(),
            lang: lang,
            folderName: userFolder
        },
        success: function(data) {
            currentFileName = data.payload.fileName;
            if (data.status === "error") {
                var error_array = data.payload.message.split("\n");
                console.log(error_array);                    
                var error_result = filterErrors(error_array, lang, data.payload.fileName);
                console.log(error_result);
                editor.getSession().setAnnotations(error_result);
            } else {
                editor.getSession().setAnnotations([]);
                console.log("No Errors");
            }
            isSendingRequest = false;
        },
        error: function(error) {
            console.log("Error:" + error);
            isSendingRequest = false;
        }
    });
}
function operation_syntax_check(operation, lang) {
    if (isSendingRequest) return;
    isSendingRequest = true;
    $.ajax({
        type: 'POST',
        url: 'api-linter/lint',
        data: {
            operation: JSON.stringify(operation),
            lang: lang,
            fileName: currentFileName
        },
        success: function(data) {
            if (data.status === "error") {
                var error_array = data.payload.message.split("\n");
                console.log(error_array);                    
                var error_result = filterErrors(error_array, lang);
                console.log(error_result);
                editor.getSession().setAnnotations(error_result);
            } else {
                editor.getSession().setAnnotations([]);
            }
            isSendingRequest = false;
            if (operationArray.length) {
                var temparray = [...operationArray];
                operationArray = [];
                operation_syntax_check(temparray, lang);
            }
        },
        error: function(error) {
            console.log("Error:" + error);
            isSendingRequest = false;
        }
    });
}
function filterErrors(error_array, lang) {
    var result = [];
    var index = 0;
    for (var i = 0; i < error_array.length; i ++) {
        if (lang === "Ruby") {
            if (!error_array[i].length) continue;
            result[index] = {};
            result[index]['type'] = 'error';
            var temp = error_array[i].substring(error_array[i].indexOf('line') + 5);
            result[index]['row'] = parseInt(temp.substring(0, temp.indexOf(','))) - 1;
            temp = temp.substring(temp.indexOf(':') + 1);
            result[index ++]['text'] = temp;
        } else if (lang === "Python") {
            if (!error_array[i].length || (error_array[i][0] !== 'E' && error_array[i][0] !== 'W')) continue;
            result[index] = {};
            if (error_array[i][0] === 'E')
                result[index]['type'] = 'error';
            else 
                result[index]['type'] = 'warning';
            var temp = error_array[i].substring(2);
            result[index]['row'] = parseInt(temp.substring(0, temp.indexOf(','))) - 1;
            temp = temp.substring(temp.indexOf(':') + 1);
            result[index ++]['text'] = temp;
        }
        else if (error_array[i].indexOf(currentFileName) === 0) {
            result[index] = {};
            if (lang === "Golang") {
                result[index]['type'] = 'error';
                var temp = error_array[i].substring(currentFileName.length + 1);
                result[index]['row'] = parseInt(temp.substring(0, temp.indexOf(':'))) - 1;
                result[index ++]['text'] = temp.substring(temp.indexOf(':', temp.indexOf(':') + 1) + 1);
            } else {
                if (error_array[i].indexOf(': error') === -1) 
                    continue;
                result[index]['type'] = 'error';
                if (lang === "C#") {
                    var ctemp = error_array[i].substring(error_array[i].indexOf(": " + result[index]['type']) + result[index]['type'].length + 3);
                    result[index]['text'] = ctemp.substring(ctemp.indexOf(":") + 1);
                } else {
                    result[index]['text'] = error_array[i].substring(error_array[i].indexOf(": " + result[index]['type']) + result[index]['type'].length + 4);
                }
                
                var temp = error_array[i].substring(currentFileName.length + 1, error_array[i].indexOf(": " + result[index]['type']));
                if (lang === "Java") {
                    result[index ++]['row'] = parseInt(temp, 10) - 1;
                } else if (lang === "C" || lang === "C++") {
                    result[index ++]['row'] = parseInt(temp.substring(0,temp.indexOf(':')), 10) - 1;
                } else if (lang === "C#") {
                    result[index ++]['row'] = parseInt(temp.substring(0,temp.indexOf(',')), 10) - 1;
                } 
            }
        }
    }
    return result;
}