# **Lexical Analyzer Implementation Report**

I’m **Eric Mpangi**, and this implementation provides a lexical analyzer (lexer) in **Python**, leveraging a **regular expression-based approach** to tokenize an input string.

## 1. Introduction to Lexical Analysis

Lexical analysis is the first phase of a compiler, responsible for scanning the input text and breaking it into meaningful tokens. A **lexer** (also called a lexical analyzer) reads a sequence of characters and groups them into **tokens**, which are categorized based on the defined lexical grammar.

Tokens are the smallest units of a programming language, such as keywords, identifiers, operators, and literals. The lexer processes input sequentially, applying **finite state automata (FSA)** principles to determine token boundaries and classify them appropriately.

## 2. Finite State Automata (FSA) and Deterministic Finite Automaton (DFA)

A **finite state automaton (FSA)** consists of:
- A finite set of states
- An alphabet (set of characters recognized)
- Transition functions mapping states to other states based on input
- A start state
- A set of final (accepting) states

A **deterministic finite automaton (DFA)** is a type of FSA where, for each state and input symbol, there is **only one possible next state**. Lexers use DFAs to match input against token patterns efficiently.

## 3. Lexer Design and Tokenization Process

The lexer uses **regular expressions (regex)** to tokenize arithmetic expressions efficiently.

The given lexer processes arithmetic expressions containing numbers, operators, and parentheses. The key tokens identified by this lexer are:

### **Key Responsibilities of a Lexer:**
- **Recognizing tokens** such as numbers, arithmetic operators, and parentheses.
- **Ignoring whitespace and invalid characters** to maintain clean tokenization.
- **Handling errors** in cases of unexpected characters or malformed expressions.
- **Ensuring correct precedence** by accurately classifying numeric types (integers, floating-point numbers).

### **Token Definitions:**
| Token Type | Example Symbols |
|------------|----------------|
| INTEGER    | 123, 456       |
| PLUS       | +              |
| MINUS      | -              |
| MULTIPLY   | *              |
| DIVIDE     | /              |
| LPAREN     | (              |
| RPAREN     | )              |
| WHITESPACE | \t, \n, space  |


- **INTEGER**: A sequence of digits (`0-9`).
- **FLOAT**: A number with a decimal point (`3.14`).
- **OPERATOR**: Symbols for arithmetic operations (`+`, `-`, `*`, `/`).
- **LPAREN / RPAREN**: Parentheses (`(`, `)`) for grouping expressions.

The lexer scans the input **left to right**, character by character, and applies the following logic:
1. If the character is a digit, consume all consecutive digits to form an INTEGER token.
2. If the character is a known operator (`+`, `-`, `*`, `/`), return the corresponding token.
3. If the character is a parenthesis (`(` or `)`), return the corresponding token.
4. If the character is a whitespace, skip it and move to the next character.
5. If an **unexpected character** is encountered, raise a `ValueError` indicating the position of the error.

## 4. Transition Diagram

The following transition diagram represents the DFA states used by the lexer:

```
   (Start) ---> [Digit] ---> (Integer) ---> [Digit] ---> (Integer)
        |              |  
        |              +--> [Operator] ---> (Operator Token)
        |
        +--> [Whitespace] ---> (Ignore & Continue)
        |
        +--> [Parentheses] ---> (LPAREN or RPAREN Token)
        |
        +--> [Unexpected Character] ---> (Raise Error)
```
Each state transition is determined by the type of character encountered.

- **States:** Represent different recognition points (e.g., start state, number recognition, operator recognition).
- **Transitions:** Arrows indicating movement between states based on input (digits, operators, or parentheses).
- **Accepting States:** Indicate successful recognition of tokens.

## 5. Tokenization Example

Given the input:

```plaintext
12 + 34 * (56 - 78)
```

The lexer generates the following tokens:

```plaintext
[INTEGER(12), PLUS(+), INTEGER(34), MULTIPLY(*), LPAREN(()), INTEGER(56), MINUS(-), INTEGER(78), RPAREN())]
```
### **Example Outputs:**
| Input          | Output Tokens                              |
|---------------|-----------------------------------------|
| "42"          | `{INTEGER 42}`                           |
| "3.14 + 2"    | `{FLOAT 3.14}, {OPERATOR +}, {INTEGER 2}` |
| "5 * (3 - 1)" | `{INTEGER 5}, {OPERATOR *}, {LPAREN (}, {INTEGER 3}, {OPERATOR -}, {INTEGER 1}, {RPAREN )}` |

## 6. Error Handling in Lexer

The lexer includes an explicit error-handling mechanism. When an unrecognized character is encountered, it raises:

```python
raise ValueError(f"Unexpected character '{input_text[last_end]}' at position {last_end}")
```

This ensures that input containing invalid symbols is immediately flagged, preventing incorrect parsing.

## 7. Future Optimizations and Enhancements

1. **Support for Floating-Point Numbers:** Extend the INTEGER state to recognize decimal points.
2. **Handling Comments:** Allow `#` or `//` to be treated as comment starters.
3. **Enhanced Error Reporting:** Provide more contextual error messages with line and column numbers.

## 8. Conclusion

This lexer effectively tokenizes arithmetic expressions using a **DFA-based approach**, ensuring efficient and accurate lexical analysis. The transition diagram, error handling, and token categorization make it a solid foundation for a parser in a larger compiler or interpreter pipeline.

