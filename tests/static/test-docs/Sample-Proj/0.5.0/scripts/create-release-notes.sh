#!/bin/bash

set -uex
# get all available machines, and do a hacky indentation (using sed)

git fetch --tags
TAG='HEAD'
USAGE="Usage: $0 --blblb
"
while (( "$#" )); do
    case "$1" in
        "-t")
            ;&
        "--tag")
            NEWTAG=$2
            shift # Shift past argument
            ;;
        *)
            echo "Unknown argument: $1"
            echo "$USAGE"
            exit 1
            ;;
    esac
    shift
done
if [ -z ${NEWTAG+x} ]; then
    echo "No previous tag provided!"
    echo "$USAGE"
    exit 1
fi


BRANCH=`git rev-parse --abbrev-ref HEAD`

echo "Updating the changelog"
cat << EOF > temp.log

\section{Version: $NEWTAG}
Date of release $(date \+\%F)

\subsection*{What is new?}

\begin{itemize}
\item
\item
\end{itemize}

\subsection*{What is changed?}

\begin{itemize}
\item
\item
\end{itemize}

\subsection*{What is fixed?}

\begin{itemize}
\item
\item
\end{itemize}

% Please go through the list below, and add all items to the appropriate
% subsection above.

EOF
#git log $OLDTAG..$NEWTAG >> temp.log
sed -e '/newinsertionpoint/r./temp.log' -i ccu-releasenotes.tex
#sed -e 's/^commit.*//g' -i cs-os-docs/ccu-releasenotes.tex
#sed -e 's/^Author.*//g' -i cs-os-docs/ccu-releasenotes.tex
#sed -e 's/_/\\_/g' -i cs-os-docs/ccu-releasenotes.tex
#sed -e 's/&/\\&/g' -i cs-os-docs/ccu-releasenotes.tex
#sed -e 's/#/\\#/g' -i cs-os-docs/ccu-releasenotes.tex
#sed -e 's/\\\\_/\\_/g' -i cs-os-docs/ccu-releasenotes.tex
#sed -e 's/\\\\&/\\&/g' -i cs-os-docs/ccu-releasenotes.tex

# Add license manifest for all components in ccu-image
# Might need to add ccu-prod-image in the future.
#export `bitbake -e|grep  ^DISTRO_VERSION | tr -d '"'`
#export `bitbake -e|grep  ^MAHCINE | tr -d '"'`
#mkdir -p cs-os-docs/ccu-image
#cp $BUILDDIR/tmp/deploy/licenses/cschargeos-ccu-image-glibc-ipk-$DISTRO_VERSION-$MY_OE_CONF/* cs-os-docs/ccu-image
#git describe --long --always --dirty | sed 's/_/\\_/' > cs-os-docs/current-oe-tag



