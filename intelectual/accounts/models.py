# -*- coding: utf-8 -*-
import re
import datetime


from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_str
from django.utils.hashcompat import md5_constructor, sha_constructor

from django.conf import settings

username_re = re.compile("^[a-z0-9_-]{3,15}$")

def get_hexdigest(algorithm, salt, raw_password):
    raw_password, salt = smart_str(raw_password), smart_str(salt)
    if algorithm == 'md5':
        return md5_constructor(salt + raw_password).hexdigest()
    elif algorithm == 'sha1':
        return sha_constructor(salt + raw_password).hexdigest()
    raise ValueError('Got unknown password algorithm type in password') 

class User(Document):
    """
    Classe base de acesso ao sistema
    A User document that aims to mirror most of the API specified by Django
    at http://docs.djangoproject.com/en/dev/topics/auth/#users
    """
    username = StringField(max_length=30, required=True, unique=True,
                           verbose_name=_('Username'),
                           help_text=_("Obrigatorio. 30 caracteres. Letras,numero e @/./+/-/_ <br>"))
    first_name = StringField(max_length=30,
                             verbose_name=_('Primeiro nome'))
    last_name = StringField(max_length=30,
                            verbose_name=_('Ultimo nome'))
    email = EmailField(unique=True,
                       verbose_name=_('Email'))
    admin = BooleanField(default=False)
    password = StringField(max_length=128)
    is_staff = BooleanField(default=False)
    is_active = BooleanField(default=True,
                             verbose_name=_('Usuario ativo'))
    is_superuser = BooleanField(default=False,
                                verbose_name=_('superuser status'),
                                help_text=_("Designates that this user has all permissions without explicitly assigning them."))
    editable = BooleanField(default=True,
                            verbose_name="O usuário é editável")
    last_login = DateTimeField(default=datetime.datetime.now)
    date_joined = DateTimeField(default=datetime.datetime.now)

    editable = BooleanField(default=True,
                            verbose_name="O usuário é editável")

    meta = {
        'allow_inheritance': True,
        'indexes': [
            {'fields': ['username', 'email'], 'unique': True}
        ]
    }

    def __unicode__(self):
        return self.username

    def get_full_name(self):
        """Returns the users first and last names, separated by a space.
        """
        full_name = u'%s %s' % (self.first_name or '', self.last_name or '')
        return full_name.strip()

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
    

    def set_password(self, raw_password, commit=True):
        """Sets the user's password - always use this rather than directly
        assigning to :attr:`~mongoengine.django.auth.User.password` as the
        password is hashed before storage.
        """
        from random import random
        algo = 'sha1'
        salt = get_hexdigest(algo, str(random()), str(random()))[:5]
        hash = get_hexdigest(algo, salt, raw_password)
        self.password = '%s$%s$%s' % (algo, salt, hash)

        if commit:
            self.save()

        return self

    def check_password(self, raw_password):
        """Checks the user's password against a provided password - always use
        this rather than directly comparing to
        :attr:`~mongoengine.django.auth.User.password` as the password is
        hashed before storage.
        """
        algo, salt, hash = self.password.split('$')
        return hash == get_hexdigest(algo, salt, raw_password)

    @classmethod
    def create_user(cls, username, password, email=None):
        """Create (and save) a new user with the given username, password and
        email address.
        """
        now = datetime.datetime.now()

        # Normalize the address by lowercasing the domain part of the email
        # address.
        if email is not None:
            try:
                email_name, domain_part = email.strip().split('@', 1)
            except ValueError:
                pass
            else:
                email = '@'.join([email_name, domain_part.lower()])

        user = User(username=username, email=email, date_joined=now)
        user.set_password(password)
        user.save()
        return user

    def get_and_delete_messages(self):
        return []
    
    def get_hour_step(self):
        return settings.HORARIO_HOUR_STEP

class AdminProfile(User):
    is_admin = True

    def clean_email(self):
        """
        procura se existem emails iguais a o que esteja desejando salvar
        caso encontre nenhum continue
        se caso for o proprio no caso de salvar um existe também continue
        caso contrario (existe mais nao e o proprio) = alerta o erro
        """
        try:
            profiles = User.objects.filter(email=self.email)
        except ObjectDoesNotExist:
            return User.clean(self)

        if profiles.count() == 0:
            return

        for p in profiles:
            if self.id == p.id:
                return

        raise ValidationError("Não é possivel inserir um administrador com um endereço de email existente")

    def clean_username(self):
        if not username_re.match(self.username):
            raise ValidationError("Por favor informe um usuário válido, "
                                  "sem espaços contendo apenas letras minusculas, números, hífens e underlines")
    
    def clean(self):
        self.clean_email()
        self.clean_username()
        
    def get_absolute_url(self):
        return "/admin/superusers/%s/" % str(self.pk)
