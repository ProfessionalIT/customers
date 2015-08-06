"""
HTML forms
(part of web.py)
"""

import copy, re, cgi
import webapi as web
import utils, net

import logging

def attrget(obj, attr, value=None):
    if hasattr(obj, 'has_key') and obj.has_key(attr): return obj[attr]
    if hasattr(obj, attr): return getattr(obj, attr)
    return value

class Form:
    r"""
    HTML form.
    
        >>> f = Form(Textbox("x"))
        >>> f.render()
        '<table>\n    <tr><th><label for="x">x</label></th><td><input type="text" id="x" name="x"/></td></tr>\n</table>'
    """
    def __init__(self, *inputs, **kw):
        self.inputs = inputs
        self.valid = True
        self.note = None
        self.validators = kw.pop('validators', [])

    def __call__(self, x=None):
        o = copy.deepcopy(self)
        if x: o.validates(x)
        return o
    
    def render(self):
        out = ''
        out += self.rendernote(self.note)
        out += '<table>\n'
        
        for i in self.inputs:
            html = i.pre + i.render() + self.rendernote(i.note) + i.post
            if i.is_hidden():
                out += '    <tr style="display: none;"><th></th><td>%s</td></tr>\n' % (html)
            else:
                out += '    <tr><th><label for="%s">%s</label></th><td>%s</td></tr>\n' % (i.id, net.websafe(i.description), html)
        out += "</table>"
        return out
        
    def render_css(self): 
        out = [] 
        out.append(self.rendernote(self.note)) 
        for i in self.inputs:
            if not i.is_hidden() and not isinstance(i,Button) and not isinstance(i,CustomLink):
                out.append('<label for="%s">%s</label>' % (i.id, net.websafe(i.description))) 
            elif isinstance(i,CustomLink):
                out.append('<label class="nodisplay"></label>') 
            out.append(i.pre)
            out.append(i.render()) 
            out.append(self.rendernote(i.note))
            out.append(i.post) 
            out.append('\n')
        return ''.join(out) 

    def rendernote(self, note):
        if note: return '<strong class="wrong">%s</strong>' % net.websafe(note)
        else: return ""
    
    def validates(self, source=None, _validate=True, **kw):
        source = source or kw or web.input()
        out = True
        for i in self.inputs:
            v = attrget(source, i.name)
            if _validate:
                out = i.validate(v) and out
            else:
                i.value = v
        if _validate:
            out = out and self._validate(source)
            self.valid = out
        return out

    def _validate(self, value):
        self.value = value
        for v in self.validators:
            if not v.valid(value):
                self.note = v.msg
                return False
        return True

    def fill(self, source=None, **kw):
        return self.validates(source, _validate=False, **kw)
    
    def __getitem__(self, i):
        for x in self.inputs:
            if x.name == i: return x
        raise KeyError, i

    def __getattr__(self, name):
        # don't interfere with deepcopy
        inputs = self.__dict__.get('inputs') or []
        for x in inputs:
            if x.name == name: return x
        raise AttributeError, name
    
    def get(self, i, default=None):
        try:
            return self[i]
        except KeyError:
            return default
            
    def _get_d(self): #@@ should really be form.attr, no?
        return utils.storage([(i.name, i.get_value()) for i in self.inputs])
    d = property(_get_d)

class Input(object):
    def __init__(self, name, *validators, **attrs):
        self.name = name
        self.validators = validators
        self.attrs = attrs = AttributeList(attrs)
        
        self.description = attrs.pop('description', name)
        self.value = attrs.pop('value', None)
        self.pre = attrs.pop('pre', "")
        self.post = attrs.pop('post', "")
        self.note = None
        
        self.id = attrs.setdefault('id', self.get_default_id())
        
        if 'class_' in attrs:
            attrs['class'] = attrs['class_']
            del attrs['class_']
        
    def is_hidden(self):
        return False
        
    def get_type(self):
        raise NotImplementedError
        
    def get_default_id(self):
        return self.name

    def validate(self, value):
        self.set_value(value)

        for v in self.validators:
            if not v.valid(value):
                self.note = v.msg
                return False
        return True

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def render(self):
        attrs = self.attrs.copy()
        attrs['type'] = self.get_type()
        if self.value is not None:
            attrs['value'] = self.value
        attrs['name'] = self.name
        return '<input %s/>' % attrs

    def rendernote(self, note):
        if note: return '<strong class="wrong">%s</strong>' % net.websafe(note)
        else: return ""
        
    def addatts(self):
        # add leading space for backward-compatibility
        return " " + str(self.attrs)

class AttributeList(dict):
    """List of atributes of input.
    
    >>> a = AttributeList(type='text', name='x', value=20)
    >>> a
    <attrs: 'type="text" name="x" value="20"'>
    """
    def copy(self):
        return AttributeList(self)
        
    def __str__(self):
        return " ".join(['%s="%s"' % (k, net.websafe(v)) for k, v in self.items()])
        
    def __repr__(self):
        return '<attrs: %s>' % repr(str(self))

