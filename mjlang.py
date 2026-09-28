import sys
import re

class MJLangInterpreter:
    def __init__(self):
        self.variables = {}
        self.lines = []
        self.pc = 0  # Program counter

    def evaluate_expression(self, expr_str):
        expr_str = expr_str.strip()
        
        # Handle Equality (BLACK OR WHITE)
        if " BLACK OR WHITE " in expr_str:
            parts = expr_str.split(" BLACK OR WHITE ")
            return int(self.get_value(parts[0]) == self.get_value(parts[1]))
            
        # Handle Addition (THRILLER)
        if " THRILLER " in expr_str:
            parts = expr_str.split(" THRILLER ")
            return self.get_value(parts[0]) + self.get_value(parts[1])
            
        # Handle Subtraction (BAD)
        if " BAD " in expr_str:
            parts = expr_str.split(" BAD ")
            return self.get_value(parts[0]) - self.get_value(parts[1])
            
        return self.get_value(expr_str)

    def get_value(self, token):
        token = token.strip()
        if token.startswith('"') and token.endswith('"'):
            return token[1:-1]
        if token.isdigit():
            return int(token)
        if token in self.variables:
            return self.variables[token]
        return token

    def run(self, code):
        # Filter empty lines
        self.lines = [line.strip() for line in code.split('\n') if line.strip()]
        
        if not self.lines or self.lines[0] != "OW!":
            print("Error: The program must begin with 'OW!'")
            return
            
        if self.lines[-1] != "HEE-HEE!":
            print("Error: The program must end with 'HEE-HEE!'")
            return

        self.pc = 1
        while self.pc < len(self.lines) - 1:
            line = self.lines[self.pc]
            
            # 1. Print statement (JAM)
            if line.startswith("JAM "):
                content = line[4:].strip()
                print(self.evaluate_expression(content))
                self.pc += 1

            # 2. Variable declaration/assignment (SHAMONE)
            elif line.startswith("SHAMONE "):
                match = re.match(r"SHAMONE\s+(\w+)\s+BILLIE JEAN\s+(.+)\s+AOW", line)
                if match:
                    var_name = match.group(1)
                    expr = match.group(2)
                    self.variables[var_name] = self.evaluate_expression(expr)
                self.pc += 1

            # 3. Loops (MOONWALK)
            elif line.startswith("MOONWALK "):
                condition_expr = line[9:].strip()
                loop_end = self.pc + 1
                nesting = 1
                while loop_end < len(self.lines):
                    if self.lines[loop_end].startswith("MOONWALK "):
                        nesting += 1
                    elif self.lines[loop_end] == "DON'T STOP 'TIL YOU GET ENOUGH":
                        nesting -= 1
                        if nesting == 0:
                            break
                    loop_end += 1

                if self.evaluate_expression(condition_expr) != 0:
                    self.pc += 1
                else:
                    self.pc = loop_end + 1

            elif line == "DON'T STOP 'TIL YOU GET ENOUGH":
                loop_start = self.pc - 1
                nesting = 1
                while loop_start >= 0:
                    if self.lines[loop_start] == "DON'T STOP 'TIL YOU GET ENOUGH":
                        nesting += 1
                    elif self.lines[loop_start].startswith("MOONWALK "):
                        nesting -= 1
                        if nesting == 0:
                            break
                    loop_start -= 1
                self.pc = loop_start

            # 4. Conditionals placeholders (WHO'S BAD)
            elif line.startswith("WHO'S BAD "):
                self.pc += 1

            elif line in ["YOU'VE BEEN HIT BY", "BEAT IT"]:
                self.pc += 1
            else:
                self.pc += 1

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python mjlang.py <your_file.mj>")
    else:
        with open(sys.argv, 'r', encoding='utf-8') as f:
            code = f.read()
        interpreter = MJLangInterpreter()
        interpreter.run(code)
