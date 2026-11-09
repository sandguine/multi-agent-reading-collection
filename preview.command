#!/bin/sh
set -eu
collection_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
open "$collection_dir/docs/index.html"
