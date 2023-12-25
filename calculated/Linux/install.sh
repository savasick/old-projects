#!/bin/bash
echo "Add calculated to applications"
echo "Install python"
sudo apt install python3 python3-pip
echo "install requirements"
pip3 install -r requirements.txt

echo "Making Desktop file"
echo "[Desktop Entry]" >> calculated.desktop
echo "Name=calculated" >> calculated.desktop
echo "Version=v0.8.5" >> calculated.desktop
echo "Icon=$PWD/calculator.png" >> calculated.desktop
echo "Exec=$PWD/calculated.py" >> calculated.desktop
echo "Terminal=false" >> calculated.desktop
echo "Type=Application" >> calculated.desktop
echo "Add permission"
chmod a+x calculated.py
chmod a+x calculated.desktop
chmod a+x calculator.png
chown $USER:$USER calculated.py
chown $USER:$USER calculated.desktop
chown $USER:$USER calculator.png


#gio set $PWD/calculated.desktop "metadata::trusted" yes
#dbus-launch gio set $PWD/calculated.desktop "metadata::trusted" true
#gio set $PWD/calculator.png "metadata::trusted" yes
#dbus-launch gio set $PWD/calculator.png "metadata::trusted" true
# for kali linux
echo "Trust app"
f=$PWD/calculated.desktop; gio set -t string "$f" metadata::xfce-exe-checksum "$(sha256sum "$f" | awk '{print $1}')"
echo "Add to Desktop"
sudo cp ./calculated.desktop $HOME/Desktop
f=$HOME/Desktop/calculated.desktop; gio set -t string "$f" metadata::xfce-exe-checksum "$(sha256sum "$f" | awk '{print $1}')"
echo "Add to applications"
sudo cp ./calculated.desktop $HOME/.local/share/applications/
f=$HOME/.local/share/applications/calculated.desktop; gio set -t string "$f" metadata::xfce-exe-checksum "$(sha256sum "$f" | awk '{print $1}')"
echo "Done"