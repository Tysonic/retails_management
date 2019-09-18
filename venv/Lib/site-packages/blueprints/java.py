import os
import sys

from pkg_resources import resource_filename


divider = ';' if sys.platform == "win32" else ':'


def add_to_class_path(javalib):
    try:
        class_path = resource_filename(javalib, '')
    except ImportError:
        pass
    else:
        if 'CLASSPATH' not in os.environ:
            os.environ['CLASSPATH'] = class_path + '/*'
        else:
            os.environ['CLASSPATH'] = '%s%s%s/*' % (
                os.environ['CLASSPATH'],
                divider,
                class_path
            )

class_path = resource_filename(__name__, 'javalib')


if not 'CLASSPATH' in os.environ:
    os.environ['CLASSPATH'] = ''


os.environ['CLASSPATH'] = '%s%s%s/*' % (
    os.environ['CLASSPATH'],
    divider,
    class_path
)


from jnius import autoclass
from jnius.reflect import Object


def to_java(value):
    if isinstance(value, Object):
        return value
    elif isinstance(value, (str, unicode)):
        String = autoclass('java.lang.String')
        return String(value)
    elif isinstance(value, int):
        Integer = autoclass('java.lang.Integer')
        return Integer(value)
    elif isinstance(value, float):
        Float = autoclass('java.lang.Float')
        return Float(value)
    # elif isinstance(value, long):
    #     Long = autoclass('java.lang.Long')
    #     return Long(value)
    elif isinstance(value, list):
        return value
    elif isinstance(value, dict):
        map = autoclass('java.util.HashMap')()
        for k, v in value.iteritems():
            map.put(k, to_java(v))
        return map
    else:
        raise TypeError('type not supported')


def from_java(value):
    if isinstance(value, autoclass('java.lang.Integer')):
        return value.intValue()
    # if isinstance(value, autoclass('java.lang.Long')):
    #     return value.longValue()
    if isinstance(value, autoclass('java.lang.Float')):
        return value.floatValue()
    if isinstance(value, autoclass('java.util.ArrayList')):
        out = []
        iterator = value.iterator()
        while iterator.hasNext():
            out.append(from_java(iterator.next()))
        return out
    return value
