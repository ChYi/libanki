# -*- coding: utf-8 -*-
# Copyright: Damien Elmes <anki@ichi2.net>
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

from anki.models import Model
from anki.lang import _

models = []

# Basic
##########################################################################

def BasicModel(deck):
    m = Model(deck)
    m.name = _("Basic")
    fm = m.newField()
    fm['name'] = _("Front")
    fm['req'] = True
    fm['uniq'] = True
    m.addField(fm)
    fm = m.newField()
    fm['name'] = _("Back")
    m.addField(fm)
    t = m.newTemplate()
    t['name'] = _("Forward")
    t['qfmt'] = "{{" + _("Front") + "}}"
    t['afmt'] = "{{" + _("Back") + "}}"
    m.addTemplate(t)
    t = m.newTemplate()
    t['name'] = _("Reverse")
    t['qfmt'] = "{{" + _("Back") + "}}"
    t['afmt'] = "{{" + _("Front") + "}}"
    t['actv'] = False
    m.addTemplate(t)
    return m

models.append((_("Basic"), BasicModel))

# Cloze
##########################################################################

def ClozeModel(deck):
    m = Model(deck)
    m.name = _("Cloze")
    fm = m.newField()
    fm['name'] = _("Text")
    fm['req'] = True
    fm['uniq'] = True
    m.addField(fm)
    fm = m.newField()
    fm['name'] = _("Notes")
    m.addField(fm)
    for i in range(8):
        n = i+1
        t = m.newTemplate()
        t['name'] = _("Cloze") + " %d" % n
        t['qfmt'] = ("{{#cloze:%d:Text}}<br>{{cloze:%d:%s}}<br>"+
                     "{{/cloze:%d:Text}}") % (n, n, _("Text"), n)
        t['afmt'] = ("{{cloze:%d:" + _("Text") + "}}") % n
        t['afmt'] += "<br>{{" + _("Notes") + "}}"
        m.addTemplate(t)
    return m

models.append((_("Cloze"), ClozeModel))
