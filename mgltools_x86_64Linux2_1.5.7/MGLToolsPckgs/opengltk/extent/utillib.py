# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.5
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_utillib', [dirname(__file__)])
        except ImportError:
            import _utillib
            return _utillib
        if fp is not None:
            try:
                _mod = imp.load_module('_utillib', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _utillib = swig_import_helper()
    del swig_import_helper
else:
    import _utillib
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



def void_void_array_get(idx):
    return _utillib.void_void_array_get(idx)
void_void_array_get = _utillib.void_void_array_get

_utillib.void_void_dim_swigconstant(_utillib)
void_void_dim = _utillib.void_void_dim

_utillib.void_void_NULL_swigconstant(_utillib)
void_void_NULL = _utillib.void_void_NULL

def void_GLenum_array_get(idx):
    return _utillib.void_GLenum_array_get(idx)
void_GLenum_array_get = _utillib.void_GLenum_array_get

_utillib.void_GLenum_dim_swigconstant(_utillib)
void_GLenum_dim = _utillib.void_GLenum_dim

_utillib.void_GLenum_NULL_swigconstant(_utillib)
void_GLenum_NULL = _utillib.void_GLenum_NULL

def void_int_array_get(idx):
    return _utillib.void_int_array_get(idx)
void_int_array_get = _utillib.void_int_array_get

_utillib.void_int_dim_swigconstant(_utillib)
void_int_dim = _utillib.void_int_dim

_utillib.void_int_NULL_swigconstant(_utillib)
void_int_NULL = _utillib.void_int_NULL

def void_int_int_array_get(idx):
    return _utillib.void_int_int_array_get(idx)
void_int_int_array_get = _utillib.void_int_int_array_get

_utillib.void_int_int_dim_swigconstant(_utillib)
void_int_int_dim = _utillib.void_int_int_dim

_utillib.void_int_int_NULL_swigconstant(_utillib)
void_int_int_NULL = _utillib.void_int_int_NULL

def void_int_int_int_array_get(idx):
    return _utillib.void_int_int_int_array_get(idx)
void_int_int_int_array_get = _utillib.void_int_int_int_array_get

_utillib.void_int_int_int_dim_swigconstant(_utillib)
void_int_int_int_dim = _utillib.void_int_int_int_dim

_utillib.void_int_int_int_NULL_swigconstant(_utillib)
void_int_int_int_NULL = _utillib.void_int_int_int_NULL

def void_int_int_int_int_array_get(idx):
    return _utillib.void_int_int_int_int_array_get(idx)
void_int_int_int_int_array_get = _utillib.void_int_int_int_int_array_get

_utillib.void_int_int_int_int_dim_swigconstant(_utillib)
void_int_int_int_int_dim = _utillib.void_int_int_int_int_dim

_utillib.void_int_int_int_int_NULL_swigconstant(_utillib)
void_int_int_int_int_NULL = _utillib.void_int_int_int_int_NULL

def void_unsignedchar_int_int_array_get(idx):
    return _utillib.void_unsignedchar_int_int_array_get(idx)
void_unsignedchar_int_int_array_get = _utillib.void_unsignedchar_int_int_array_get

_utillib.void_unsignedchar_int_int_dim_swigconstant(_utillib)
void_unsignedchar_int_int_dim = _utillib.void_unsignedchar_int_int_dim

_utillib.void_unsignedchar_int_int_NULL_swigconstant(_utillib)
void_unsignedchar_int_int_NULL = _utillib.void_unsignedchar_int_int_NULL

def void_unsignedint_int_int_int_array_get(idx):
    return _utillib.void_unsignedint_int_int_int_array_get(idx)
void_unsignedint_int_int_int_array_get = _utillib.void_unsignedint_int_int_int_array_get

_utillib.void_unsignedint_int_int_int_dim_swigconstant(_utillib)
void_unsignedint_int_int_int_dim = _utillib.void_unsignedint_int_int_int_dim

_utillib.void_unsignedint_int_int_int_NULL_swigconstant(_utillib)
void_unsignedint_int_int_int_NULL = _utillib.void_unsignedint_int_int_int_NULL

def void_int_voidstar_array_get(idx):
    return _utillib.void_int_voidstar_array_get(idx)
void_int_voidstar_array_get = _utillib.void_int_voidstar_array_get

_utillib.void_int_voidstar_dim_swigconstant(_utillib)
void_int_voidstar_dim = _utillib.void_int_voidstar_dim

_utillib.void_int_voidstar_NULL_swigconstant(_utillib)
void_int_voidstar_NULL = _utillib.void_int_voidstar_NULL

_utillib.sizeof_GLbitfield_swigconstant(_utillib)
sizeof_GLbitfield = _utillib.sizeof_GLbitfield

_utillib.sizeof_GLboolean_swigconstant(_utillib)
sizeof_GLboolean = _utillib.sizeof_GLboolean

_utillib.sizeof_GLbyte_swigconstant(_utillib)
sizeof_GLbyte = _utillib.sizeof_GLbyte

_utillib.sizeof_GLclampd_swigconstant(_utillib)
sizeof_GLclampd = _utillib.sizeof_GLclampd

_utillib.sizeof_GLclampf_swigconstant(_utillib)
sizeof_GLclampf = _utillib.sizeof_GLclampf

_utillib.sizeof_GLdouble_swigconstant(_utillib)
sizeof_GLdouble = _utillib.sizeof_GLdouble

_utillib.sizeof_GLenum_swigconstant(_utillib)
sizeof_GLenum = _utillib.sizeof_GLenum

_utillib.sizeof_GLfloat_swigconstant(_utillib)
sizeof_GLfloat = _utillib.sizeof_GLfloat

_utillib.sizeof_GLint_swigconstant(_utillib)
sizeof_GLint = _utillib.sizeof_GLint

_utillib.sizeof_GLshort_swigconstant(_utillib)
sizeof_GLshort = _utillib.sizeof_GLshort

_utillib.sizeof_GLsizei_swigconstant(_utillib)
sizeof_GLsizei = _utillib.sizeof_GLsizei

_utillib.sizeof_GLubyte_swigconstant(_utillib)
sizeof_GLubyte = _utillib.sizeof_GLubyte

_utillib.sizeof_GLuint_swigconstant(_utillib)
sizeof_GLuint = _utillib.sizeof_GLuint

_utillib.sizeof_GLushort_swigconstant(_utillib)
sizeof_GLushort = _utillib.sizeof_GLushort

def glCleanRotMat(*args, **kwargs):
    return _utillib.glCleanRotMat(*args, **kwargs)
glCleanRotMat = _utillib.glCleanRotMat

def extractedGlutSolidSphere(*args, **kwargs):
    return _utillib.extractedGlutSolidSphere(*args, **kwargs)
extractedGlutSolidSphere = _utillib.extractedGlutSolidSphere

def solidCylinder(*args, **kwargs):
    return _utillib.solidCylinder(*args, **kwargs)
solidCylinder = _utillib.solidCylinder

def namedPoints(*args, **kwargs):
    return _utillib.namedPoints(*args, **kwargs)
namedPoints = _utillib.namedPoints

def glDrawSphereSet(*args, **kwargs):
    return _utillib.glDrawSphereSet(*args, **kwargs)
glDrawSphereSet = _utillib.glDrawSphereSet

def glDrawCylinderSet(*args, **kwargs):
    return _utillib.glDrawCylinderSet(*args, **kwargs)
glDrawCylinderSet = _utillib.glDrawCylinderSet

def glDrawIndexedGeom(*args, **kwargs):
    return _utillib.glDrawIndexedGeom(*args, **kwargs)
glDrawIndexedGeom = _utillib.glDrawIndexedGeom

def triangleNormalsPerFace(*args, **kwargs):
    return _utillib.triangleNormalsPerFace(*args, **kwargs)
triangleNormalsPerFace = _utillib.triangleNormalsPerFace

def triangleNormalsPerVertex(*args, **kwargs):
    return _utillib.triangleNormalsPerVertex(*args, **kwargs)
triangleNormalsPerVertex = _utillib.triangleNormalsPerVertex

def triangleNormalsBoth(*args, **kwargs):
    return _utillib.triangleNormalsBoth(*args, **kwargs)
triangleNormalsBoth = _utillib.triangleNormalsBoth
def glTriangleNormals(vertices, triangles, mode = "PER_FACE" ):
    if mode == "PER_FACE":
        return triangleNormalsPerFace(vertices, triangles)
    elif mode == "PER_VERTEX":
        return triangleNormalsPerVertex(vertices, triangles)
    elif mode == "BOTH":
        return triangleNormalsBoth(vertices, triangles)

# This file is compatible with both classic and new-style classes.

attachCurrentThread = _utillib.attachCurrentThread
detachCurrentThread = _utillib.detachCurrentThread
attachedThread = _utillib.attachedThread
glTrackball = _utillib.glTrackball