class Textbox(Input):
    """Textbox input.
    
        >>> Textbox(name='foo', value='bar').render()
        '<input type="text" id="foo" value="bar" name="foo"/>'
        >>> Textbox(name='foo', value=0).render()
        '<input type="text" id="foo" value="0" name="foo"/>'
    """        
    def get_type(self):
        return 'text'

class Password(Input):
    """Password input.

        >>> Password(name='password', value='secret').render()
        '<input type="password" id="password" value="secret" name="password"/>'
    """
    
    def get_type(self):
        return 'password'

class Textarea(Input):
    """Textarea input.
    
        >>> Textarea(name='foo', value='bar').render()
        '<textarea id="foo" name="foo">bar</textarea>'
    """
    def render(self):
        attrs = self.attrs.copy()
        attrs['name'] = self.name
        value = net.websafe(self.value or '')
        return '<textarea %s>%s</textarea>' % (attrs, value)

class Dropdown(Input):
    r"""Dropdown/select input.
    
        >>> Dropdown(name='foo', args=['a', 'b', 'c'], value='b').render()
        '<select id="foo" name="foo">\n  <option value="a">a</option>\n  <option selected="selected" value="b">b</option>\n  <option value="c">c</option>\n</select>\n'
        >>> Dropdown(name='foo', args=[('a', 'aa'), ('b', 'bb'), ('c', 'cc')], value='b').render()
        '<select id="foo" name="foo">\n  <option value="a">aa</option>\n  <option selected="selected" value="b">bb</option>\n  <option value="c">cc</option>\n</select>\n'
    """
    def __init__(self, name, args, *validators, **attrs):
        self.args = args
        super(Dropdown, self).__init__(name, *validators, **attrs)

    def render(self):
        attrs = self.attrs.copy()
        attrs['name'] = self.name
        
        x = '<select %s>\n' % attrs
        
        for arg in self.args:
            if isinstance(arg, (tuple, list)):
                value, desc= arg
            else:
                value, desc = arg, arg 
            if str(self.value) == value.decode('utf8'): 
                select_p = ' selected="selected"'
            elif str(self.value) == str(value):
                select_p = ' selected="selected"'
            else: select_p = ''
            
            x += '  <option%s value="%s">%s</option>\n' % (select_p, net.websafe(value), net.websafe(desc))
            logging.debug('O COMBO: ' + x)
        x += '</select>\n'
        return x

class Radio(Input):
    def __init__(self, name, args, *validators, **attrs):
        self.args = args
        super(Radio, self).__init__(name, *validators, **attrs)

    def render(self):
        x = '<span>'
        for arg in self.args:
            if isinstance(arg, (tuple, list)):
                value, desc= arg
            else:
                value, desc = arg, arg 
            attrs = self.attrs.copy()
            attrs['name'] = self.name
            attrs['type'] = 'radio'
            attrs['value'] = arg
            if self.value == arg:
                attrs['checked'] = 'checked'
            x += '<input %s/> %s' % (attrs, net.websafe(desc))
        x += '</span>'
        return x

class Checkbox(Input):
    """Checkbox input.

    >>> Checkbox('foo', value='bar', checked=True).render()
    '<input checked="checked" type="checkbox" id="foo_bar" value="bar" name="foo"/>'
    >>> Checkbox('foo', value='bar').render()
    '<input type="checkbox" id="foo_bar" value="bar" name="foo"/>'
    >>> c = Checkbox('foo', value='bar')
    >>> c.validate('on')
    True
    >>> c.render()
    '<input checked="checked" type="checkbox" id="foo_bar" value="bar" name="foo"/>'
    """
    def __init__(self, name, *validators, **attrs):
        self.checked = attrs.pop('checked', False)
        Input.__init__(self, name, *validators, **attrs)
        
    def get_default_id(self):
        value = utils.safestr(self.value or "")
        return self.name + '_' + value.replace(' ', '_')

    def render(self):
        attrs = self.attrs.copy()
        attrs['type'] = 'checkbox'
        attrs['name'] = self.name
        attrs['value'] = self.value

        if self.checked:
            attrs['checked'] = 'checked'            
        return '<input %s/>' % attrs

    def set_value(self, value):
        self.checked = bool(value)

    def get_value(self):
        return self.checked

