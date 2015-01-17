from web.template import CompiledTemplate, ForLoop, TemplateResult

import admin, site
_dummy = CompiledTemplate(lambda: None, 'dummy')
join_ = _dummy._join
escape_ = _dummy._escape

