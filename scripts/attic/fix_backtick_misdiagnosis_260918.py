#!/usr/bin/env python3
"""Fix verify_quotes.py: CIRCLED ] inside char class must be escaped as \]"""
with open('scripts/verify_quotes.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Problem: [' + CIRCLED + r']...' — CIRCLED contains ] chars, so the first ]
# in CIRCLED (after ⑳) prematurely closes the char class.
# Fix: change the closing ] of the char class to \]
# 
# Pattern in source: r']\*{0,2}'  (char class ends with CIRCLED, then ]\*{0,2})
# Must become:      r']\*{0,2}' → r'\]\*{0,2}'
# i.e., the ] after CIRCLED becomes \] so it's a literal ] in the regex

# Find lines with CIRCLED in re.match
import re
lines = content.split('\n')
for i, line in enumerate(lines):
    if '+ CIRCLED +' in line and 're.match' in line:
        print(f"Line {i+1} BEFORE: {line[:100]}")
        # The pattern is: r']...{N}' where the first ] after CIRCLED closes the char class
        # We need to escape it: r']\...{N}' → r']\...{N}'
        # In the raw string: r']\*{0,2}' → r'\]\*{0,2}'
        # Only the ] that closes the char class (followed by \*{ or \s+) needs escaping
        # The ] inside CIRCLED is already there but is INSIDE the class
        # The class-closing ] is the one after CIRCLED's last char
        # Strategy: in the string concatenation r']\*{' or r']\s+', escape the ]
        # Replace: r']\*{' → r'\]\*{'  and  r']\s+' → r'\]\s+'
        line = line.replace(r"r']\*{0,2}", r"r']\*{0,2}")
        line = line.replace(r"r']\s+", r"r']\s+")
        # Actually we need to ADD the backslash: r']\*{' → r'\]\*{'
        # These are raw strings so \ is literal
        line_new = re.sub(r"r'\]\{(\d+),(\d+)\}", lambda m: m.group(0), line)
        # The actual fix: wherever r']...' appears (char class closer after CIRCLED),
        # add \ before ]
        # Pattern: after CIRCLED + r']' → char class closes
        # Fix: r'] followed by \*{ or \s+ → r'\] followed by \*{ or \s+
        line = re.sub(r"(CIRCLED \+ r')\](\\*\d)", r"\1\\]\2", line)
        if line != lines[i]:
            print(f"Line {i+1} AFTER:  {line[:100]}")
        lines[i] = line

content = '\n'.join(lines)
with open('scripts/verify_quotes.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Done")
