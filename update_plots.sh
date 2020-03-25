git pull
git submodule update --recursive --remote
pushd src
python ita_new_cases.py
popd
