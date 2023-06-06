# Cross-Language Compatible CFG "If-Else" Condition Conversion

This project aims to provide a strategy for converting a CFG (Control Flow Graph) "If-Else" condition selection that is compatible with both Go and Java programming languages. By following the outlined steps and considering the syntax and semantics of both languages, you can ensure that your CFG will work seamlessly in both Go and Java.

## Strategy Overview
1. Understand the syntax differences: Familiarize yourself with the syntax variations between Go and Java for writing if-else conditions.
2. Write your CFG in a language-agnostic manner: Focus on expressing the logical flow of your program using high-level concepts, avoiding language-specific constructs or syntax.
3. Identify language-specific variations: Identify any differences in operators, data types, or control flow constructs between Go and Java. Make necessary adjustments in your CFG to account for these variations.
4. Create separate translation functions: Develop separate translation functions for Go and Java, which take your language-agnostic CFG as input and generate the corresponding code in the respective language. These functions handle the language-specific syntax and conversions.
5. Test and validate: Thoroughly test the translation functions using various scenarios and inputs to ensure the generated code works correctly in both Go and Java.

## Usage

To use this project, follow these steps:

1. Clone the repository to your local machine.
2. Modify the language-agnostic CFG to suit your specific if-else condition selection.
3. Implement the separate translation functions for Go and Java, ensuring the correct conversion from the CFG to each language's syntax.
4. Test the translation functions using different inputs and scenarios to validate the correctness of the generated code.

## Project Structure

The project structure is as follows:
- README.md              # Project overview and instructions
- go_translation.go      # Go translation function
- java_translation.java  # Java translation function

## Contributing

Contributions to this project are currently resricted! If you find any issues or have ideas for improvements, please feel free to open an issue or submit a pull request.
Current contributors:
- [Ikhsan Assidiqie](https://github.com/ikhsansdqq)
- [Fauzan Rizqi Muhammad](https://github.com/CakZemprongzz)

## Technology
![ChatGPT](https://img.shields.io/badge/chatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white) ![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white)
![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white) ![Go](https://img.shields.io/badge/go-%2300ADD8.svg?style=for-the-badge&logo=go&logoColor=white)

___
By following the outlined strategy, you can ensure that your CFG "If-Else" condition selection is compatible with both Go and Java. Remember to allocate sufficient time for testing and debugging to ensure the accuracy of the translations.
