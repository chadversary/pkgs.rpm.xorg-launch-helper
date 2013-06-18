#!/bin/bash

pkgname=xorg-launch-helper
date=20130618
sha=ac353a7
version=${date}.${sha}

tmpdir=$(mktemp -d)
git_dir=/$tmpdir/$pkgname.git

git clone --bare git://github.com/sofar/$pkgname.git $git_dir
git --git-dir=$git_dir archive --prefix=$pkgname-$version/ $sha \
    | xz > $pkgname-$version.tar.xz
