# PyERP [www.pyerp.cl](http://www.pyerp.cl)
PyERP is an project open-source, user-oriented, **ERP** system based on Django framework. If you want to help both as an **investor**, **partner** or as a **developer** send me email: mfalcon@ynext.cl :+1:.It is in development, it is not finished ,while we will upload videos so you can see our progress. Follow me [Youtube](https://www.youtube.com/channel/UCM93kgnjXu393jgKjjSkUjQ).

[Dcumentation](https://falconsoft3d.github.io/pyerp/)

# Deploy
```
apt-get update && apt-get upgrade -y
apt  install docker.io
sudo curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

```
docker-compose up -d --build
```

![Alt text](https://github.com/falconsoft3d/pyerp/blob/master/marketing/pyerp-m.png?raw=true "Ynext")

# Install PyERP using the following command
```
git clone https://github.com/falconsoft3d/pyerp
virtualenv env --python=python3
source env/bin/activate
cd pyerp
pip3 install -r requirements.txt
python manage.py init_pyerp
python manage.py runserver
```
   

# Modules Status
| #  | Module  | State | Project | Bugs | Date | Developer | Note |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 01 | [base](https://github.com/falconsoft3d/pyerp/tree/master/apps/base) | starting | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |
| 02 | [home](https://github.com/falconsoft3d/pyerp/tree/master/apps/home) | starting | [home](https://github.com/falconsoft3d/pyerp/projects/3) | - | - | [falconsoft3d](https://github.com/falconsoft3d)| - |
| 03 | [chat](https://github.com/falconsoft3d/pyerp/tree/master/apps/chat)  | starting | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |
| 04 | [crm](https://github.com/falconsoft3d/pyerp/tree/master/apps/crm)  | starting | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |
| 05 | [marketing](https://github.com/falconsoft3d/pyerp/tree/master/apps/marketing)  | starting | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |
| 06 | [pos](https://github.com/falconsoft3d/pyerp/tree/master/apps/pos)  | starting | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |
| 07 | [project](https://github.com/falconsoft3d/pyerp/tree/master/apps/project)  | starting | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |
| 08 | [purchase](https://github.com/falconsoft3d/pyerp/tree/master/apps/purchase) | starting | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |
| 09 | [sale](https://github.com/falconsoft3d/pyerp/tree/master/apps/sale)  | starting | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |
| 10 | [stock](https://github.com/falconsoft3d/pyerp/tree/master/apps/stock) | starting | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |
| 11 | [flow](https://github.com/falconsoft3d/pyerp/tree/master/apps/flow) | starting | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |
| 12 | [paypal](https://github.com/falconsoft3d/pyerp/tree/master/apps/paypal) | - | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |
| 13 | [payroll](https://github.com/falconsoft3d/pyerp/tree/master/apps/payroll) | starting | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |
| 14 | [odoo_api](https://github.com/falconsoft3d/pyerp/tree/master/apps/odoo_api) | - | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |
| 15 | [l10n_spain](https://github.com/falconsoft3d/pyerp/tree/master/apps/l10n_spain) | - | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |
| 16 | [l10n_chile](https://github.com/falconsoft3d/pyerp/tree/master/apps/l10n_chile) | - | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |
| 17 | [run_server](https://github.com/falconsoft3d/pyerp/tree/master/apps/run_server) | - | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |
| 18 | [academy](https://github.com/falconsoft3d/pyerp/tree/master/apps/academy) | - | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |
| 19 | [forum](https://github.com/falconsoft3d/pyerp/tree/master/apps/forum) | - | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |
| 20 | [bim](https://github.com/falconsoft3d/pyerp/tree/master/apps/bim) | - | [bim](https://github.com/falconsoft3d/pyerp/projects/2) | - | - | [falconsoft3d](https://github.com/falconsoft3d) | Construction Project Management Software  |
| 21 | [marketplace](https://github.com/falconsoft3d/pyerp/tree/master/apps/marketplace) | - | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |


# Feedback and Support
We welcome your feedback and support, raise issues if you want to see a new feature or report a bug.
https://github.com/falconsoft3d/pyerp/issues


# Screenshot
![Alt text](https://github.com/falconsoft3d/pyerp/blob/master/marketing/screenshot_pyerp_1.png?raw=true "Ynext")
![Alt text](https://github.com/falconsoft3d/pyerp/blob/master/marketing/screenshot_pyerp_2.jpg?raw=true "Ynext")
![Alt text](https://github.com/falconsoft3d/pyerp/blob/master/marketing/screenshot_pyerp_3.png?raw=true "Ynext")
![Alt text](https://github.com/falconsoft3d/pyerp/blob/master/marketing/screenshot_pyerp_4.png?raw=true "Ynext")
![Alt text](https://github.com/falconsoft3d/pyerp/blob/master/marketing/screenshot_pyerp_5.png?raw=true "Ynext")

# Who I am
My Name is Marlon Falcón Hernández. I am a Civil Engineer and Master in Architecture. I have worked for years in ERP development.
![Alt text](https://github.com/falconsoft3d/pyerp/blob/master/marketing/marlon-falcon-youtube.png?raw=true "Marlon")

# My contact data
```
Ynext | Marlon Falcón Hernández | Santiago de Chile | Chile
* ERP, CRM y Software: https://www.ynext.cl
» WhatsApp: +56 9 4299 4534
» Email: mfalcon@ynext.cl , falconsof.3d@gmail.com
» Instagram: https://www.instagram.com/ynextspa
» Facebook: https://www.facebook.com/Ynext-1150152835134897
» Github: https://github.com/falconsoft3d
» linkedin: https://linkedin.com/in/marlon-falcón-3a2aa9a4
» Support me Paypal: https://www.paypal.me/falconsoft3d
```

