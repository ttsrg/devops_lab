#!/bin/bash
#Installing python

sudo yum install -y nano mc git
set -x
sudo -u vagrant -s --  <<EOF

PYTHONVER=3.7.1

if [[ ! -d \$HOME/.pyenv/versions/\$PYTHONVER ]] ; then
        echo -en "\033[35m python \$PYTHONVER    not exists \033[0m\n"
        sudo yum install -y curl zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel \
        openssl-devel xz xz-devel libffi-devel 1>/dev/null
	curl -L  https://raw.github.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash 1>/dev/null


        export PATH="\$HOME/.pyenv/bin:\$PATH"
        eval "\$(pyenv init -)"
        eval "\$(pyenv virtualenv-init -)"

        pyenv install -f  \$PYTHONVER 
        pyenv global  \$PYTHONVER 
        pip install --upgrade pip
	pip install wheel
        pip install virtualenv
        pyenv virtualenv -f virtenv3

elif [[ ! -L $HOME/.pyenv/versions/virtenv3 ]] ; then
        echo -en "\033[35m virtualenv3  not exists \033[0m\n"

        pyenv virtualenv -f virtenv3
        python -V
else
    	echo -en "\033[32m Python $PYTHONVER  and virtualenv3 exists \033[0m\n"
fi


PYTHONVER=2.7.15

if [[ ! -d \$HOME/.pyenv/versions/\$PYTHONVER ]] ; then
        echo -en "\033[35m python \$PYTHONVER    not exists \033[0m\n"
        sudo yum install -y curl zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite$
        openssl-devel xz xz-devel libffi-devel 1>/dev/null
        curl -L  https://raw.github.com/yyuu/pyenv-installer/master/bin/pyenv-installer | $


        export PATH="\$HOME/.pyenv/bin:\$PATH"
        eval "\$(pyenv init -)"
        eval "\$(pyenv virtualenv-init -)"

        pyenv install -f  \$PYTHONVER
#        pyenv global  \$PYTHONVER
        pip install --upgrade pip
        pip install wheel
        pip install virtualenv
        pyenv virtualenv -f virtenv2

elif [[ ! -L \$HOME/.pyenv/versions/virtenv2 ]] ; then
        echo -en "\033[35m virtualenv2  not exists \033[0m\n"

        pyenv virtualenv -f virtenv2
        python -V

else
    	echo -en "\033[32m Python \$PYTHONVER  and virtualenv2 exists \033[0m\n"
fi
EOF

python -V
pyenv virtualenvs
pyenv versions
                

#workaround
grep pyenv /home/vagrant/.bashrc
if [ "$?" != "0" ]; then
    echo nopyenvEXPORT
sudo -u vagrant -s --  <<EOF2
cat << EOF >> \$HOME/.bashrc
export PATH="\$HOME/.pyenv/bin:\$PATH"
EOF
EOF2
    echo "eval \$(pyenv init -)" >> /home/vagrant/.bashrc
    echo "eval \$(pyenv virtualenv-init -)" >> /home/vagrant/.bashrc
else
    echo EXPORTis
fi

cat /home/vagrant/.bashrc | grep init



set +x
exit 0

eval "\$\(pyenv init -\)"
eval "\$\(pyenv virtualenv-init -\)"
echo "\$\(pyenv virtualenv-init -\)" >> \$HOME/.bashrc
echo "eval \$(pyenv virtualenv-init -)" >> \$HOME/.bashrc




