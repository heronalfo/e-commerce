```markdown
# Brazilian Data Types

## 1. CEP (Postal Address Code)

CEP is a code used by the Brazilian postal service to uniquely identify addresses. It follows the format `XXXXX-XXX`, where `X` is a numeric digit.

### Example of CEP
- 01001-000
- 12345-678

### Regex Pattern for CEP Validation
```regex
^\d{5}-\d{3}$
```

## 2. CPF (Individual Taxpayer Registry)

CPF is an identification document used in Brazil for individuals. It follows the format `XXX.XXX.XXX-XX`, where `X` is a numeric digit.

### Example of CPF
- 123.456.789-01
- 987.654.321-00

### Regex Pattern for CPF Validation
```regex
^\d{3}\.\d{3}\.\d{3}-\d{2}$
```

## 3. Brazilian Telephone Number Format

In Brazil, telephone numbers follow a specific format, usually composed of the country code, area code, and phone number. The most common format is `+55 (XX) XXXXX-XXXX` or `+55 (XX) XXXX-XXXX` for landlines.

### Example of Phone Number
- +55 (11) 91234-5678 (Mobile)
- +55 (11) 1234-5678 (Landline)

### Regex Pattern for Phone Number Validation
```regex
^\+\d{2} \(\d{2}\) \d{4,5}-\d{4}$
```

## Python Usage Examples

### CEP Validation
```python
import re

def validate_cep(cep):
    pattern = re.compile(r'^\d{5}-\d{3}$')
    if not pattern.match(cep):
        raise ValueError('Invalid CEP')
    return cep

# Usage example
validate_cep('01001-000')
```

### CPF Validation
```python
import re

def validate_cpf(cpf):
    pattern = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')
    if not pattern.match(cpf):
        raise ValueError('Invalid CPF')
    return cpf

# Usage example
validate_cpf('123.456.789-01')
```

### Phone Number Validation
```python
import re

def validate_phone(number):
    pattern = re.compile(r'^\+\d{2} \(\d{2}\) \d{4,5}-\d{4}$')
    if not pattern.match(number):
        raise ValueError('Invalid phone number')
    return number

# Usage example
validate_phone('+55 (11) 91234-5678')
```

## Conclusion

These are some of the main data types used in Brazil, each with its own specific format and validation patterns. It is important to follow these patterns to ensure the integrity and validity of data in systems that use Brazilian information.
```

This file provides an overview of the formats for CEP, CPF, and phone numbers in Brazil, along with examples and regex patterns for validation.
```