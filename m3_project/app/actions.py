import datetime

from django.contrib.auth.models import Group, User, Permission
from django.contrib.contenttypes.models import ContentType, ContentTypeManager
from m3.actions import ActionPack
from m3_ext.ui import all_components as ext
from objectpack.actions import ObjectPack
from objectpack.ui import BaseEditWindow
from objectpack.ui import ModelEditWindow

from .controller import observer


class ContentTypeActionPack(ObjectPack):
    model = ContentType

    add_to_menu = True
    add_window = edit_window = ModelEditWindow.fabricate(model=ContentType)

class UserEditWindow(BaseEditWindow):

    def _init_components(self):
        """
        Здесь следует инициализировать компоненты окна и складывать их в
        :attr:`self`.
        """
        super(UserEditWindow, self)._init_components()

        self.field__password = ext.ExtStringField(
            label=u'password',
            name='password',
            allow_blank=False,
            anchor='100%')

        self.field__last_login = ext.ExtDateField(
            label=u'last login',
            name='last_login',
            allow_blank=True,
            anchor='100%')

        self.field__superuser = ext.ExtCheckBox(
            label=u'superuser status',
            name='superuser_status',
            anchor='100%')

        self.field__username = ext.ExtStringField(
            label=u'username',
            name='username',
            allow_blank=False,
            anchor='100%')

        self.field__first_name = ext.ExtStringField(
            label=u'first name',
            name='first_name',
            allow_blank=True,
            anchor='100%')

        self.field__last_name = ext.ExtStringField(
            label=u'last name',
            name='last_name',
            allow_blank=True,
            anchor='100%')

        self.field__email = ext.ExtStringField(
            label=u'email address',
            name='email_address',
            allow_blank=True,
            anchor='100%')

        self.field__staff_status = ext.ExtCheckBox(
            label=u'staff status',
            name='staff_status',
            anchor='100%')

        self.field__active = ext.ExtCheckBox(
            label=u'active',
            name='active',
            checked=True,
            anchor='100%')

        self.field__joined = ext.ExtDateField(
            label=u'date joined',
            name='date_joined',
            allow_blank=False,
            format='d.m.Y',
            value='{d}.{m}.{y}'.format(
                d=datetime.date.today().day,
                m=datetime.date.today().month,
                y=datetime.date.today().year),
            anchor='100%')

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(UserEditWindow, self)._do_layout()
        self.form.items.extend((
            self.field__password,
            self.field__last_login,
            self.field__superuser,
            self.field__username,
            self.field__first_name,
            self.field__last_name,
            self.field__email,
            self.field__staff_status,
            self.field__active,
            self.field__joined
        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(UserEditWindow, self).set_params(params)
        self.height = 'auto'


class UserActionPack(ObjectPack):
    model = User

    add_to_menu = True
    add_window = edit_window = UserEditWindow


class GroupActionPack(ObjectPack):
    model = Group

    add_to_menu = True
    add_window = edit_window = ModelEditWindow.fabricate(model=Group)


class PermissionActionPack(ObjectPack):
    model = Permission

    add_to_menu = True
    add_window = edit_window = ModelEditWindow.fabricate(
        model=Permission,
        model_register=observer
                                                         )
