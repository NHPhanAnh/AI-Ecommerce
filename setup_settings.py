import os

services = [
    ('customer-service', 'customer_service', 'mysql', 'customer_db', '3306', 'root'),
    ('staff-service', 'staff_service', 'mysql', 'staff_db', '3306', 'root'),
    ('laptop-service', 'laptop_service', 'postgresql', 'laptop_db', '5432', 'user'),
    ('mobile-service', 'mobile_service', 'postgresql', 'mobile_db', '5432', 'user')
]

for folder, module, db_type, db_name, port, user in services:
    settings_path = os.path.join(r"C:\kiemtra01", folder, module, "settings.py")
    with open(settings_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Update INSTALLED_APPS
    content = content.replace(
        "'django.contrib.staticfiles',",
        "'django.contrib.staticfiles',\n    'app',\n    'rest_framework',"
    )

    # Update DATABASES
    old_db = "DATABASES = {\n    'default': {\n        'ENGINE': 'django.db.backends.sqlite3',\n        'NAME': BASE_DIR / 'db.sqlite3',\n    }\n}"
    
    db_config = f"""DATABASES = {{
    'default': {{
        'ENGINE': 'django.db.backends.{db_type}',
        'NAME': '{db_name}',
        'USER': '{user}',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '{port}',
    }}
}}"""
    
    content = content.replace(old_db, db_config)
    content = content.replace("ALLOWED_HOSTS = []", "ALLOWED_HOSTS = ['*']")

    with open(settings_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Settings updated successfully.")
