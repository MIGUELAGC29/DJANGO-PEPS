from django import forms
from Login.models import Usuario



 
        

class FormularioUsuario(forms.ModelForm):
    """ Formulario de Registro de un usuario en la base e datos
    
    
        Variables:
        
            - password1 : Contraseña
            - password2 : Verificacion
    """
    
    password1 = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Ingrese su contraseña...',
            'id' : 'password1',
            'required' : 'required',
        }
    ))
    
    password2 = forms.CharField(label = 'Contraseña de confirmación', widget = forms.PasswordInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Ingrese su contraseña...',
            'id' : 'password2',
            'required' : 'required',
        }
    ))
    
    class Meta:
        model = Usuario
        fields = ('email', 'username', 'nombres', 'apellidos')
        widgets = {
            'email' : forms.EmailInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Correo Electronico',
                }
            ),
            'nombres' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese su nombre',
                }
            ),
            'apellidos' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese sus apellidos',
                }
            ),
            'username' : forms.NumberInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese su nombre',
                }
            )
        }
        
        
    def clean_password2(self):
        """ Validación de Contraseña
        
        Metodo que valida que ambas contraseñas ingresadas sean igual, esto antes de ser encriptadas y guardadas en la base de datos, 
        Retornar la contraseña válida
        
        Excepciones:
        - ValidationError -- cuando las contraseñas no son iguales muestra mensaje de error
        
        """
        
        
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden')
        return password2
    
    
    def save(self,commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
        