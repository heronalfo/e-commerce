```markdown
# Tipos de Dados Brasileiros

## 1. CEP (Código de Endereçamento Postal)

O CEP é um código utilizado pelos Correios do Brasil para identificar endereços de forma única. Ele segue o formato `XXXXX-XXX`, onde `X` é um dígito numérico.

### Exemplo de CEP
- 01001-000
- 12345-678

### Padrão Regex para Validação de CEP
```regex
^\d{5}-\d{3}$
```

## 2. CPF (Cadastro de Pessoas Físicas)

O CPF é um documento de identificação utilizado no Brasil para indivíduos. Ele segue o formato `XXX.XXX.XXX-XX`, onde `X` é um dígito numérico.

### Exemplo de CPF
- 123.456.789-01
- 987.654.321-00

### Padrão Regex para Validação de CPF
```regex
^\d{3}\.\d{3}\.\d{3}-\d{2}$
```

## 3. Padrão de Nomenclatura Telefônica Brasileira

No Brasil, os números de telefone seguem um formato específico, geralmente composto pelo código do país, código de área e número do telefone. O formato mais comum é `+55 (XX) XXXXX-XXXX` ou `+55 (XX) XXXX-XXXX` para números fixos.

### Exemplo de Número de Telefone
- +55 (11) 91234-5678 (Celular)
- +55 (11) 1234-5678 (Fixo)

### Padrão Regex para Validação de Número de Telefone
```regex
^\+\d{2} \(\d{2}\) \d{4,5}-\d{4}$
```

## Exemplos de Utilização em Python

### Validação de CEP
```python
import re

def validate_cep(cep):
    pattern = re.compile(r'^\d{5}-\d{3}$')
    if not pattern.match(cep):
        raise ValueError('CEP inválido')
    return cep

# Exemplo de uso
validate_cep('01001-000')
```

### Validação de CPF
```python
import re

def validate_cpf(cpf):
    pattern = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')
    if not pattern.match(cpf):
        raise ValueError('CPF inválido')
    return cpf

# Exemplo de uso
validate_cpf('123.456.789-01')
```

### Validação de Número de Telefone
```python
import re

def validate_phone(number):
    pattern = re.compile(r'^\+\d{2} \(\d{2}\) \d{4,5}-\d{4}$')
    if not pattern.match(number):
        raise ValueError('Número de telefone inválido')
    return number

# Exemplo de uso
validate_phone('+55 (11) 91234-5678')
```

## Conclusão

Esses são alguns dos principais tipos de dados utilizados no Brasil, cada um com seu próprio formato específico e padrões de validação. É importante seguir esses padrões para garantir a integridade e a validade dos dados em sistemas que utilizam informações brasileiras.
```

Este arquivo fornece uma visão geral dos formatos de CEP, CPF e números de telefone no Brasil, juntamente com exemplos e padrões de regex para validação.