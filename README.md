# Mini-Sistema-de-Controle-de-Estoque-RAD-
protótipo ágil de uma aplicação Desktop com Interface Gráfica  (GUI) para gerenciar o estoque de uma loja.


# Git 

## 1. Clonar o repositório

Cada integrante deve clonar o repositório do GitHub:

```bash
git clone https://github.com/samuelmel/Mini-Sistema-de-Controle-de-Estoque-RAD-
```

Depois entrar na pasta do projeto:

```bash
cd Mini-Sistema-de-Controle-de-Estoque-RAD-
```

---

# 2. Criar sua branch

Cada integrante deve trabalhar na própria branch para evitar conflitos.

Exemplos:

```bash
git checkout -b réipodi
```

## Interface

```bash
git checkout -b edellybosta
```

---

# 3. Verificar em qual branch está

```bash
git branch
```

A branch atual aparecerá com `*`.

---

# 4. Salvar alterações

Depois de terminar uma parte do código:

```bash
git add .
```

Criar commit:

```bash
git commit -m "descrição da alteração"
```

Exemplo:

```bash
git commit -m "implementa CRUD sqlite"
```

---

# 5. Enviar para o GitHub

```bash
git push -u origin nome-da-branch
```

Exemplo:

```bash
git push -u origin crud-database
```

Depois do primeiro push, basta usar:

```bash
git push
```

---

# 6. Atualizar projeto local

Antes de começar a programar no dia:

```bash
git checkout main
git pull
```

Depois voltar para sua branch:

```bash
git checkout nome-da-branch
```

---

# Regras do Grupo

* Cada integrante deve trabalhar apenas na sua branch
* Evitar modificar arquivos da tarefa de outra pessoa
* Fazer commits frequentes
* Sempre testar antes de dar push
* Não apagar arquivos do projeto sem avisar o grupo
