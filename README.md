# PyERP
PyERP is an open-source, user-oriented, ERP system based on Django framework.

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
| #  | Module  | State | New mode | Translation | Bugs | Date | Note |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 01 | base  | starting | x | - | - | - | - |
| 02 | home  | starting | - | - | - | - | - |
| 03 | chat  | starting | - | - | - | - | - |
| 04 | crm  | starting | x | - | - | - | - |
| 05 | marketing  | starting | - | - | - | - | - |
| 06 | pos  | starting | x | - | - | - | - |
| 07 | project  | starting | x | - | - | - | - |
| 08 | purchase | starting | x | - | - | - | - |
| 09 | sale  | starting | - | - | - | - | - |
| 10 | stock | starting | - | - | - | - | - |
| 11 | flow | starting | - | - | - | - | - |
| 12 | paypal | starting | - | - | - | - | - |
| 13 | payroll | starting | x | - | - | - | - |
| 14 | odoo api | starting | - | - | - | - | - |
| 15 | l10n_spain | - | - | - | - | - | - |
| 16 | l10n_chile | - | - | - | - | - | - |
| 17 | run_server | - | - | - | - | - | - |
| 18 | academy | - | - | - | - | - | - |
| 19 | forum | - | - | - | - | - | - |

if you want to help send me email: mfalcon@ynext.cl

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

