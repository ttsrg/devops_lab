#!/bin/bash
#Installing python

if [[ ! -d $HOME/.pyenv/versions/2.7.0 ]] ; then
	echo -en "\033[35m python 2.7.0   not exists \033[0m\n"
	sudo yum install -y curl zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel \
	openssl-devel xz xz-devel libffi-devel
	curl -L  https://raw.github.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

	export PATH="/$HOME/.pyenv/bin:$PATH"
	eval "$(pyenv init -)"
	eval "$(pyenv virtualenv-init -)"

	pyenv install -f  2.7.0
	pip install wheel
	pyenv global  2.7.0
	pip install --upgrade pip
	pip install wheel
	pip install virtualenv
	pyenv virtualenv -f virtenv2

	python -V
	pyenv virtualenvs
	pyenv versions

elif [[ ! -L $HOME/.pyenv/versions/virtenv2 ]] ; then 
	echo -en "\033[35m virtualenv2  not exists \033[0m\n"

	pip install virtualenv
	pyenv virtualenv -f virtenv2

	python -V
	pyenv virtualenvs
	pyenv versions
else 
	echo -en "\033[33m python 2 and virtualenv2 exists \033[0m\n"
fi


echo "################### install second ver of python"

PYTHONVER=3.7.1
if [[ ! -d $HOME/.pyenv/versions/$PYTHONVER ]] ; then
        echo -en "\033[35m python $PYTHONVER    not exists \033[0m\n"
        sudo yum install -y curl zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel \
        openssl-devel xz xz-devel libffi-devel
	curl -L  https://raw.github.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

        export PATH="/$HOME/.pyenv/bin:$PATH"
        eval "$(pyenv init -)"
        eval "$(pyenv virtualenv-init -)"

        pyenv install -f  $PYTHONVER 
        pyenv versions
        pyenv global  $PYTHONVER 
        pip install --upgrade pip
	pip install wheel
        pip install virtualenv
        pyenv virtualenv -f virtenv3

        python -V
        pyenv virtualenvs
        pyenv versions

elif [[ ! -L $HOME/.pyenv/versions/virtenv3 ]] ; then
        echo -en "\033[35m virtualenv3  not exists \033[0m\n"

        pip install virtualenv
        pyenv virtualenv -f virtenv2
        python -V
        pyenv virtualenvs
        pyenv versions
else
    	echo -en "\033[32m Python $PYTHONVER  and virtualenv3 exists \033[0m\n"
fi


cat << EOF >> $HOME/.bashrc
export PATH="/\$HOME/.pyenv/bin:\$PATH"
eval "\$(pyenv init -)"
eval "\$(pyenv virtualenv-init -)"
EOF

source $HOME/.bashrc


python -V
pyenv virtualenvs
pyenv versions



exit 0




