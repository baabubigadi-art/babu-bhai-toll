[app]
title = Babu Bhai Toll
package.name = babubhaitoll
package.domain = org.babubhai
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0
orientation = portrait
fullscreen = 0
android.api = 30
android.minapi = 21
android.ndk = 25b
android.jdk = /usr/lib/jvm/java-17-openjdk-amd64
android.accept_sdk_license = True
android.archs = arm64-v8a
android.allow_backup = True
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 0
