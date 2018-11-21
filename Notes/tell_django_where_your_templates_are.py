# how django can find your templates?
# here are the process.
# step 1:
#   touch a directroy named "templates"
#there two conditions:
#   ①if the templates are used as common,you'd better touch the "templates" at the same directory with app.
#   ②if the templates are custom-made for a specified app,you need to touch the "templates"  in the app directory.


#step 2:
#  telling django where your templates are.
# in the settings.py, find a var named TEMPLATES

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
#modify one of the records
'DIRS':[
    os.path.join(BASE_DIR,'templates'),
]

#that is all.
