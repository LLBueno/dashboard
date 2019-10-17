# Dashboard
Dashboard desenvolvido na disciplina de Programação de Scripts.

## Instalação no Ubuntu


### Pyenv
Instale o Pyenv para controlar suas versões de Python em um ambientes isolados.

Instalação das dependências do pyenv
> $ sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm gettext libncurses5-dev tk-dev tcl-dev blt-dev libgdbm-dev git python-dev python3-dev aria2 vim libnss3-tools python3-venv liblzma-dev

Instale o pyenv
> $ curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

Adicione as variáveis de ambiente em seu arquivo ```.bashrc```.

```
export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"

export PIPENV_VENV_IN_PROJECT=1
export PYENV_ROOT=~/.pyenv
```
Reinicie o seu shell para aplicar as variáveis adicionadas.

> $ exec $SHELL

Instale o Python 3. Exemplo:

> $ pyenv install 3.8.0

Para agilizar defina como sua versão global.

> $ pyenv global 3.8.0

### Pipenv
Instale o pipenv para controle das dependências do projeto.

> $ pip install pipenv

Clone o projeto

> $ git clone https://github.com/LLBueno/dashboard.git

Dentro do diretório raiz, crie seu ambiente usando as dependências de desenvolvimento já adicionadas.

> $ pipenv sync -d


## Terminando...
