[app]
# (str) Title of your application
title = M-Browser Pro

# (str) Package name
package.name = m_browser_pro

# (str) Package domain (needed for android packaging)
package.domain = org.mubarak

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 1.0

# (list) Application requirements
# നിന്റെ ബ്രൗസറിന് ആവശ്യമായ ലൈബ്രറികൾ ഇതിലുണ്ട്
requirements = python3,kivy,requests,urllib3,certifi

# (str) Supported orientations
orientation = portrait

# (list) Permissions
# ഇന്റർനെറ്റ് കിട്ടാൻ ഇത് നിർബന്ധമാണ്
android.permissions = INTERNET

# (int) Target Android API
android.api = 31

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 23b

# (bool) Use the private directory for storage
android.private_storage = True

[buildozer]
# (int) Log level (2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
