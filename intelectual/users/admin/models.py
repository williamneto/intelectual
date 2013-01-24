# -*- coding: utf-8 -*-
import sys
import re
import datetime

from constants import *

from mongoengine import *
from mongoengine.queryset import QuerySet
from django.core.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.signals import user_logged_in, user_logged_out
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
    
    def register_historic(self, object, action, use_ehit=False, ehit_minutes=5):
        """
        Salva historico

        se utilizar `use_ehit`
        procura pela mesma acao 5 minutos antes
        se encontrada incrementa o numero de ehits (extra hits)
        assim nao ocorre o risco de entupir o banco de dados ou uma
        falha de segurança que permita entupir o db
        """
        now = datetime.datetime.now()
        
        if use_ehit:
            min_time = now - datetime.timedelta(minutes=ehit_minutes)

            log = Historic.objects(action=action, obj_ref=object,
                                   user=self,
                                   dtime__gte=min_time,
                                   dtime__lte=now).first()

            if log:
                if not log.ehits:
                    log.ehits = 1
                else:
                    log.ehits += 1

                log.dtime = now
                log.save(cascade=False)
                return log

        log = Historic(action=action, obj_ref=object, 
                       user=self)

        if isinstance(self, UnidadeProfile):
            log.unid = self.unidade

        log.save(cascade=False)
        return log

    def has_perm(self, perm):
        if self.is_superuser and self.is_active:
            return True

        return False

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
            

    def has_perm(self, perm):
        return True
    
    def clean(self):
        self.clean_email()
        self.clean_username()
        
    def get_absolute_url(self):
        return "/admin/superusers/%s/" % str(self.pk)

class Historic(Document):
    """
    Histórico de Acesso
    """
    user =  ReferenceField(User, dbref=True)
    unid = ReferenceField(Unidade, dbref=True)
    action = StringField()
    obj_ref = GenericReferenceField(db_field="objRef")
    obj_name = StringField(db_field="objName")
    dtime = DateTimeField(default=datetime.datetime.now)
    ehits = IntField()

    @classmethod
    def get_label_for_module(cls, module, action):
        """
        Usado para buscar o label de ação
        """

        #custom action
        if module in HISTORIC_CUSTOM_ACTIONS:
            actions = HISTORIC_CUSTOM_ACTIONS[module]
            
            if action in actions:
                return actions[action]
        
        if (action in HISTORIC_GENERIC_ACTION_LABELS and
            module not in HISTORIC_EXCLUDE_COMMON_MODULES):
            return HISTORIC_GENERIC_ACTION_LABELS[action]

    @property
    def action_parts(self):
        if self.action:
            return self.action.split('.', 1)
        return None, None

    @property
    def module(self):
        return self.action_parts[0]

    def get_module_label(self):
        if self.module:
            return HISTORIC_MODULES_NAMES[self.module]

    def get_action_label(self):
        mod, action = self.action_parts
        return self.get_label_for_module(mod, action)

    def get_user(self):
        if self.user and isinstance(self.user, Document):
            return self.user
        return u"Usuário Removido"

    def get_dtime_display(self):
        return self.dtime.strftime("%d/%m/%Y %H:%M:%S")

    @property
    def object(self):
        if self.obj_ref:
            if isinstance(self.obj_ref, Document):
                return self.obj_ref
            return "Objeto Removido"
        elif self.obj_name:
            return self.obj_name

    @object.setter
    def object(self, obj):
        self.obj_ref = obj

    def get_absolute_url(self):
        if self.obj_ref and hasattr(self.obj_ref,
                                    'get_absolute_url'):
            return self.obj_ref.get_absolute_url()

    def save(self, *args, **kwargs):
        if self.obj_ref and hasattr(self.obj_ref, '__unicode__'):
            self.obj_name = self.obj_ref.__unicode__()

        return super(Historic, self).save(*args, **kwargs)
        

    meta = {'allow_inheritance': False,
            'collection': 'log',
            'indexes': ['action']
            }
