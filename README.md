# propositional-logic-parser-python
This Python tool is designed to parse propositional logic formulas. It enables the processing of logical formulas that involve symbols such as ~ (not), & (and), | (or), => (implies), and <=> (if and only if).

Additionally, it provides two features:
- `to_string` method: The parsed formula will be displayed back with appropriate UTF-8 symbols and adequate spacing for improved readability.
- Abstract Syntax Tree (AST) image generation: The tool also generates a PNG image that visually represents the abstract syntax tree resulting from the formula parsing process. This helps users visualize the hierarchical structure of the formula and understand its logical composition.

Note: This project was tested using Python 3.10.9 on Ubuntu.

## Installation
1. Before starting, you need to have Python installed on your system.
2. Clone or download the project repository.
3. Install Poetry.
4. Install the project with poetry. Run the following in the root of the project:
    ```shell
    $ poetry install
    ```
5. Install `Graphviz` which is a `pydot` dependency to be installed separately. It can be downloaded from https://graphviz.org/download/.

## Usage
To use the propositional logic parser, activate the project environment and execute the `plparser-cli` command with the formula you want to parse as a command-line argument.
You can use the flags `-p` or `--print` to print the formula and the argument `-g` or `--generate` followed by a filename to generate the corresponding PNG image.  

You must ensure that every formula that includes a binary connective (&, |, =>, or <=>) is surrounded by parentheses. For example, write "(wff_1 & wff_2)" for a formula using the AND connective. Conversely, when utilizing the negation connective, omit the use of parentheses. Instead, use "\~wff" to represent a negated formula. A combination of the two rules allows to write "\~(wff_1 & wff_2)". By following these formatting rules, you can ensure that your formulas are unambiguous and correctly interpreted by the program.

Note: It is important to adhere to these formatting rules to avoid exceptions. 

Here is an example of using the CLI:
```shell
$ plparser-cli -p -g "wff" "(~ (( ~A & (B1 | B2) )<=>C ) => D)"
```
The output will be:
```
Well-formed formula: (¬((¬A ∧ (B1 ∨ B2)) ↔ C) → D)
The image wff.png has been generated.
```
Also, the following PNG image named `wff.png` will be created in the current directory.

![The AST representation of the wff](images/wff.png)

## License
This project is licensed under the Apache 2.0 license.
See the LICENSE file for more information.

## Acknowledgements
This project utilizes the following open-source libraries:
- `pydot`:
  - Version: 2.0.0
  - License: MIT
  - Project website: https://github.com/pydot/pydot
  - Purpose: used for generating image of the AST.
- `pytest`:
  - Version: 7.4.4
  - License: MIT
  - Project website: https://docs.pytest.org
  - Purpose: used for testing purposes.
- `textX`:
  - Version: 4.0.1
  - License: MIT
  - Project website: https://textx.github.io/textX
  - Purpose: used for parsing the input formula.

Special thanks to the authors and contributors who dedicated their time and effort to develop these libraries. Their hard work and valuable contributions have greatly benefited the software development community.

## Contact
If you have any questions or inquiries, please contact raphael.bonatti@algolance.com.
