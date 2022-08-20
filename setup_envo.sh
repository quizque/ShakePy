#!/bin/sh

echo "ShakePi devloper environment setup script"

if [ -d "./src" ] 
then
    echo "Deleating tmp folder..."
    rm -r tmp/

    echo "Creating Python venv..."
    python3 -m venv tmp

    echo "Activating venv..."
    cd ./tmp/bin
    ./activate

    echo "Installing ShakePi"
    pip install -e ../../

     echo Done!
    echo "Make sure to select the virtual environment if your IDE supports it (VS Code)"
    exit

else
    echo "src/ folder doesn't exist! Make sure you are running this in the right directory."
fi