[app]
title = streaming
package.name = myapp
package.domain = org.streaming
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,xml
version = 0.1
requirements = python3,kivy,numpy,opencv, kivymd, ffpyplayer, pillow, android
orientation = portrait

# Android specific
fullscreen = 0
android.permissions = INTERNET
android.arch = armeabi-v7a
[buildozer]
log_level = 2
warn_on_root = 1
