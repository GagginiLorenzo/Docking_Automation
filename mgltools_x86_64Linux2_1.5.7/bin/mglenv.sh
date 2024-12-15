#!/bin/sh

#
# --- TSRI, Michel Sanner Copyright 2004 ---
#
# get absolute path to this script
case "`uname -s`" in
    Linux)
	SCRIPTDIR=$(unset -v CDPATH; cd "$(dirname "$(readlink -f $0 || echo $0)")" && pwd -P)
	;;
    Darwin*)
	SCRIPTDIR=$(unset -v CDPATH; cd "$(dirname "$(readlink $0 || echo $0)")" && pwd -P)
	;;
esac
# $SCRIPTDIR is not $WHERE_I_INSTALLED/bin

######
## Set some environment variable.
MGL_ROOT=$(dirname $SCRIPTDIR)
export MGL_ROOT

########
## plaform we run on
##
MGL_ARCHOSV=`$MGL_ROOT/bin/archosv`
export MGL_ARCHOSV

#######
## path to the extralibs directory.
##
MGL_EXTRALIBS="$MGL_ROOT/lib"
export MGL_EXTRALIBS

#######
## path to the extrainclude directory
MGL_EXTRAINCLUDE="$MGL_ROOT/include"
export MGL_EXTRAINCLUDE


########
## add the path to the directory holding the python interpreter to your path
##
PATH="$MGL_ROOT/bin:$PATH"
export PATH


TCL_LIBRARY="$MGL_ROOT/tcl8.5"
export TCL_LIBRARY

TK_LIBRARY="$MGL_ROOT/tk8.5"
export TK_LIBRARY

# Open Babel formats, plugins directory:
BABEL_LIBDIR="$MGL_ROOT/lib/openbabel/2.4.1"
export BABEL_LIBDIR
BABEL_DATADIR="$MGL_ROOT/share/openbabel/2.4.1"
export BABEL_DATADIR

# set path so we get the versions of command we expect
originalpath="$PATH"

# set the LD_LIBRARY PATH for each platform
case "`uname -s`" in
    Linux)
	LD_LIBRARY_PATH="$MGL_ROOT/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
	export LD_LIBRARY_PATH
	;;
    Darwin*)
        # NOTE: the user may have already set DISPLAY, so don't change it    
        if [ ! "$DISPLAY" ]; then
            DISPLAY=":0.0"
            export DISPLAY
        fi
        # If the X11 is not running, modify .xinitrc to remove xterm
        # This assumes X11 is installed!
        ps -wx -ocommand | grep -e '[X]11' > /dev/null;
        if [ \"$?\" != \"0\" -a ! -f ~/.xinitrc ]; then
            echo \"rm -f ~/.xinitrc\" > ~/.xinitrc
            sed 's/xterm/# xterm/' /opt/X11/lib/X11/xinit/xinitrc >> ~/.xinitrc                 
        fi 
	# This will start X11 which provides windows system.
	# which is needed to run ADT/PMV and VISION
	open -a XQuartz
	DYLD_LIBRARY_PATH="$MGL_ROOT/lib:${DYLD_LIBRARY_PATH:+:$DYLD_LIBRARY_PATH}"
	export DYLD_LIBRARY_PATH
	;;
esac


# system-dependent error checking
case "`uname -s`" in
	Linux)
		p0="/usr/lib/libGL.so.1"
		p1="/usr/X11R6/lib/libGL.so.1"
		if [ -f "$p0" -a -f "$p1" ]
		then
			ls0=`ls -Ll "$p0" | sed 's,/.*,,'`
			ls1=`ls -Ll "$p1" | sed 's,/.*,,'`
			if [ "$ls0" != "$ls1" ]
			then
				echo "OpenGL misconfiguration detected."
				echo "Please reinstall graphics driver."
				#exit 1
			fi
		fi
		;;
	Darwin*)
		;;
esac
 
# deduce any flags we want to pass to python
pyflags=""
for i in "$@"
do
	case $i in
	--opt)
		pyflags="$pyflags${pyflags:+ }-OO"
		# remove '--opt' from list of args
		shift
		;;
	esac
done

# using our distributed version of python, don't use any python
# environment variables, especialy PYTHONHOME and PYTHONPATH
unset PYTHONHOME
echo "setting PYTHONHOME environment"
PYTHONHOME="$MGL_ROOT"
export PYTHONHOME
PYTHONPATH="$MGL_ROOT/MGLToolsPckgs"
export PYTHONPATH
# prevent adding user site-packages such as ~/.local/lib/pythonX.Y/site-packages
# that might contain incompatible packages
export PYTHONNOUSERSITE="disabled"
python="$MGL_ROOT/bin/MGLpython2.7"
