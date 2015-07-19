# -*- coding: utf-8 -*-
# App Models.


class Field(object):
    """
    """
    def __init__(self,
                 nome,
                 tipo,
                 size,
                 requerid,
                 validator,
                 value,
                 desc_text,
                 help_text,
                 can_list,
                 can_search,
                 representation):
        """
        """
        self.nome = nome
        self.tipo = tipo
        self.size = size
        self.requerid = requerid
        self.validator = validator
        self.value = value
        self.desc_text = desc_text
        self.help_text = help_text
        self.can_list = can_list
        self.can_search = can_search
        self.representation = representation


class Usuario(object):
    __table__ = 'usuario'

    def __init__(self, id=None, login=None, senha=None, nivel_acesso=None):
        """
        """
        self.id = Field(nome='id',
                        tipo=int(),
                        size=int('8'),
                        requerid=True,
                        validator='requerid_number',
                        value=id,
                        desc_text='Id do Usuario',
                        help_text='Id do usuário com 20 posições',
                        can_list=True,
                        can_search=True,
                        representation=None)
        self.login = Field(nome='login',
                        tipo=str(),
                        size=int('150'),
                        requerid=True,
                        validator='requerid_str',
                        value=login,
                        desc_text='Login do Usuário',
                        help_text='Login do Usuário',
                        can_list=True,
                        can_search=True,
                        representation=None)
        self.senha = Field(nome='senha',
                        tipo=str(),
                        size=int('8'),
                        requerid=True,
                        validator='requerid_pwd',
                        value=senha,
                        desc_text='Senha do Usuário',
                        help_text='Senha do Usuário',
                        can_list=True,
                        can_search=False,
                        representation=None)
        self.nivel_acesso = Field(nome='nivel_acesso',
                                 tipo=int(),
                                 size=int('8'),
                                 requerid=True,
                                 validator='requerid_number',
                                 value=nivel_acesso,
                                 desc_text='Nível de acesso do Usuário',
                                 help_text='Nível de acesso do Usuário',
                                 can_list=False,
                                 can_search=False,
                                 representation=None)

    def get_class_name(self):
        """
        """
        return "Usuario"

    @classmethod
    def get_list_title(self):
        """
        """
        return "Listagem de Usuários"

    @classmethod
    def get_form_title(self):
        """
        """
        return "Usuário"

    @classmethod
    def get_default_field_order(self):
        """
        """
        return "login"

    @classmethod
    def exposed_search_properties(self):
        """
        """
        return [('all', 'Todos'),
                ('login', 'Login')]

    @classmethod
    def exposed_list_properties(self):
        """
        """
        colunms = ['Login']
        fields = ['login']
        attributes = {'colunms': colunms,
                      'fields': fields}
        return attributes

    def get_field_value(self, field):
        """
        """
        if hasattr(self, field):
            return getattr(self, field)

    def __str__(self):
        """
        """
        if self is not None:
            if self.login:
                return self.login

    @classmethod
    def save(self, form):
        """
        if not validate_id(form.id):
            try:
                entity = exists_entity(self.__table__, 'login', form.login)
                if (entity is not None):
                    raise AlreadyExistsValueException(form.login)
                else:
                    insert_id = db.insert(self.__table__,
                                          login = form.login,
                                          senha = form.senha,
                                         nivel_acesso = int(form.nivel_acesso))
            except IndexError:
                insert_id = db.insert(self.__table__,
                                      login = form.login,
                                      senha = form.senha,
                                      nivel_acesso = int(form.nivel_acesso))
        else:
            db.update(self.__table__,
                      where = "id=$id",
                      vars = locals(),
                      login = form.login,
                      senha = form.senha,
                      nivel_acesso = int(form.nivel_acesso))

        """
        pass

if __name__ == "__main__":
    import pdb;
    pdb.set_trace()
    leandro = Usuario(1, 'leandro', '12345', 2)
    print leandro
