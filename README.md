# PORT Scanner para TCP

## Projeto de um scanner de portas TCP em Python

Atividade faz parte do roteiro 1, da materia de tecnologias hacker, do curso de Engenharia de Computação, Insper.

## Modo de Uso

Para rodar, basta rodar o comando:

```bash
python3 main.py
```

Ele possui alguns flags que podem ser utilizados, todos opcionais:

- `-h` ou `--help`: para mostrar a ajuda
- `--host`: para especificar o host a ser escaneado
- `--port`: para especificar a porta a ser escaneada

Nas portas, ao ser passado o valor `all`, ele irá escanear todas as portas de 1 a 65535.


### Rodando sem usar flags

```bash
python3 main.py
```


### Rodando com flags

```bash
python3 main.py --host 127.0.0.1 --port 1-1000
```

## Referencias

- [Writing a Basic Port Scanner in Python](https://westoahu.hawaii.edu/cyber/forensics-weekly-executive-summmaries/writing-a-basic-port-scanner-in-python/)