class MultiCheckbox(Input):
    """MultiCheckbox input.

    >>> the_values = [('1', 'foo'), ('2', 'bar'), ('3', 'baz')]

    >>> print MultiCheckbox('vars', the_values).render()
    <input type="checkbox" id="vars_1" value="1" name="vars"/> foo<br />
    <input type="checkbox" id="vars_2" value="2" name="vars"/> bar<br />
    <input type="checkbox" id="vars_3" value="3" name="vars"/> baz

    >>> print MultiCheckbox('vars', the_values, checked=['2', '3']).render()
    <input type="checkbox" id="vars_1" value="1" name="vars"/> foo<br />
    <input checked="checked" type="checkbox" id="vars_2" value="2" name="vars"/> bar<br />
    <input checked="checked" type="checkbox" id="vars_3" value="3" name="vars"/> baz

    Mock web.input for testing ::

    >>> def myinput(*args, **kargs):
    ...     return dict(vars=[u'1', u'2'])
    >>> web.input = myinput 

    >>> c = MultiCheckbox('vars', the_values)
    >>> c.validate([])
    True
    >>> c.validate('vars')
    True
    >>> c.get_value()
    [u'1', u'2']
    >>> print c.render()
    <input checked="checked" type="checkbox" id="vars_1" value="1" name="vars"/> foo<br />
    <input checked="checked" type="checkbox" id="vars_2" value="2" name="vars"/> bar<br />
    <input type="checkbox" id="vars_3" value="3" name="vars"/> baz
    """
    def __init__(self, name, args, *validators, **attrs):
        self.args = args
        self.checked = attrs.pop('checked', list())
        super(MultiCheckbox, self).__init__(name, *validators, **attrs)

    def get_default_id(self, value='id'):
        return self.name + '_' + value.replace(' ', '_')

    def render(self):
        result = list()
        for arg in self.args:
            if isinstance(arg, (tuple, list)):
                value, desc = arg
            else:
                value, desc = str(arg), str(arg)
            attrs = self.attrs.copy()
            attrs.update(
                dict(type='checkbox', name=self.name, value=value, 
                     id=self.get_default_id(value)))
            if value in self.checked:
                attrs['checked'] = 'checked'
            result.append('<input class="multicheckbox" %s/> %s' % (attrs, desc))
        return ''.join(result)
        #return '\t'.join(result)

    def set_value(self, value):
        pass

    def get_value(self):
        return self.checked

    # we don't care about the value as we need a special access to web.input
    # maybe we could add a method to each form field to tell the form if it
    # need special retrieval (like telling the form it is a list value or not)
    def validate(self, value=None):
        params = {self.name: list()}
        checked = web.input(**params)[self.name]
        self.checked = checked

        for v in self.validators:
            if not v.valid(checked):
                self.note = v.msg
                return False
        return True

class Button(Input):
    """HTML Button.
    
    >>> Button("save").render()
    '<button id="save" name="save">save</button>'
    >>> Button("action", value="save", html="<b>Save Changes</b>").render()
    '<button id="action" value="save" name="action"><b>Save Changes</b></button>'
    """
    def __init__(self, name, *validators, **attrs):
        super(Button, self).__init__(name, *validators, **attrs)
        self.description = ""

    def render(self):
        attrs = self.attrs.copy()
        attrs['name'] = self.name
        if self.value is not None:
            attrs['value'] = self.value
        html = attrs.pop('html', None) or net.websafe(self.name)
        return '<button %s>%s</button>' % (attrs, html)

class CustomLink(Input):
    """HTML Link.
    
    >>> Button("save").render()
    '<button id="save" name="save">save</button>'
    >>> Button("action", value="save", html="<b>Save Changes</b>").render()
    '<button id="action" value="save" name="action"><b>Save Changes</b></button>'
    """
    def __init__(self, name, *validators, **attrs):
        super(CustomLink, self).__init__(name, *validators, **attrs)
        self.description = ""

    def render(self):
        attrs = self.attrs.copy()
        attrs['name'] = self.name
        if self.value is not None:
            attrs['value'] = self.value
        html = attrs.pop('html', None) or net.websafe(self.name)
        link = attrs.pop('link', None) or net.websafe(self.name)
        return "<a href='%s' target='_blank' class='custom_link'>%s</a>" % (link, html)

class Hidden(Input):
    """Hidden Input.
    
        >>> Hidden(name='foo', value='bar').render()
        '<input type="hidden" id="foo" value="bar" name="foo"/>'
    """
    def is_hidden(self):
        return True
        
    def get_type(self):
        return 'hidden'

class File(Input):
    """File input.
    
        >>> File(name='f').render()
        '<input type="file" id="f" name="f"/>'
    """
    def get_type(self):
        return 'file'

    def set_value(self, value):
        self.value = value
        if isinstance(value, cgi.FieldStorage):
            self.filename = value.filename
            self.content = value.value
            self.file = value.file
    
class Validator:
    def __deepcopy__(self, memo): return copy.copy(self)
    def __init__(self, msg, test, jstest=None): utils.autoassign(self, locals())
    def valid(self, value): 
        try: return self.test(value)
        except: return False

notnull = Validator("Required", bool)

class regexp(Validator):
    def __init__(self, rexp, msg):
        self.rexp = re.compile(rexp)
        self.msg = msg
    
    def valid(self, value):
        return bool(self.rexp.match(value))

if __name__ == "__main__":
    import doctest
    doctest.testmod()