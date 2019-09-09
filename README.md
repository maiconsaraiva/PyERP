# PyERP
PyERP is an project open-source, user-oriented, **ERP** system based on Django framework. If you want to help both as an **investor**, **partner** or as a **developer** send me email: mfalcon@ynext.cl :+1:.
The first version will be released at the end of 2020. While we will upload videos so you can see our progress. Follow me [Youtube](https://www.youtube.com/channel/UCM93kgnjXu393jgKjjSkUjQ).

# Telegram Group (Pyerp)
https://t.me/pyerp

![Alt text](https://github.com/falconsoft3d/pyerp/blob/master/marketing/pyerp-m.png?raw=true "Ynext")

# Install PyERP using the following command
```
git clone https://github.com/falconsoft3d/pyerp
virtualenv env --python=python3
source env/bin/activate
cd pyerp
pip3 install -r requirements.txt
python manage.py runserver
```
    

# Modules Status
| #  | Module  | State | New mode | Translation | Bugs | Date | Developer | Note |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 01 | [base](https://github.com/falconsoft3d/pyerp/tree/master/apps/base) | starting | x | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |
| 02 | [home](https://github.com/falconsoft3d/pyerp/tree/master/apps/home) | starting | - | - | - | - | [falconsoft3d](https://github.com/falconsoft3d)| - |
| 03 | [chat](https://github.com/falconsoft3d/pyerp/tree/master/apps/chat)  | starting | - | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |
| 04 | [crm](https://github.com/falconsoft3d/pyerp/tree/master/apps/crm)  | starting | x | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |
| 05 | [marketing](https://github.com/falconsoft3d/pyerp/tree/master/apps/marketing)  | starting | - | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |
| 06 | [pos](https://github.com/falconsoft3d/pyerp/tree/master/apps/pos)  | starting | x | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |
| 07 | [project](https://github.com/falconsoft3d/pyerp/tree/master/apps/project)  | starting | x | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |
| 08 | [purchase](https://github.com/falconsoft3d/pyerp/tree/master/apps/purchase) | starting | x | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |
| 09 | [sale](https://github.com/falconsoft3d/pyerp/tree/master/apps/sale)  | starting | - | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |
| 10 | [stock](https://github.com/falconsoft3d/pyerp/tree/master/apps/stock) | starting | - | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |
| 11 | [flow](https://github.com/falconsoft3d/pyerp/tree/master/apps/flow) | starting | - | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |
| 12 | [paypal](https://github.com/falconsoft3d/pyerp/tree/master/apps/paypal) | starting | - | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |
| 13 | [payroll](https://github.com/falconsoft3d/pyerp/tree/master/apps/payroll) | starting | x | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |
| 14 | [odoo_api](https://github.com/falconsoft3d/pyerp/tree/master/apps/odoo_api) | starting | - | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |
| 15 | [l10n_spain](https://github.com/falconsoft3d/pyerp/tree/master/apps/l10n_spain) | - | - | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |
| 16 | [l10n_chile](https://github.com/falconsoft3d/pyerp/tree/master/apps/l10n_chile) | - | - | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |
| 17 | [run_server](https://github.com/falconsoft3d/pyerp/tree/master/apps/run_server) | - | - | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |
| 18 | [academy](https://github.com/falconsoft3d/pyerp/tree/master/apps/academy) | - | - | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |
| 19 | [forum](https://github.com/falconsoft3d/pyerp/tree/master/apps/forum) | - | - | - | - | - | [falconsoft3d](https://github.com/falconsoft3d) | - |

# Rules for Developers
1- all apps with namespace urls.py
```
app_name = 'crm'
```
2- Translation
Translation in the Templates
```
<p>{{ _('Project') }}</p>
```
Traslation in the models
```
name = models.CharField(_("Name"), max_length=80)
```
Traslation in the Views
```
COUNTRY_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
]
```
3- Alls Apps need this file
info.json
```
{
	"name": "Chat",
	"version":"1.0.0.1",
	"author": "YnexT SpA",
	"website": "www.ynext.cl",
	"category": "Accounting",
	"summary": "Account",
	"depends": "",
	"description": "Demo Hello",
	"external_dependencies":"",
	"type":"public",
	"color":"bg-success",
	"fa":"fa-comments",
	"sequence":"10"
}

```

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

# Feedback and Support
We welcome your feedback and support, raise issues if you want to see a new feature or report a bug.
https://github.com/falconsoft3d/pyerp/issues


# Screenshot
![Alt text](https://github.com/falconsoft3d/pyerp/blob/master/marketing/05.png?raw=true "Ynext")
![Alt text](https://github.com/falconsoft3d/pyerp/blob/master/marketing/01.png?raw=true "Ynext")
![Alt text](https://github.com/falconsoft3d/pyerp/blob/master/marketing/02.png?raw=true "Ynext")
![Alt text](https://github.com/falconsoft3d/pyerp/blob/master/marketing/03.png?raw=true "Ynext")
![Alt text](https://github.com/falconsoft3d/pyerp/blob/master/marketing/04.png?raw=true "Ynext")

