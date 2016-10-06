Install django
Install django-bootstrap-forms
- https://github.com/tzangms/django-bootstrap-form
- Add ‘bootstrapform’ in INSTALLED_APPS (settings.py)
Install django-mptt:
- git clone git://github.com/django-mptt/django-mptt.git
- cd django-mptt
- python setup install 
- add ‘mptt’ in INSTALLED_APPS (settings.py)
Install django-mptt-admin
- https://github.com/mbraak/django-mptt-admin
- $ pip install django-mptt-admin
- add ‘django-mptt-admin’ in INSTALLED_APPS (settings.py)

Add library

First ‘jQuery’
<script data-require="jquery@2.1.1" data-semver="2.1.1" src="//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
Next ‘Bootstrap’
<link href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0//css/bootstrap.min.css" rel="stylesheet">
<script data-require="bootstrap@3.2.0" data-semver="3.2.0" src="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.js"></script>

Add plugin

Change alert to sweetAlert (swal)
download from http://t4t5.github.io/sweetalert/ or ‘$ npm install sweetalert’

Add datepicker for Bootstrap
download from http://www.eyecon.ro/bootstrap-datepicker/#
<script src="{% static 'datepicker/js/bootstrap-datepicker.js' %}"></script>
<link rel="stylesheet" type="text/css" href="{% static 'datepicker/css/datepicker.css' %}">