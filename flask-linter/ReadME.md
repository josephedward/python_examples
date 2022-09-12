# Linters for ACEeditor
  Supports HTML, JavaScript, CSS, Java, PHP, C, C++, C#, Python, Ruby, and Golang.

# Installation
- Build Docker image by following command:
  `docker build -t acelinter:1.0 .`
- Run Docker image by following command:
  `docker run -d -p 3000:3000 acelinter:1.0`

# How it works
- Back-End
  * /api-linter/initlint: This endpoint is for creating temp file to compile C/C++, C#, Java, Ruby, Python, Golang and retrieves compile result(error) to be used as linter in front-end.
  * /api-linter/lint: This endpoint is for operational transformation for created temp file to compile and get result(error).
  * /api-linter/removeTemp: This endpoint is for removing temp folder and files which created for compilation for compiled languages.
- Front-End
  * `const userFolder = "temp/" + Math.random().toString(36).substring(2, 15);` : This is the folder which will be created to store temp files for compile compiled languages in Back-End. You can use user ID instead of this random string in future development.
  * `function init_syntax_check(lang) { ... }` : This is the function for /api-linter/initlint endpoint. When the language is switched to compiled language, this function will be called, create temp folder and file to be compiled on the back-end, and retrieves the result.
  * `function operation_syntax_check(operation, lang) { ... }`: This is the function for /api-linter/lint endpoint. When user type something in the code editor and if it's compiled language, this function will be called to post operational transformation and retrieves the result.
  * `function filterErrors(error_array, lang) { ... }`: This is the function to get linter(error) from the result of init_syntax_check & operation_syntax_check functions for different languages.
  
