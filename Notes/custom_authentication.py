'''
how can I custom authentication for my project?
To solve this problem,many tutorials have been referenced,including django's offical document.
To fear of taking detours,I recorded the process:
'''
# step 1:
#     define a class that used as authentication backend,and in the class you need to implement
# two methods:authenticae and get_user.
#     the structure of the class is familar with following:


    class CustomBackend:
    def authenticate(self,request,username=None,password=None):
        ...
                           
    def get_user(self,user_id):
        ...

# step 2:
#     specifing backend for your project.It is allowed if there are two or more backends in your project,but in
# the case,you should deal with it more carefully.here, I emphasize that the order of backends is important.
# To specify backend,you need to modify the settings.py.You need to override the var 'AUTHENTICATION_BACKEDNS'
# All you need to do exactly is just add the following into settings.py:
AUTHENTICATION_BACKENDS=[
    'value' ,###attention please,the value is path of CustomBackend
]

# step 3:
# If you want to use the backend you have defined,you need to instantiate for the CustomBackend   