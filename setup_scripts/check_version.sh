#! /bin/sh

echo "checking python & pip version"
python --version
pip --version

echo "checking node version"
node --version
npm --version
npx --version

echo "checking go version"
go version

echo "checking c++ version"
g++ --version
gcc --version
gdb --version
make --version

echo "checking TypeScript version"
tsc --version

echo "checking Java Version"
javac --version
java -version

echo "End of the Program"
